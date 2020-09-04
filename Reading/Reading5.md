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
- When user query domain name, pc doesn't browse off to find IP address, rather they look for it in domain cached. If you are able to find it, you are skipping a lot of steps
- These records are stored for short period of time. Whenever you create a record, you have the option to set a TTL.
- TTL is tile to live, which tell resolve name server how long they can store the record information
- TTL's can range anywhere from 30 seconds to a week

## Ubuntu Server

- Ubuntu server is open source platform
- It can be scaled up to enterprise level
- Ubuntu server can serve up websites, file shares, and containers as well as expand your company offering with an incredible cloud presence
- IF business is looking for quick and cost effective server solution, then Ubuntu is the way to go
- The minimum requirement for Ubuntu is:
    - 512 MB of RAMs
    - 1 GHz CPU
    - 1 GB disk space
- Ubuntu has become the first choice for administrator and DevOps engineers looking to deploy OpenStack
- Ubuntu will be leading IT to $1T mark
- The highest competitor for Ubuntu is Red Hat, Suse, centOS, Fedora Server, Windows Server

--- 

## Video

- Computer use number talk to each other
- Names are something that humans use to identify each other
- to bridge the gap DNS was developed
- DNS domain name system
- DNS is like a phone book
- Steps that DNS take
    1. Type yahoo to query to resolver server
    2. Resolver will query and if can't find it, it will send to root server
    3. operated by 13 set of company
    4. root server will direct to top level domain server
    5. TLD stores the address information for top level domains like com .net .org etc..
    6. TLD is not going to know IP address, so it will direct server to authorative name server 
    7. they will know the I.P address
    8. it will send it back to computer
    9. some of the DNS info will be saved to ISP server