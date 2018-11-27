
* https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html

```sh
aws ec2 run-instances --image-id ami-1a2b3c4d --count 1 --instance-type c3.large --key-name MyKeyPair --security-groups MySecurityGroup


aws ec2 run-instances --image-id ami-abc12345 --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-1a2b3c4d --subnet-id subnet-6e7f829e


aws ec2 run-instances --image-id ami-005bb0af4ade8c765 --count 1 --instance-type t2.micro --key-name MyKeyPair --security-groups sg-112ad66b --subnet-id subnet-75c3db3c --associate-public-ip-address
```