import os
from aws_cdk import (
    core as cdk, 
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3
)

class VpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        REGION = cdk.Environment(region=os.environ["CDK_DEFAULT_REGION"])

        # Setup IAM user for logs
        vpc_flow_role = iam.Role(
            self, 'FlowLog',
            assumed_by=iam.ServicePrincipal('vpc-flow-logs.amazonaws.com')
        )

        ## S3 Bucket for VPC Flow Logs
        bucket = s3.Bucket(self, "VPCFlowLogs",
            block_public_access = s3.BlockPublicAccess.BLOCK_ALL,
            encryption = s3.BucketEncryption.KMS_MANAGED,
            enforce_ssl = True
        )
        
        ## Create VPC
        vpc = ec2.Vpc(self, "StartupVPC", 
            max_azs=3,
            cidr="10.0.0.0/19",
            nat_gateways=2,
            gateway_endpoints={
                "S3Endpoint": ec2.GatewayVpcEndpointOptions(
                    service=ec2.GatewayVpcEndpointAwsService('s3')
                    )
            },
            flow_logs={
                "StartupVPCFlowLogs": ec2.FlowLogOptions(
                    destination=ec2.FlowLogDestination.to_s3(bucket=bucket, key_prefix="VPCFlowLogs/")
                )
            }
        )
 