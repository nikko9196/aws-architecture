# Part II.1. - Base Design Questions:
### My final architecture design based on the requirements for part II.1:

![Assignment2_PartII_Official Design-Part II.1](<Diagrams_and_Images/Assignment2_PartII_Official Design-Part II.1.png>)


### The division table of CIDR:
![CIDR - Divided based on tiers-01](<Diagrams_and_Images/CIDR - Divided based on tiers-01.png>)
![CDIR - Divided based on AZs-01](<Diagrams_and_Images/CDIR - Divided based on AZs-01.png>)
---

# Part II.2. - Expansive Network Design Questions:
### 1. How would you add access for the EC2 instances to S3 and DynamoDB?

![Assignment2_PartII_Official Design-Part II.2.1](<Diagrams_and_Images/Assignment2_PartII_Official Design-Part II.2.1.png>)

**Explain the method:**
- The most convenient method to add access for the EC2 instances to S3 and DynamoDB is by using the Gateway VPC Endpoints. 
- Gateway VPC endpoints establish a secure connection to Amazon S3 and DynamoDB without the necessity for an internet gateway or a NAT device in your VPC. Gateway endpoints differ from other types of VPC endpoints as they don't utilise AWS PrivateLink, which is simple.
- Moreover, there is no additional charge for using Gateway Endpoints.
- To extend my explanation, actually, we can also use Interface VPC Endpoints to access S3 (but not DynamoDB). Interface Endpoints enable connectivity to services over AWS PrivateLink. However, Interface VPC Endpoints are implemented using Elastic Network Interfaces (ENIs). They offer more advanced features and depending on your network design and scale, this can lead to a larger number of ENIs, potentially impacting resource utilisation in your VPC. In addition, Interface VPC Endpoints' usage for S3 is billed.
- Therefore, the best option to add access for the EC2 instances to both S3 and DynamoDB is with Gateway VPC Endpoints.



---

### 2. Given that there are 2 AutoScalingGroups for 2 different applications, illustrate the flow of traffic in 3 different Network diagram figures (use the Base design figure as a starting point):
### A. In Green arrows: from 1 API Service Group to another (1 separate figure expected)
**Option 1: 2 API Service Groups on the same subnet:**
![Assignment2_PartII_Official Design-Part II.2.2.A(1)](<Diagrams_and_Images/Assignment2_PartII_Official Design-Part II.2.2.A(1).png>)

**Option 2: 2 API Service Groups on different AZs:**
![Diagrams_and_Images/Assignment2_PartII_Official Design-Part II.2.2.A(2)](<Diagrams_and_Images/Assignment2_PartII_Official Design-Part II.2.2.A(2).png>)

### B. In Orange arrows: from 1 API Service to reach out to Google Maps API in the public internet to get more data (another separate figure expected)
![Assignment2_PartII_Official Design-Part II.2.2.B](<Diagrams_and_Images/Assignment2_PartII_Official Design-Part II.2.2.B.png>)


### C. In Blue arrows: requests from public internet to reach one of the API Services (and another separate figure expected)
![Assignment2_PartII_Official Design-Part II.2.2.C](<Diagrams_and_Images/Assignment2_PartII_Official Design-Part II.2.2.C.png>)


