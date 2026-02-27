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
    
    ###################################################################################

    import boto3
import time
import json

s3 = boto3.client("s3")
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    # Création d’un bucket S3 (nom unique)
    bucket_name = f"poec-bucket-{int(time.time())}"
    try:
        s3.create_bucket(Bucket=bucket_name)
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    # Lancement d’une instance EC2 t2.micro
    ami_id = "ami-0b6c6ebed2801a5cb"  # AMI Amazon Linux de ta région
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                                'Key': 'Name',
                                'Value': 'Boto3Instance'
                        },
                    ]
                },
            ]
            )

    instance_id = response["Instances"][0]["InstanceId"]

    # Réponse de la Lambda
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Ressources créées avec succès",
            "bucket": bucket_name,
            "instance_id": instance_id
        })
    }
  
