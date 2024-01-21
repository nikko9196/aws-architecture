# Part I.6.
### Given a simple AWS EC2 in a Auto Scaling Group architecture with ALB and a dedicated DB instance, name 5 system design components/techniques that can help you scale your system to meet more end-customers demand. Hinted layers: Static content cache / Dynamic content cache / Compute distribution / Persistency / Decoupling methods
### For each component, explain in few words (other than adding complexity), what are the trade offs of introducing these components if they weren't added before
5 system design components/ techniques that can help to scale your system to meet more end-customers demand:
**1. Static Content Cache with Amazon CloudFront (CDN):**
- We can integrate CloudFront to cache and deliver static content/files such as HTML/CSS/JS, photos, and videos from edge locations. This minimises the load on the origin server (EC2 instances) and reduces latency for end-users. As the number of end-customers increases, the global distribution of cached content ensures efficient delivery, improved response times, and reduced load on the central infrastructure.
- **Trade-offs:** While CloudFront enhances performance, there might be costs associated with data transfer and cache invalidation complexities.

**2. Dynamic content cache with Amazon ElastiCache:**
- Amazon ElastiCache, whether using Redis or Memcached, helps scale the system by offloading read-intensive queries from the main database. This reduces the load on the database server and enhances overall system responsiveness. As the user base grows, the in-memory caching provided by ElastiCache ensures faster access to frequently requested dynamic data, contributing to improved system scalability.
- **Trade-offs:** The management of cache consistency and the potential for data staleness, along with the additional operational overhead of maintaining the cache, can pose challenges in a system.

**3. Compute Distribution with Elastic Load Balancer:**
- Elastic Load Balancer (ELB) distributes incoming traffic across multiple EC2 instances, enabling the system to handle a larger number of concurrent requests. As end-customer demand increases, ELB dynamically scales the capacity up or down based on traffic patterns. This ensures optimal resource utilisation, high availability, and the ability to accommodate more users without compromising performance.
- **Trade-offs:** Firstly and importantly, costs may also increase as instances scale. Moreover, session management introduces challenges in handling state between distributed instances.

**4. Persistency with Amazon RDS Read Replicas:**
- Using RDS Read Replicas helps the system scale by distributing read and write operations. Read replicas offload read queries, reducing the load on the primary database so that it can focus on write-intensive operations. The distributed nature of Read Replicas supports the system in efficiently handling a larger number of concurrent read requests, contributing significantly to scalability without compromising performance.
- **Trade-offs**: Additional costs may be associated with maintaining and synchronising replicas. Moreover, managing data consistency demands careful oversight, given the potential for a slight delay in aligning updates between the primary database and its associated replicas.

**5. Decoupling methods with Amazon SQS, Lambda, and EventBridge:**
- Decoupling components using services like SQS, Lambda, and EventBridge contributes to system scalability by enabling asynchronous and event-driven architectures. This allows individual components to scale independently. For example, if a part of the system experiences a surge in demand, it can trigger events that are processed asynchronously by other components. This decoupled approach helps the system adapt to varying workloads and ensures scalability without tightly coupling components.
- **Trade-offs:** Managing the order of messages, preventing duplicates, and handling asynchronous processing can be challenging. Additionally, coordinating events across services may introduce potential complexities.
