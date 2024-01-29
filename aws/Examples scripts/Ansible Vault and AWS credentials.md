## Ansible Vault and AWS credentials
For use AWS credentials in Ansible Vault, you need to create a vault and add a file with the following content:

1. Create a vault
```shell
ansible-vault create group_vars/all/vault.yml
```
2. Fill the password
3. Edit the pass.yml to add the credentials for AWS
```yaml
aws_access_key: AAAAAAAAAAAAAABBBBBBBBBBBB       
aws_secret_key: afjdfadgf$fgajk5ragesfjgjsfdbtirhf
```
4. Quit and save the file

Now you can use the credentials in your playbook with the following syntax:
```yaml
aws_access_key: "{{aws_access_key}}"
aws_secret_key: "{{aws_secret_key}}"
```

**<span style="color:FE7A36">Warning</span>** : The password for the vault will be prompt every time you run the playbook. To avoid this, you can create a file with the password and use it with the following syntax:
```shell
# 1. Create a hashed password file vault.pass
openssl rand -base64 2048 > vault.pass

# 2. Create an ansible vault with 'vault.pass' is referenced with '--vault-password-file' option to avoid prompt for password
ansible-vault create group_vars/all/pass.yml --vault-password-file vault.pass
```
With this method, you have to add the option '--vault-password-file' every time you run the playbook or editing the vault.

## How to get the AWS credentials
1. Go to the AWS console
2. Click on Services then on Security and Identity & Compliance
3. Click on IAM
4. Go on Users in the left menu and click on an user or create a new one
5. Click on the tab Security credentials
6. Click on Create access key then select CLI
7. Continue and create the key and copy the Access key ID and the Secret access key to the vault.

### **<span style="color:FE7A36">Warning</span>** :
If you create a temporary credential, you have to use the session token in the vault too. The session token is valid for 12 hours.
```yaml
aws_access_key: AAAAAAAAAAAAAABBBBBBBBBBBB       
aws_secret_key: afjdfadgf$fgajk5ragesfjgjsfdbtirhf
aws_session_token: <Your-session-token>
```