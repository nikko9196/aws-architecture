# Part I.1.
### Explain eventual and strong consistency
- Eventual consistency is a consistency model, which means that after a write, reads will eventually see it (typically within milliseconds). Data is replicated asynchronously. It means that during the short-term period, users accessing different data centres may observe different versions of the data. The trade-off in eventual consistency is made to achieve better availability and partition tolerance in the CAP theorem (Consistency, Availability, Partition Tolerance).
- Strong consistency is a consistency model, which means that after a write, reads will see it and the reads are consistent with the write. Data is replicated synchronously. It ensures that all nodes in the system see the same data for a given entity at the same time and are available across all server nodes globally.

Reference: https://medium.com/@abhirup.acharya009/strong-consistency-vs-eventual-consistency-19ce6f87c112
---

### Which AWS persistent services/feature should you expect eventual consistency?
- We should expect eventual consistency in AWS DynamoDB and AWS Key Management Service (KMS). 
- DynamoDB tables, including local and global secondary indexes, default to eventual consistency for reads. Similarly, the AWS KMS's API follows an eventual consistency model, indicating that changes to KMS resources may not be immediately visible in subsequent commands.

Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.htmlhttps://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html
---

### Which AWS persistent services/feature should you expect strong consistency?
- AWS S3: Since the end of 2020, S3 has become strong consistency: For example,  GET, PUT, and LIST operations are now strongly consistent. 
- Amazon RDS for PostgreSQL: Amazon RDS for PostgreSQL, similar to traditional SQL databases, ensures ACID compliance (ACID = Atomic, Consistent, Isolated, and Durable), making it reliable for transaction processing and maintaining data consistency. With robust support for complex queries and indexing, PostgreSQL exhibits high performance, addressing critical needs like order processing, user authentication, and inventory management.

Reference: Link: https://aws.amazon.com/blogs/aws/amazon-s3-update-strong-read-after-write-consistency/
---

### Name some (2-3) usecases where eventually consistent persistences are acceptable
Eventually consistent persistences are acceptable in the usecases where real-time consistency is not very vital:
- The Internet Domain Name System (DNS) is a well-known/ classic example of a system with an eventual consistency model. DNS servers do not show us the latest values but, rather, the values are cached and replicated across many directories over the Internet.
- The second usecase is the Social Media Feeds: In social media applications, where users post updates and share content, eventual consistency can be acceptable. Users might not expect immediate consistency across all devices or when accessing the platform from different locations. As long as the updates eventually reach all users, it meets the requirements of the use case.

