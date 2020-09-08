# Linux Web Server

## Barracuda: What is a DMZ Network?

- DMZ (demilitarized zone) works a subnetwork containing an organization's exposed, outward-facing services.
- it act as a point where untrusted network meet
- When DMZ is configured correctly, it gives extra security to the organization.
- Host in the DMZ controls permission to other service within the internal network.
- All of the network that communicate with user should be placed in the DMZ. One of the most common services are
    1. Web Servers: Responsible for maintaining communication with an internal database.
    2. Mail Servers: The authentication and the meessages are often stored on servers without direct access to the internet. Therefore email server will be build directly in DMZ in order to interact with and access the email database
    3. FTP servers: FTP should always partially isolated from critical internal systems.
- DMZ designs
    - there are many methods to prepare DMZ but notable DMZ configs are two which is single firewall or dual firewall
        1. Single firewall: Single firewall is modest approach with minimum of 3 network interface. 
            - Extenal netowkr device -> DMZ (third party)
        2. Dual firewall: The more secure approach
            - The first firewall is frontend firewall. Responsible for traffic destined for the DMZ
            - Second firewall is backend firewall. Responsible for traffic that travels from the DMZ to the internal network
- The router serve as both connection point and firewall for SOHO. Hence, DMZ can built by adding a dedicated firewall
- DMZ are an essential part of network security

---

## DMZ Network
- DMZ acts as a exposed point to an untrusted network, commonly call internet.