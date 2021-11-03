# startupvpc

This solution uses the ![AWS CDK](https://aws.amazon.com/cdk/) to create a simple but effective ![Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/).  This solution handles the complexity of creating a multi-Availability Zone VPC with public and private subnets, route tables, NAT Gateways, and all of the other components required when building a VPC.

## Reference Architecture

![Reference Architecture for the VPC for Starups](/architecture/VPCforStartups.png)

## Details

The VPC for Startups spans 3 ![Availability Zones (AZ)](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) and contains a private and public subnet in each AZ.  The VPC contains 2 managed ![NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) that provide network translation service for all resources located in the private subnets.  The 2 NAT Gateways provide a balance of redundancy and cost.  The VPC also comes with a ![Gateway VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html) for the ![Amazon S3](https://aws.amazon.com/pm/serv-s3) service, which sends all traffic destined for Amazon S3 buckets over a private connection instead of the internet.  This enhances the security posture of the VPC and reduces the overall cost by removing S3 traffic from the internet egress.  Finally, ![VPC flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) are enabled and saved to an S3 bucket that is automatically created for you.  The VPC flow logs capture information about the IP traffic to and from the network interfaces within the VPC and are saved to S3 for analysis.

## Installation Instructions

This solution is build using the AWS CDK and Python.  Python AWS CDK applications require Python 3.6 or later.  The Python package installer, pip, and virtual environment manager, virtualenv, are also required. Windows installations of compatible Python versions include these tools. On Linux, pip and virtualenv may be provided as separate packages in your package manager. Alternatively, you may install them with the following commands: 
```
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install --upgrade virtualenv
```

Clone this solution to your workspace with the command
```
git clone https://github.com/conorcolgan/startupvpc
cd startupvpc
```
After cloning the solution, create and activate the project's virtual environment. This allows the project's dependencies to be installed locally in the project folder, instead of globally. 
```
virtualenv .venv
source .venv/bin/activate
```
After activating your virtual environment, install the dependencies:
```
python -m pip install -r requirements.txt
```
NOTE: Activate the project's virtual environment whenever you start working on it. Otherwise, you won't have access to the modules installed there, and modules you install will go in the Python global module directory (or will result in a permission error). 

Once you have installed the requirements you can run the command `cdk diff` to see a list of the resources that will be deployed.  The command `cdk deploy` is used to deploy the solution into an account where you are authenticated.

To learn more about the AWS CDK please see the ![AWS Cloud Development Kit (CDK) documentation](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
