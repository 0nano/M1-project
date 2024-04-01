import argparse
import subprocess
import os

def ftp_local():
    print("Running local FTP")

def ftp_aws():
    print("Running AWS FTP")
    # Vérifier si une instance AWS FTP existe
    print("Checking if an aws instance already exists FTP")
    # Execute the Ansible playbook with the --vault-password-file option
    subprocess.run(["ansible-playbook", "scenario1_ftp.yml", "-e", "mode=-ftp", "--ask-vault-pass"])
    # Si elle existe, exécuter le scénario pour l'instance AWS FTP


def ssh_local():
    print("Running local SSH")

def ssh_aws():
    print("Running AWS SSH")
    # Vérifier si une instance AWS SSH existe
    # Si elle existe, exécuter le scénario pour l'instance AWS SSH
    # Sinon, appeler scenario2

def main():
    print("Hello and welcome in the Scenario 1")
    print("If you haven't deploy the environment first please run the choose_scenario_mode.py as administrator first")
    print("If you have already done it now you can interact with the scenario")
    print("")
    parser = argparse.ArgumentParser(description="Script to run different sections.")
    parser.add_argument("section", choices=["ftp", "ssh"], help="Section to run")
    parser.add_argument("--type", choices=["local", "aws"], help="Type of section to run (local or aws)")
    args = parser.parse_args()

    if args.section == "ftp":
        if args.type == "local":
            ftp_local()
        elif args.type == "aws":
            ftp_aws()
    elif args.section == "ssh":
        if args.type == "local":
            ssh_local()
        elif args.type == "aws":
            ssh_aws()

if __name__ == "__main__":
    main()



