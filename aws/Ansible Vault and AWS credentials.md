For use AWS credentials in Ansible Vault, you need to create a vault and add a file with the following content:

1. Create a vault
```shell
ansible-vault create group_vars/all/vault.yml
```
2. Fill the password