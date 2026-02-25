import boto3
import time
import json

s3 = boto3.client("s3")
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    # Création d’un bucket S3 (nom unique)
    bucket_name = f"poec-bucket-{int(time.time())}"
    s3.create_bucket(Bucket=bucket_name)

    # Lancement d’une instance EC2 t2.micro
    ami_id = "AMI_ID_A_REMPLACER"  # AMI Amazon Linux de ta région
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1
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
