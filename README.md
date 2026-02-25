#### THIS IS LOCALLY CREATED GIT PROJECT
modified from 'dev branch'
####################################################################

import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name="us-east-1")
    response = ec2_client.run_instances(
    ImageId="ami-0b6c6ebed2801a5cb",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="met_demo",
    SecurityGroupIds=["sg-03c84be8b4c4a718c"],
    TagSpecifications=[
        {
                'ResourceType': 'instance',
                'Tags': [
                    {
                            'Key': 'Name',
                            'Value': 'MyBoto3Instance'
                    },
                ]
            },
        ]
        )
    instance_id = response['Instances'][0]['InstanceId']
    return "Successfully launched EC2 instance"
