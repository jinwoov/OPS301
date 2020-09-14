# Azure Cloud Administration

## What Is Microsoft Azure, Anyway?

- Azure is cloud computing service that provides similar service to Amazon web services or Google Cloud Platform
- Traditionally business would have to host their own server using its own hardware
- Enterprise will had to pay someone to keep their connection solid.
- When you need more computing powers,you can just purchase it off from the site instead of looking for new piece of hardwar
- YOu can host whatever you need on the cloud
- Originally, it was called `Windows Azure`, but they transitioned to `Microsoft Azure`.
- Azure offers Active Directory which is hosted on Azure and it allows organization to have all those centralized administration features without requiring them to host their own AD.

---

## Identity management

- Identity management is the process of authenticating and authorization security principals.
- Support single enterprise directory
- Enforce and measure key security attributes when authenticating all users
- uses password and multi factor authentication.
- Single resource can change all the settings in one place
- SSO is another benefit
- By signing in just once using single user account, you can grant access to all the application and resources as per the business needed.
- `Role-based access control` (RBAC): 
    - allow one user to manage virtual machines in subscriptions
    - allow a DBA group to manage SQL database
    - Allow a user to manage all resources in a resouce group
    - Allow an application to access all resources in a resource group
- Azure AD encourage admin to not to host non-employee accounts in corporate directory
- Use modern password protection
- Disable legacy authentication methods