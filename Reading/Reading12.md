# DevOps

## What is DevOps? A Basic Introduction

- Dev ops primary goal to achieve continuous integration to continuous delivery
- `Development and operation` is what Dev-Ops stands for.
- DevOps puts information technology and specifically software and website development
- Continuous Integration
    - multiple of pieces of source doe and development elements come togeter and create a finished software product. Each piece is usually designed by a specific person or team as part of a sprint.
- Continuous Delivery
    - It's a process of how software is tested to allow for constant delivery of features
- Continuous testing is needed to validate against requirement, ensuring all of the requirement of the sprint the been met.
- Continuous Monitoring is monitors any bugs, security and compliance
- Dev ops are important as more businesses are realizing that the linear waterfall processes weren't working as well as they should be. 
- With continuous processes, developers are able to sed up development times as you can roll out new features to customers often.
- With the roles and responsibilities in Dev-Ops
    DevOps or platform engineer, build engineer, Reliability engineer, release manager, data analyst, and product manager
- The motto of Dev-Ops are transparency, trust, collaboration and communication to increase productivity and customer satisfaction.

---

## An Introduction to Infrastructure as Code
- To maintain and optimize performance, many businesses are increasing to meet demand. 
- Automation in cloud and infrastructure can increase the delivery value and reliability
- You can write code to manage your servers, databasees, network and apply changes to your infrastructure as needed.
- The benefit of having IaC is that you can automate the manual provisioning that you would do otherwise
- Idempotence: can apply multiple time without changing the result beyond the initial application
- Tools like Ansible and Terraform have built-in features to make your code idempotent.
- It reduce cost, faster software delivery, self documenting, version controlled, validation and testing, and improved security.
- The configuration management tools are designed to manage users, install and manage software and tools on existing server.
    - Cef, puppet, ansible and saltstack are imarily configuration tools
- Provisioning tools
    - Terraform, cloudformation, openstack heat. It is used to create servers, database servers and load balancers, queues, subnets, firewall and other components of your infrastructure.
- Mutable infrastructure is one that can be modified after it has been provisioned. 
- Tools like Terraform and CloudFormation are designed to create a new server from a machine image or a container image every time.
- Imperative vs declarative tools
    - you list steps to be taken to arrive at the desired state.
    - chef is primarily an imperative tool, ansible uses a hybrid approach and support both imperative and declarative techniques.
    - Declare tools are category where you declare the desired end tate
- Terraform to build VPCs subnet, Internet gateways, load balancers and VMs, then use Ansible to configure and deploy service on these instances.