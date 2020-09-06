# Windows Server

## Microsoft Active Directory®: The Ultimate AD FAQ – JumpCloud
- Active Directory (AD) is widely used on-prem directory service.
- On prem directory service platform
- Identity provider
- it serve as windows application 
- Group policy object (gpo)
- before IT was on-prem hence AD was widely used
- jump cloud allows wire or wireless 
    - allow cross platform
- Active directory is a service that enables admin to manage and secure IT resources
- Admin can us AD to manage user from using specific Windows laptops, servers and applications.
- Admin can also enforce security settings and software updates using AD.
- AD was released on 1999 alongside of Windows 2000 Server edition
- AD utilize DNS protocol and Lightweight Directory
- Primary user of AD are admins, where they use AD to manage, operate and configure AD.
- AD admins likely include all of the IT team and may also include numbers of the security, DevOps, or engineering teams.
- AD object is unit of information store within Active Directory's database
    - This can include user, laptops, servers, and even groups of other object
- objects and theses sets of group is called GPO (group policy objects)
- `forest` is top art of AD logical structure
- `forest` describes group of `trees`, that reflects # of domains.
- `domains` in this case is group of users, computers and devices that are part of same AD database.
- `trees` could be used to group all of the domains as brances belonging to the same trees. An organization that has multiple trees could then group them into a forest
- Domain controller: that server that is used to authenticate users and authorize users to use specific apps
- IT resources are app, system, file, network
- these resources are known as domain and domain controller allows only certain user to access this resources. Like a gate keeper
- `directory service database` = `identity provider`
- identity provider manage username and password
- when user enters through the portal to remote in they are required to sign in with authentication
    - when enter, it will run through domain control which then queries directory service database.
    - if the credential matches the db, then domain controller will authorize user to access the resources.
    - if fails, domain controllers will prevent the users.
- domain controllers was designed during the late 90's and was on-prem.
- Active Directory Domain services
    - ADDS is active directory + domain
    - ADDS federate all of the users throughout windows server
    - use active directory as manage the users
- Azure directory service
    - cloud based service
    - user authentication 
    - azure AD allows cloud platform authentication and authorization to use cloud services within the resource group.
    - single sign-on access
    - Not intended to be a solve or replacement of AD, rather it was designed to compliment the AD
- LDAP: directory houses critical info (auth info). This can be for various application.
- Single Sign on (SSO)
- Active directory is not a open source and is privately own by Microsoft.
- AD contains database
- When AD is installed on server, it becomes domain controller
- Backup is important to keep the saved settings.
- The estimated time for Windows server is five years.
- Some of the best practice for Active Directory are
    1. Change the default security settings: change default settings, since attacker has pretty good understanding of default settings
    2. Utilize principles of least privilege in AD roles and groups: giving least privileges, you reduce attackers surface from intruders
    3. Control administration privileges and limit accounts in the Domain Admins group 
    4. Don’t use a domain controller like it’s a computer: don't install software or applications on a domain controller
    5. Patch AD regularly
    6. Monitor nd audit Ad Health: 
    7. Define a naming convention at beginning thi will go a long way in keeping AD
    8. Clean up AD regularly
    9. Get domain ime right.  
- To secure the AD, patch, upto date and utilize principles of least privilege. 
- cost of AD can be calculated as 
    ```
    Costs of Active Directory =
    servers + software + hosting + backup + security + monitoring + VPNs
    + IT admin + third-party SW + multi-factor authentication + governance
    ```
- The advantage of using AD
    1. Greater admin control over Windows resources
    2. Improve efficiency for users and admins
    3. More secure Windows systems, networks, & data
    4. Reliable and thorough reporting for auditing & compliance
- The disadvantage of using AD
    1. Reduced functionality with Mac & Linux systems
    2. Difficult to configure and manage
    3. Requires on-premises hardware
    4. High upfront costs
    5. Limited connectivity to cloud apps & infrastructure
- With secure infrastructure, applying group-base management at scale is must have big organization
- Some of the alternative to Windows AD are OpenLDAP, G suite, Jump cloud.