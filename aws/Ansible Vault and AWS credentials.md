## Ansible Vault and AWS credentials
For use AWS credentials in Ansible Vault, you need to create a vault and add a file with the following content:

1. Create a vault
```shell
ansible-vault create group_vars/all/vault.yml
```
2. Fill the password
3. Edit the pass.yml to add the credentials for AWS
```yaml
ec2_access_key: AAAAAAAAAAAAAABBBBBBBBBBBB       
ec2_secret_key: afjdfadgf$fgajk5ragesfjgjsfdbtirhf
```
4. Quit and save the file

Now you can use the credentials in your playbook with the following syntax:
```yaml
aws_access_key: "{{ec2_access_key}}"
aws_secret_key: "{{ec2_secret_key}}"
```

**Warning** : The password for the vault will be prompt every time you run the playbook. To avoid this, you can create a file with the password and use it with the following syntax:
```shell
# 1. Create a hashed password file vault.pass
openssl rand -base64 2048 > vault.pass

# 2. Create an ansible vault with 'vault.pass' is referenced with '--vault-password-file' option to avoid prompt for password
ansible-vault create group_vars/all/pass.yml --vault-password-file vault.pass
```
With this method, you have to add the option '--vault-password-file' every time you run the playbook or editing the vault.