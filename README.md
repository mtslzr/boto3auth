# boto3auth

boto3auth is a simple (Python 3) wrapper for starting clients/resources with Boto3.

## Installation

_Requires boto3._

```bash
pip install boto3auth
```

## Usage

Required:
  - `resource`: Chosen AWS resource (e.g. `ec2`, `dynamodb`, `sqs`, etc.)
  - `type`: Chosen Boto3 Session (`resource` or `client`)
Optional:
  - `region`: Chosen AWS region (e.g. `us-east-1`, `ca-central-1`, etc.)
  - `account_id`: Chosen AWS account, if assuming role
  - `role`: Chosen IAM role, if assuming role

_boto3auth assumes you have local AWS credentials configured (or are using a system like [aws-vault])._

```python
import boto3auth

# EC2 resource with local credentials
resource = boto3auth.auth('ec2')

# DynamoDB resource with assumed role
resource - boto3auth.auth('dynamodb', 'resource', 'us-east-1', '123412341234', 'my-cool-role')

# EC2 client in ca-central-1
client = boto3auth.auth('ec2', 'client', 'ca-central-1')
```

[aws-vault]: https://github.com/99designs/aws-vault
