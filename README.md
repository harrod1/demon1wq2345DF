#### THIS IS LOCALLY CREATED GIT PROJECT
modified from 'dev branch'
####################################################################

import boto3
# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name=REGION)


try:
    response = ec2_client.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        MinCount=1,
        MaxCount=1,
        KeyName=KEY_PAIR_NAME,
        SecurityGroupIds=[SECURITY_GROUP_ID],
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
    print(f"Successfully launched EC2 instance with ID: {instance_id}")

except Exception as e:
    print(f"Error launching EC2 instance: {e}")
