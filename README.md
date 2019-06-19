# boto3auth

boto3auth is a simple (Python 3) wrapper for starting clients/resources with Boto3.

## Installation

_Requires boto3._

```bash
pip install boto3auth
```

## Usage

```python
import boto3auth

b3a = boto3auth.Boto3Auth(region, account_id, role, sts)
```

Properties:
  - `region`: AWS region (e.g. `us-east-1`, `ca-central-1`, etc.)
    - Defaults to `us-east-1`, if not set.
  - `account_id`: AWS account number (if assuming role)
  - `role`: AWS IAM role (if assuming role)
  - `sts`: Boto3 STS credentials (if assuming a secondary role)

### Auth

```python
b3a.auth(resource, type)
```

Arguments:
  - `resource`: AWS resource (e.g. `ec2`, `dynamodb`, `sqs`, etc.)
  - `type`: Boto3 Session type (`resource` or `client`)

_boto3auth will use local AWS credentials (works well with [aws-vault])._

```python
import boto3auth

# EC2 resource in us-east-1, with local credentials.
b3a = boto3auth.Boto3Auth()
resource = b3a.auth('ec2')

# DynamoDB resource in us-west-2, with assumed role.
b3a = boto3auth.Boto3Auth('us-west-2', '123412341234', 'my-cool-role')
resource = b3a.auth('dynamodb', 'resource')

# EC2 client in ca-central-1 that requires two assumed roles.
# e.g. Local -> Account #1 -> Account #2
first = boto3auth.Boto3Auth('ca-central-1', '123412341234', 'first-role')
first.creds() # creds() runs sts.AssumeRole and sets result to self.sts.

second = boto3auth.Boto3Auth('ca-central-1', '456745674567', 'second-role', first.sts)
client = second.auth('ec2', 'client')
```

[aws-vault]: https://github.com/99designs/aws-vault
