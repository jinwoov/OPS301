# Networking

## What is a Computer network
- Network is between two or more computers that are connected via wired(cables) or wireless(WiFi). The purpose of this connection are transmitting, exchanging, or sharing data and resources.
- The geographic location defines what computer network as a LAN(local area network) connects computers in a defined physical space, like an office building. For WAN (wide area network) can connect computers across continents. 

## Computer Network Types
- LAN: Local area network. Connects computer over short distance, allowing computers to exchange files, data, and resources. The most common use of LAN is office building, school, or hospital. 
- WLAN: Wireless local ara network. Just like LAN but with wireless connection.
- WAN: Wide area network. Connects computer over a wide area. Connecting billions of computer world wide. 
- MAN: Metropolitan area network. Larger than LANs but smaller than WANs. Cities and government entities typically manages MANs.
- PAN: Personal area network. Serves one person. Across two different device that user use. Like airdrop.
- SAN: Storage area network. Block-level storage. 
- CAN: Campus area network. Corporate area network. Larger than LAN but smaller than WAN. Usually serves college, universities, business campuses.
- VPN: Virtual private network. Secure, point-to-point connection between two network end points.

## Important terms and concepts
- IP address: unique identifier assigned to every device connected to network that uses the Internet Protocol for communication. 
- Nodes: connection point inside a network that can receive, send, create, or store data.  
- Routers: physical or virtual device that sends information contained in data packets between networks. Router forwards these data packets until it reaches its destination.
- Switch is a device that connects other devices and manages node to node communication within network. 
    - circuit switching: establishes dedicated communication path between nodes in a network. Preventing other traffic can ravel along that path
    - packet switching: breaking down data into independent component called packets. 
    - Message switching: sends message in its entirety from the source node. 
- Ports: Ports are suite or room numbers if IP address is hotel.
- Network cable types: most common network cable types are Ethernet twisted pair, coaxial and fiber optic. The choice of cable will be depending on the network setting.

## Computer networks and the internet
- Internet connection are created using protocol. Those protocols include hypertext transfer protocol (http). 
- Internet service providers (ISPs) and network service providers (NSPs) provides the ground that allows the transmission of packets of data or information over the internet. 

## How does it work?
- Computer connects nodes (computers, routers, and switches) using cables, fiber optics or wireless signals. These connections allows network to communicate with each other.
- Network follows protocols that defines how communication are sent and received. 
- Each device are assigned with unique identifier, IP. 

## Architecture

### Main types of network architecture
- P2P, peer-to-peer and client/server.
- In P2P, two or more computers connects are a peers, meaning they have equal power and privileges on the network. 
- P2P doesn't need central server
- In a client/server network, client access and communicate through the server. In client/server architecture, they don't share resources.
- Client/server is sometimes called tiered model because it's designed with multiple levels or tiers.

### Network Topology
- refers how the nodes and links in network are arranged
    - Bus network topology: when network node is connected directly using main cable.
    - Ring topology: nodes are connected in a loop. Each device has exactly two neighbors. Connected indirectly through multiple nodes.
    - Star network: all nodes are connected to a single, central hub and each node is indirectly connected through that hub.
    - Mesh topology: Overlapping connection between nodes.

## Security
- The defense mechanism can be firewall
- Process of authentication adds another layer of security.
- The use of public cloud also requires updates to security procedures to ensure continued safety and access. A secure cloud demands a secure underlying network. 

## Mesh networks
- Mesh networks self-configure and self-organize, searching for the fastest, most reliable path on which to send information.

### Types of mesh networks
- full mesh technology: every network is connected to each other. It costs more to execute, hence partial mesh topology is used more often
- wireless mesh network: connected through wireless network

## Load Balancers and networks
- efficiently distribute tasks workloads and network traffic across available servers.
- Load balancer is like air traffic control, watches which flight is coming in and directs it toward the router or server best equipped to manage it.
- it is to avoid resource overload and optimize available resources.

## Content delivery networks
- CDN is server network that delivers temporarily stored. CDN stores this content in distributed location and serves it to users as way to reduce the distance between your website visitors. Having the cache data to the end user allows you to serve content faster and helps websites better each a global audience.

---
## **Video**

- Topology is a layout of how a network communicates with different devices.
- wired and wireless
    - Star topology
        - all computers are connected to a hub (one central point)
            - one computer fail, then other computers will not fial
            - if the central point fails, all of the computer fails.
            - **single point of failure**
    - ring topology
        - each computer is connected together and forms a ring
        - each data packet is going around 
        - it is very old
        - advantage is that it is easy to install and execute
        - if one computer goes down or single distorment of cable occurs all of the system fails.
    - bus topology
        - old topology
        - each of the computer and network devices are connected to backbone. 
        - BNC, T connector
        - cheap and easy to implement
        - it requires both end to have terminator
        - there must be no loose end
        - if terminator is disconnected in one end, it bounce back the data packet.
            - this event is called signal reflection
            - data flow is disrupted
    - mesh topology each computer is connected to all of the devices
        - advantage is high redundancy
        - computer will still be able to work
        - can be expensive
        - rarely used for local
        - internet is example of this occurrence
- Wireless topology 
    - wire end and wireless 
    - wireless access point acts as bridge
    - adhoc: simple topology
        - doesn't require wire, cable, router
        - p2p network
        - directly connected to each other
        - each devices are required to setup of security
    - wireless mesh, devices are interconnected to each other. each wireless point will talk to each other
        - very redundant

---

## Network Design and Best Practices
- Network Architecture
    - Building blocks mindset
    - Scalable and modular
    - ISP (pipe) -> Gateway(router) -> core -> access -> devices 
    - how traffic flows
    - 