Functional requiremnets
Continue to refine requirements, what are we designing, what is within scope
    Type of content
NFR do napkin math.These will inform us where our bottlenecks could be
    How many daily active users?
    How many read/write transactions per day, month, year 
    How much storage do we need for all the data
    You can use this to also guide your schema
High level design
    List out what architecture patterns
    Servers (web server vs app server ie front end vs backend)
    Services and connecting databases


SQL (want most accurate and up-to-date data)
1. Structured data with complex queries
2. ACID transactions (banks, inventory managament)
3. Fixed Schema
4. Data relations

NoSQL 
1. Unstructured 
2. Scalability & flexibility via read replicas and sharding
3. Specialized data models 
   - Document: Metadata (like Spotify song details).
   - Key-Value: Session Storage.
   - Wide-Column: IoT Analytics.
   - Graph: Social Networks, Recommendation Systems.

Caching
- For eviction policies, MRU, LRU, LFU

Assumptions
Char - 2 Bytes
Int - 4 Bytes
Float (Timestamps) - 8 Bytes
image - 100 KB