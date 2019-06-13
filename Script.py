import boto3
session = boto3.Session(
    aws_access_key_id='AKIATFQLGRQPXBARJEES',
    aws_secret_access_key='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',
)

s3 = session.resource('s3')
outfile = open('nEw.pem', 'w')
key_pair = ec2.create_key_pair(KeyName='nEw')
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)


ec2 = boto3.resource('ec2', region_name = 'eu-west-1' )
instance = ec2.create_instances(
    ImageId = 'ami-007294ed)',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'nEw')#,
    #SubnetId = 'No preference (default subnet in any Availability Zone)')
print (instance[0].id)
		

securitygroup = instance.create_security_group(GroupName='Mygtoup1', Description='only allow SSH traffic', VpcId=vpc.id)
securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)
securitygroup = instance.create_security_group(GroupName='Mygtoup1', Description='HTTP allow SSH traffic', VpcId=vpc.id)
securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=80, ToPort=80)
