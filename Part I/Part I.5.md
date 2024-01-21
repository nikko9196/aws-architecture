# Part I.5.
### What is Change Data Capture (CDC)?
CDC is a process that tracks and captures changes made to data in a database, and then action can be taken using the changed data.

---

### What is CDC useful for?
For examples, CDC is useful for data warehousing, business intelligence, and data integration scenarios where maintaining an accurate and up-to-date/real-time copy of data is essential. Instead of replicating entire datasets each time, CDC allows systems to identify and transmit only the changed data, reducing the amount of data transferred and improving efficiency.

Reference: 
- https://rivery.io/blog/what-is-change-data-capture-cdc/#:~:text=Change%20data%20capture%20tracks%20changes,between%20databases%20in%20real%2Dtime.

---

### Which additional architecture patterns can CDC enable?
Some architecture patterns are:
- **Event-Driven Architecture:** CDC aligns well with event-driven architecture, where events are triggered by changes in data. This pattern enables the creation of loosely coupled, scalable systems where components react to specific data changes, leading to more responsive and efficient applications.
- **Microservices Architecture:** CDC can facilitate the transition from monolithic to microservices architecture by capturing and propagating changes in the data layer. This enables a more decoupled and modular approach, where each microservice can react to specific data changes without relying on a centralised database.

---

### Find AWS architecture references for the use of CDC
### Transactional Processing
**AWS Architecture Reference:** https://aws.amazon.com/blogs/apn/change-data-capture-from-on-premises-sql-server-to-amazon-redshift-target/
**An usecase of a hypothetical retailer with a customer loyalty program to demonstrate how Change Data Capture is used:**
![Change Data Capture - Customer Loyalty Programme](<Diagrams_and_Images/Change Data Capture - Customer Loyalty Programme.jpeg>)
Change Data Capture (CDC) is important in this scenario, systematically tracking and replicating incremental changes in customer loyalty data from the on-premises SQL Server database to AWS. It ensures efficiency by capturing only relevant changes and minimising data transfer and storage needs. The real-time synchronisation enabled by AWS Database Migration Service (DMS) keeps the AWS environment promptly updated. CDC, with additional columns like timestamp and operation indicators, safeguards data integrity during replication. In terms of transactional processing, CDC aligns with the Online Transaction Processing (OLTP) system, monitoring transaction logs for changes and maintaining transactional consistency across environments. This solution integrates new customer registrations, loyalty updates, and deletions, providing timely and accurate insights for analytical purposes.

#### Analytics Processing
**AWS Architecture Reference:** https://aws.amazon.com/blogs/big-data/stream-change-data-to-amazon-kinesis-data-streams-with-aws-dms/
**An usecase of an energy company to demonstrate how Change Data Capture is used:**
![Change Data Capture - Weekly Batch Job with Analytics](<Diagrams_and_Images/Change Data Capture - Weekly Batch Job with Analytics.png>)
In the energy company's scenario, the deployment of Change Data Capture (CDC) through AWS Database Migration Service (AWS DMS) plays a central role in achieving real-time analytics processing. CDC captures and streams changes from Amazon RDS, enabling the company to shift away from weekly batch jobs and gain immediate, precise insights into customer usage patterns and billing details. This ensures data consistency and synchronisation while significantly enhancing the company's analytics processing capabilities.
The integration of CDC with Amazon Kinesis Data Streams further streamlines real-time data flow, enabling AWS Lambda to respond to specific streams promptly. This responsiveness triggers timely emails and SMS notifications to customers, addressing concerns about potential slowdowns in the core transactional system due to massive data processing. Additionally, leveraging Kinesis Data Firehose to load transaction data into the Amazon S3 data lake supports immediate and accurate forecasting, effectively overcoming challenges associated with traditional batch analytics.

