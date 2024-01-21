# Part I.2.
### Explain the need for messaging integration
- Messaging integration is essential for enterprises managing independently developed applications across diverse languages and platforms. The imperative arises from the necessity to achieve responsive data and process sharing. Utilising messaging not only facilitates the frequent, immediate, and reliable transfer of data packets asynchronously in customisable formats but also supports loose coupling between applications, ensuring independence in development and maintenance. 
- This established approach, successfully implemented across enterprises for years, serves as a cornerstone for integrating systems while enabling workflow automation, event-driven architecture, and the integration of diverse technologies.


### Why should we use message brokers in microservices architecture?
- A message broker, functioning as software, facilitates message exchange among applications, systems, and services, and enables efficient message queuing, routing and delivery. A key responsibility lies in swift message enqueuing to allow for high concurrency and throughput. In the message broker framework, services can function both as message producers and consumers. Initiating asynchronous operations, message producers publish messages to the broker, which subsequently buffers them in a queue until consumed by the intended services.
- Message brokers play an important role in microservices by decoupling services, enabling interaction without intricate knowledge of each other. This fosters ease in modifying, replacing, or adding new services without disrupting the entire system. They contribute to scalability through independent scaling based on workloads, facilitate reliability by ensuring message persistence and fault tolerance, and enable the implementation of agile, responsive event-driven architectures. The flexibility in supporting various communication patterns like publish-subscribe, request-response, and queuing empowers developers to choose the most fitting pattern for their specific use case.
---
References:
https://redis.com/solutions/use-cases/message-broker-pattern-for-microservices-interservice-communication/
https://serverlessland.com/event-driven-architecture/visuals/why-use-message-brokers
https://jackynote.medium.com/message-brokers-pros-cons-and-their-crucial-role-in-microservice-3dc6c0df2e53#:~:text=Message%20brokers%20are%20a%20cornerstone,of%20the%20microservices%20being%20built.


### Find AWS architecture references for the use of message broker in microservices.
