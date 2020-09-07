#  Identity Management

## Article - Active Directory 360: Fundamentals of Active Directory, Workgroups and Domains
- The five srevices that runs on Windows Server
    - AD domain service (AD DS)
    - AD lightweight directory service
    - AD federation service(AD FS)
    - AD certificate service (AD CS)
    - AD Rights Management services (AD RMS)
- ADDS
    - store of information like telephone directory
    - AD is not a database, rather it is directory that points to database. 
    - When deploying AD, one should consider two things
        - Logical and physical
            - Logical side: this is the hierarchy of objects such as users, computer, groups and organizational units.
        - Physical side: admin has to think about servers that provide the AD service and contain all the critical information
-  Workgorup vs domains
    - A workgroup is a peer to peer network with no central authentication. When user wants to get a file from other computer, they need to create username and password on the other user's computer.
    - Workgroup is great in a way that small office with 15 or less computers. 
    - For bigger scale, client-server network environment is more preferred.
    ![Workgroup vs domain](./assets/workgroup.png)
- Domain service provides more flexibility in a way that when user or groups of users want to access another computer on the domain, they don't need to create another account on that computer
- All of the authentication and authorization is done by domain controller
    - Authentication: The client and server authenticate each other to verify who the user or system is.
    - Authorization: The server determines if the client has the required permissions to access a resource.
- Authentication is processed by Kerberos authentication protocols. Authorization is processed by Access Control Lists(ACLs). 
