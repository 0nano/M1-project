## How to use a credential file
You have two methods to use a credential file. The first one is to use the default credential file, which is located in the following path:
```bash
~/.aws/credentials
```
or you can use a custom credential file, which is located in an another path to do that you need to set the environment variable `AWS_SHARED_CREDENTIALS_FILE` to the path of the custom credential file. For example:
```bash
export AWS_SHARED_CREDENTIALS_FILE=/Your/path/to/M1-project/credentials
```

## How to create a credential file
To create a credential file you need to create a file with the following format:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
aws_session_token = YOUR_SESSION_TOKEN
```
The `aws_session_token` is optional, you can use it if you have a session token.