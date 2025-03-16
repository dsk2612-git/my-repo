import boto3
client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-0ddfba243cbee3768',
    InstanceType="t2.micro",
    KeyName ="demo",
    MaxCount=1,
    MinCount=1
)

