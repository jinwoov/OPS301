# Linux DNS Server

- without DNS, everything will fail
- Human readable form of string from IP address. 
- All of the Ip address has period at the end.
- . is end of the namespace
- Browser ask os system and ask resolving name server to look up ip protocol.
- resolving name server only know where to find the root
- The root server refers to top of the domain server.
- TLD server refers to authoritative name server. 
- Authoritative name server gives the ip to the cache and it will go back to interent to access the website.
- 30 years ago, every one had to know IP address to access website.
- Where is the information of Ip address to DNS stays? it is stored in nameservers
- Instead of storing every domains, they store the locations of the TLD
- TLD are like .com that ends in the domain name
- When user query domain name, pc doesn't browse off to find IP address, rather they look for it in domain cached. If you are able to find it, you are skipping alot of steps
- These records are stored for short period of time. Whenever you create a record, you have the option to set a TTL.
- TTL is tile to live, which tell resolve name server how long they can store the record information
- TTL's can range anywhere from 30 seconds to a week
- 