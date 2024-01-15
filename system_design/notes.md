Questions:
Schema of database
SQL vs NoSQL
How are we handling scale?
Do we need to handle scale with the database? (sometimes a normal, single instance db is enough)


After we receive our prompt, this is the flow
1. Narrow down requirements
   - What functionality are we focusing on?
   - Define the scope by using the interviewer and asking them requirements
   - Functional vs Nonfunctional
     - Functional = features
     - Nonfunctional = 
       - scalability (throughput, storage capacity)
       - performance (latency, how heavy reads/writes)
       - availability
   - Calculations
     - 86400 seconds in a day => aprox to 100k seconds
       - ex. 
       - 100M daily active users, 100r per day, onlu 10% of users make a tweet daily => 10M tweets a day, 10b reads per day
       - Throughput = 10b reads/100k seconds = 100k reads per second
2. High level design
3. Scaling
4. Db Schema

RateLimiter Example
NFR
Latency, Throughput, Storage, # of users, 
IP address = 4 bytes, for each user to store # of requests they've made = 128 bytes
1b users x 132 bytes = 132 Gb (remember 1b = 1Gb), therefore we can store 132 gb into memory
We want high availability
Fail-open => system behaves as if Rate limiter never existed, so all functionality would exist, but a small subset of users could spam while the Rate Limiter is down
Fail-closed => system shuts down, report error back to user, no functionality at all. this is bad for this scenario