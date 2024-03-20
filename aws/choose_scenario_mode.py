import subprocess

def main():
    print("Welcome to the deployment program!")
    print("Please choose the action:")
    print("1. Deploy")
    print("2. Remove Docker containers")
    print("3. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        deploy()
    elif choice == "2":
        remove_docker_containers()
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return

def deploy():
    print("Please choose the deployment mode:")
    print("1. Local")
    print("2. aws")
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
    subprocess.run(["ansible-playbook", "scenario1.yml", "-e", f"mode={mode}", "--ask-vault-pass"])

def remove_docker_containers():
    print("Removing Docker containers...")
    subprocess.run(["ansible-playbook", "clean_docker.yml"])

if __name__ == "__main__":
    main()
