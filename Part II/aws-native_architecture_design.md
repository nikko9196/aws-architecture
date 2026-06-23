# Part II: AWS Native Architecture Design

## Design Requirements

- The client wishes to build a news aggregator web app to earn money with Google Ads
  - The backend constantly look for latest news from many different news websites. Some sites require refreshing data every 10 seconds, some sites less frequently
  - Save the aggregated news headline and links into a no management database with infinite scale
  - The backend should use a no management API Gateway to allow for the static website to make API calls to
- The website should be ideally
  - Very cheap to host, and
  - Deployed to a globally available CDN
  - Completely billed by on-demand pricing models
  - Has no management effort required, except for incident resolution
- Both the API Gateway and the static website have domain name
  - Static website has CNAME `www.` points to `bestnewsaggregator.com`
  - API Gateway has domain record `api.`
  - The API Gateway should be protected against Layer 7 attacks such as SQL injection, or DDOS protection
  - Both need to be secured by SSL certificate from a publicly trusted CA
- The backend should be consisted of:
  - `GET /news API` to get the latest news from the static website. It may look at geolocation, device, and browser information to customize the news resource
  - `GET /news API` response should also be cached to save infrastructure cost
  - Only the Origin `www.` should be able to make request to `api.` (CORS)
  - A scheduler component that trigger scalable backend job to fetch for latest news articles
  - Fetched links need to be checked if they are actually new according to the internal database with infinite scale mentioned earlier
  - The combination infrastructure of scheduling + fan-out scheduling event to the list of new source + get news executor should be fast, management free, and scalable
  - Some news sources are only updated once daily while others are known to have new articles to be released at any given moment. Thus, the design should be able to trigger news source aggregators tailored for individual websites at a different rate, depending on the frequency settings of each of the crawled websites. Note that there are thousands of websites thus the chosen scheduling setup should be scalable to reduce overheads on the engineers to add more sources.

---

## My final architecture design based on the requirements of the client:

![PartII_AWS_Native_Architecture_Design](PartII_AWS_Native_Architecture_Design.png)

---

### Notes on the AWS Components on how some of the requirements are fulfilled:

Let's break down the requirements of the client so that we can find the best suitable options for each of them:

**1. For Static Website Hosting:**

- The client wishes to have a website, which is very cheap to host. Therefore, **Amazon S3** is the most suitable one. Moreover, they want the website to be deployed to a globally available CDN, and **AWS CloudFront** can fulfil this requirement.
- Moreover, these two services are billed by on-demand pricing models: S3's bill is charged based on storage and data transfer, and CloudFront's bill is charged based on data transfer and requests. However, the AWS free-tier option is available for these 2 services, which saves the client more cost.
- Because the static website has CNAME www. points to bestnewsaggregator.com, and API Gateway has domain record api., **AWS Route53** can be a solution for this requirement.
- Both the API Gateway and the static website require SSL certificates from a reputable Certificate Authority (CA) for security. AWS offers a convenient solution called **AWS Certificate Manager (ACM)**, which can handle the signing of SSL certificates for us.
- **AWS WAF** will be used to protect the API Gateway (and also the static website) against attacks from hackers (and Layer 7 attacks such as SQL injection, or DDOS protection). AWS WAF will be attached at/on CDN, and has filter rules to detect any suspicious requests.

**2. Back-end for API requests:**

- The back-end should use a no-management API Gateway to allow for the static website to make API calls. Only the Origin www. should be able to make requests to api. (CORS). With these 2 requirements, we will use **AWS API Gateway**.
- When the system receives the GET/news API to get the latest news from the static website, it may look at geolocation, device, and browser information to customise the news and resource. We will use **AWS Lambda** to write a function. Inside the Lambda function, we will analyse this information, and based on this information, the back end will fetch and customise the latest news accordingly.
- The client requested that the GET/news API response should also be cached to save infrastructure costs. Both **AWS API Gateway** and **AWS CloudFront** have their caching option. If your API serves a global audience or if you want to cache static assets along with API responses, CloudFront might be a more cost-effective solution. CloudFront can help offload traffic from your origin server and reduce the load on your infrastructure. However, if your API is primarily serving a specific region and you only need caching for API responses, AWS API Gateway caching may be simpler and more cost-effective. Therefore, depending on the more specific situation of the client, we can choose either one of these two options.

**3. Back-end with fetching data from external news websites:**

To fetch data from external news websites, the clients have some requirements:

- The backend constantly looks for the latest news from many different news websites and fetches data at different rates. It requires a scheduler component to initiate scalable backend tasks for fetching the most recent news articles. Because there are thousands of websites thus the chosen scheduling setup should be scalable to reduce overheads on the engineers to add more sources. The recommendation for this requirement is to use **AWS EventBridge Scheduler**. This service is highly scalable and allows you to schedule millions of tasks that can invoke many AWS services and over 6,000 API operations. Delivering schedules at scale and reducing maintenance costs, EventBridge Scheduler eliminates the necessity for infrastructure provisioning, management, and integration with multiple services.
- For saving aggregated news headlines and links into a no-management database with infinite scalability, consider using **Amazon DynamoDB**, a fully managed NoSQL database service provided by AWS. DynamoDB is designed to provide scalability, low-latency performance, and automatic scaling based on your needs.
- When the links are fetched and saved back to our database (AWS Dynamo DB as suggested above), fetched links need to be checked if they are actually new according to the internal database. **Lambda** functions can do the job here: From fetching data from external websites to checking whether the data is new or old. If the data (news) is new, it will add it back to DynamoDB. Otherwise, the data will be ignored.
- For a fast, management-free, and scalable infrastructure combining scheduling, fan-out scheduling events to the list of news sources, and executing news retrieval, we can consider using **AWS Step Functions** for orchestrating the workflow.

**4. Incident Resolution:**

- From the client's requirement, the website should ideally have no management effort required, except for incident resolution. If there are issues with the Lambda functions in your workflow or architecture, **AWS SNS** can be employed to notify developers of the company, allowing them to promptly address any problems.

---

### Note: Traffic flows:

![PartII_AWS_Native_Architecture_Design](PartII_AWS_Native_Architecture_Design.png)

**Front-end: Blue-marking numbers:**

- 1->7: After typing the domain name of the website, the browser client can access it and then see the front-end interface of the website returning back to them.

**Back-end, with API requests: Black-marking numbers:**

- 1->3: If the browser client interacts with the website (for example, clicking any button to read any news, which means they are sending the GET/news API request).

- 4->5: When the GET API request reaches the API Gateway. If the API Gateway receives any requests, it will trigger the Lambda function to query items from the database DynamoDB based on the requests' details.

- 6->9: Then, the GET API responses will be returned back to the client.

**Back-end, fetching data from external news websites: Red-marking numbers:**

- 1: EventBridge Scheduler has scheduled tasks and will trigger the Lambda function to fetch data from external news websites, depending on the schedules for different websites.

- 2: The first Lambda function will fetch data (news/articles) from external news websites. External News Websites are normally public, so we do not need to have any IAM Role to fetch the data.

- 3: Data from external news websites is returned back to us.

- 4: After getting the data (news/articles), the second Lambda function will do the task of checking if this data is new or not.

- 5: The second Lambda function queries data from DynamoDB to do a comparison.

- 6: Requested data getting from DynamoDB is returned back to the second Lambda function.

- 7: The second Lambda function will check whether the latest fetched data is new or not by comparing the links of two articles because that is a unique identifier for each news/article.

- 8: If data is new, it will be saved to DynamoDB. Otherwise, the data will be ignored.

**Handling incident:**

- Also, if the execution fails, it will trigger the AWS SNS to send messages to notify developers of the company about the issues.
