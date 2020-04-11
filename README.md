#eks-auth-py
This tool generates a kubernetes configuration file ready to access an eks cluster.

The user will be given the option to select existing or create new profile, before being asked for an MFA code.

Once the basic process is completed the user will need to move the new kubernetes config file to the default location (~/.kube/config).

##Assumptions

The use of script script assumes you have the following configured.

- an AWS IAM account with MFA enabled.
- a group for kubernetes users, configured with the following policy:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "eks:DescribeCluster",
      "Resource": "*"
    },
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": "iam:GetUser",
      "Resource": "arn:aws:iam::**ACCOUNT_NUMBER**:user/${aws:username}"
    },
    {
      "Sid": "VisualEditor2",
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::**ACCOUNT_NUMBER**:role/kubernetes-admin"
    }
  ]
}
```
- a role with the following policy applied:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sts:GetCallerIdentity",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": "true"
                }
            }
        }
    ]
}
```

The group policy config should look something like this:

 ```
    group:
        user  
        group-policy
    role:
        role-policy
```

##Configuration Requirements

- config.ini:

    general.REGION = the desired aws region the cluster resides in.
    
    cluster.NAME   = the name of the cluster, specified under the "Name" tag.
    
    cluster.ROLE   = the name of the role to be assumed as specified in the role arn.
    
- AWS_ACCESS_KEY_ID = the AWS access key you will be using to access the EKS cluster.

- AWS_SECRET_ACCESS_KEY = the secret AWS access key you will be using to access the EKS cluster.