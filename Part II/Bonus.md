# Part III.Bonus
### If you were to adopt a container orchestration engine and an associated compute engine on AWS to replace EC2 and AutoScalingGroup:
### What would you use? Why do you think you would like to work with your selected option based on your personal preference?
If I were to adopt a container orchestration engine and an associated compute engine on AWS to replace EC2 and AutoScaling Group,
**a. For a Container Orchestration Engine:**
I would use **Amazon Elastic Kubernetes Service (Amazon EKS)**. The reasons are:
- Kubernetes is a widely adopted and popular choice for container orchestration systems for automating software deployment, scaling, and management. Also, Kubernetes has a large community. 
- Amazon EKS is a fully managed Kubernetes service to run Kubernetes in the AWS cloud, which means AWS will take care of the control plane: It runs and scales across multiple AWS Availability Zones to ensure high availability. This aligns with the requirement of spanning Subnets across all 3 AZs. Moreover, EKS scales with the application needs, automatically adjusting the number of nodes in our cluster based on demand. Therefore, these give us a free of mind and we can focus on deploying and managing our applications rather than worrying about the underlying Kubernetes infrastructure.
- In addition, related to security, Amazon EKS integrates with AWS Identity and Access Management (IAM) for authentication and authorisation, providing a secure way to control access to your Kubernetes clusters. This aligns with your security requirements for different tiers in the VPC.
- To sum up, I think this integration aligns well with the existing AWS infrastructure that we have.
**b. For an associated Compute Engine:**
To replace EC2 and AutoSclaing Group, for an associated compute engine, I would use **AWS Fargate** going together with AWS EKS. The reasons are:
- AWS Fargate can operate on a serverless model, where you don't need to manage the underlying EC2 instances. This aligns with the requirement of replacing EC2 and Auto Scaling Group.
- AWS Fargate can automatically scale based on the needs of our application.
- Moreover, in terms of cost, Fargate gives you a flexible option compared to the traditional EC2 instances in that we can pay for the vCPU and memory that our container consumes.

### Which benefits would you gain over EC2 combined with AutoScalingGroup?
Adopting Amazon EKS with AWS Fargate offers several key benefits over the traditional EC2 combined with the Auto Scaling Groups model. 
- Firstly, the use of EKS introduces a fully managed Kubernetes service, ensuring high availability across multiple AWS Availability Zones and automatically scaling the infrastructure based on application demand. This eliminates the need for manual intervention in scaling configurations and enhances overall resource efficiency. 
- Additionally, EKS integrates with existing AWS infrastructure, providing a cohesive environment for application deployment. 
- Transitioning to Fargate further streamlines operations by abstracting away the need to manage EC2 instances, allowing for a serverless model that automatically scales and efficiently utilises resources. 
- Lastly, the combination of EKS and Fargate presents a modern, secure, and cost-effective solution, enabling a focus on application development while offloading infrastructure management complexities associated with EC2 and Auto Scaling Groups.

---

### What problem does Service Discovery solve?
- Service Discovery is a way for you to discover different APIs using the registered name. Service Discovery enables automated registration, discovery, and resolution of service endpoints, ensuring that applications can communicate with each other efficiently, regardless of their current location or scaling state. In a containerised environment with microservices, where services can scale up or down dynamically, maintaining an up-to-date registry of service locations becomes crucial.

### What is the Service Discovery AWS offering for your Container Orchestration and Compute option?
- **AWS Cloud Map** is the Service Discovery AWS offering for my Container Orchestration (AWS EKS) and Compute (Fargate) option.

---

### What problem does Service Mesh solve?
- A service mesh acts as a dedicated software layer managing communication between microservices in a scalable application. 
- As applications scale and the number of microservices increases, it becomes challenging to monitor the performance of these services. A service mesh addresses this complexity by providing features such as monitoring, logging, tracing, and traffic control. It operates independently of each service's code, enabling it to work across network boundaries and with multiple service management systems. 
- The adoption of a service mesh is driven by the need for service-level observability, providing visibility into service communication, and service-level control for administrators enforcing fine-grained governance. 

### What is the AWS Service Mesh offering for your Container Orchestration and Compute option?
- **AWS App Mesh** is the service mesh offering for my Container Orchestration (AWS EKS) and Compute (Fargate) option. 