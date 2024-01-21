# Part I.3.
### Explain the differences between point-to-point messaging pattern (Queue) and publish/subscribe pattern (Pub/Sub)
**1. Message recipients:**
- Point-to-point: Messages are sent from one sender to one specific receiver. While the channel can have multiple receivers consume messages concurrently, each message is consumed by only one receiver at a time.
- Pub/Sub: Messages are broadcast to multiple subscribers. The Producer (sender) publishes messages to a Topic, and multiple subscribers (receiver) can receive and process these messages independently. Each message can be consumed by multiple subscribers. 

**2. Message Consumption:**
- Point-to-point: Messages are put onto the queue by the sender and the receiver will consume the messages from the queue. However, the channel can provide a buffer for messages and the consumer can control the rate of consumption. Messages persist until the consumer processes them and delete them from the queue.
- Pub/Sub: It uses the Push Model, where messages are pushed to downstream consumers instead of consumers pulling messages from a queue.

**3. Receivers and Scalability:**
- Point-to-point: The message sender must know the specific receiver, creating a one-to-one relationship. However, point-to-point channels can support many concurrent receivers, allowing for scalability.
- Pub/Sub: Message publishers do not need to know where the messages will be consumed. It enables One-to-Many Communication, allowing multiple subscribers to be interested in the same set of messages and facilitating dynamic scalability.
--
References:
https://www.ibm.com/docs/en/wip-mg/2.0.0?topic=concepts-publishsubscribe
https://www.ibm.com/docs/en/wip-mg/2.0.0?topic=concepts-point-point-messaging
https://programmingsharing.com/point-to-point-and-publish-subscribe-messaging-model-2efc4d2b6726
https://serverlessland.com/event-driven-architecture/pub-sub-messaging
https://serverlessland.com/event-driven-architecture/point-to-point-messaging


### When would you use point-to-point messaging over the other?
- Based on its characteristics, we will use point-to-point messaging for task distribution among many different workers. A single worker will consume a particular task from the queue, process it, and then remove it from the queue, preventing others from processing it.
-- 
References:
- https://serverlessland.com/event-driven-architecture/visuals/point-to-point-messaging
https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html

### When would you use publish/subscribe over the other?
- Based on its characteristics, this model is suitable for scenarios where multiple components or services are interested in the same event or type of information, such as broadcasting notifications. 
- For example, in an airline situation related to the time update of a flight, multiple parties will be interested in this information, such as ground crews, baggage handlers, flight attendants and pilots preparing for the next trip, and so on. In this case, the pub/sub model is more suitable. 
--
References:
https://programmingsharing.com/point-to-point-and-publish-subscribe-messaging-model-2efc4d2b6726
https://serverlessland.com/event-driven-architecture/visuals/publish-subscribe


### Find AWS architecture references for point-to-point messaging
Reference: https://aws.amazon.com/blogs/compute/implementing-enterprise-integration-patterns-with-aws-messaging-services-point-to-point-channels/
(diagram of point-to-point)
![Point-to-Point_One-way_Traditional Messaging](<Diagrams_and_Images/Point-to-Point_One-way_Traditional Messaging.jpeg>)
![Point-to-Point_One-way_Cloud-Native Messaging](<Diagrams_and_Images/Point-to-Point_One-way_Cloud-Native Messaging.jpeg>)
This blog expertly navigates the intricacies of enterprise integration patterns with AWS messaging services, specifically focusing on the important concept of point-to-point messaging. It effectively contrasts traditional messaging using Amazon MQ with cloud-native alternatives such as Amazon SQS and Amazon SNS. By illustrating one-way messaging scenarios, the article underscores the adaptability of Amazon MQ queues for traditional methods and Amazon SQS queues for cloud-native implementations. 
![Point-to-Point_Request-Response_Traditional Messaging](<Diagrams_and_Images/Point-to-Point_Request-Response_Traditional Messaging.jpeg>) 
![Point-to-Point_Request-Response_Cloud-Native Messaging](<Diagrams_and_Images/Point-to-Point_Request-Response_Cloud-Native Messaging.jpeg>)
Additionally, the discussion extends to request-response messaging, showcasing the application of both traditional (Amazon MQ) and cloud-native (Amazon SQS) approaches.




