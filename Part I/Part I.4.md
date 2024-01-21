# Part I.4.
### Explain idempotency in the context of transactional processing
Idempotency ensures that an action can be repeated without changing the result from its initial application. This concept is crucial in transactional processing, such as online shopping scenarios. For instance, pressing the "pay" button multiple times should not result in placing the order more than once. In financial transactions, idempotency is important to prevent accidental double charges to customers or making multiple payments to vendors.

---

### What does it mean to have an idempotent consumer?
The idempotent consumer functions as a Message Filter, ensuring the exclusion of duplicate messages. It mitigates the risk of unintended consequences or disruptions to the system caused by the presence of duplicate messages.

---

### Given SQS as the message broker, and Lambda function as the message consumer
### How would you implement Lambda as an idempotent consumer?
This is a diagram that I found on the AWS page relating to Processing Payments. The diagram shows the application of SQS, the Lambda function, and a third-party API that the function calls for payment:

![Idempotency - Payment Process](<Diagrams_and_Images/Idempotency - Payment Process.png>)

**To implement Lambda as an idempotent consumer, we should use Idempotent Processing Logic:**
- Annotate the "process" method responsible for handling a single payment record with the @IdempotencyKey annotation, which specifies which parametre is used as the idempotency key.
- The idempotent feature ensures that if an SQS record with the same payload is received more than once, the third-party API is not called multiple times. Subsequent calls return before invoking the "process" method.

**Handle Exceptions and Retries (and consider to use Lambda Powertools):**
- If an exception is thrown from the "process" method, the idempotency feature does not store the idempotency state in the persistence layer. This allows for safe retries, particularly if the third-party API returns a server-side error.
- By default, if one message from a batch fails, all messages in the batch are retried. This approach ensures consistency and helps in handling partial failures.
- Moreover, we can consider to use Lambda Powertools. It provides additional modules such as the SQS Batch Processing module, which assists in handling partial failures that may occur during batch processing.

Reference: 
- https://aws.amazon.com/blogs/compute/handling-lambda-functions-idempotency-with-aws-lambda-powertools/

### Which component would become the bottleneck when you implement idempotent consumers?
Lambda, SQS or third-party API would become the bottleneck when you implement idempotent consumers. For examples:
- **Lambda Function** Concurrency Limit: If the incoming message volume exceeds the Lambda function's concurrency limit, it may lead to processing delays and potential throttling.
- **SQS** Message Visibility Timeout: If the Lambda function's processing time surpasses the SQS message visibility timeout, messages might become visible to other consumers before processing is completed.
- **Third-party API** with the limitations of resources: such as database connection pool limits, throughput and query limits, or compute resource constraints, may struggle to handle the computational load imposed by the Lambda function.

References:
- https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html