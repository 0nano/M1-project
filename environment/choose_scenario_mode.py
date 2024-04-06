import subprocess

def main():
    print("Welcome to the deployment program!")
    print("Please choose the action:")
    print("1. Deploy Scenario 1")
    print("2. Deploy Scenario 2")
    print("3. Remove Docker containers")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        deploy()
    elif choice == "2":
        print("Scenario 2 is not available yet")
    elif choice == "3":
        remove_docker_containers()
    elif choice == "4":
        print("Exit ...")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        return

def deploy():
    print("Please choose the deployment mode:")
    print("1. Local")
    print("2. AWS")
    mode_choice = input("Your choice: ")

    if mode_choice == "1":
        mode = "local"
    elif mode_choice == "2":
        mode = "aws"
    else:
        print("Invalid choice. Please choose 1 or 2.")
        return

    print(f"Deployment in {mode} mode in progress...")

    # Execute the Ansible playbook with the --vault-password-file option
    subprocess.run(["ansible-playbook", "scenario1_all_in_oneEC2.yml", "-e", f"mode={mode}", "--ask-vault-pass"])

def remove_docker_containers():
    print("Removing Docker containers...")
    print("Please choose the cleaning mode:")
    print("1. Local")
    print("2. AWS")
    mode_choice = input("Your choice: ")

    if mode_choice == "1":
        mode = "local"
    elif mode_choice == "2":
        mode = "aws"
        print("Would you like to clean all the docker or delete the EC2 instance ?")
        print("1. Docker")
        print("2. EC2")
        second_choice = input("Your choice: ")
        if second_choice == "1":
            second_mode = "docker"
        elif second_choice == "2":
            second_mode = "ec2"
        else:
            print("Invalid choice. Please choose 1 or 2.")
            return
    else:
        print("Invalid choice. Please choose 1 or 2.")
        return

    print(f"Cleaning in {mode} mode in progress...")

    subprocess.run(["ansible-playbook", "clean_docker.yml", "-e", f"mode={mode}", "-e", f"second_mode={second_mode}", "--ask-vault-pass"])

if __name__ == "__main__":
    main()
