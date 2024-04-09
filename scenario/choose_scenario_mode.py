import os  # Importez le module os pour utiliser les variables d'environnement
import subprocess
import inscription
import psycopg2

def main():
    print("Welcome to the deployment program!")
    print("Please choose the action:")
    print("1. Deploy Scenario 1")
    print("2. Deploy Scenario 2")
    print("3. Remove Docker containers")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        deploy("scenario1/scenario1_all_in_oneEC2")
    elif choice == "2":
        deploy("scenario2/scenario2_all_in_oneEC2")
    elif choice == "3":
        remove_docker_containers()
    elif choice == "4":
        print("Exit ...")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        return

def deploy(playbook_name):
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

    if mode == "aws":
        with open('../guacamole/ec2_adress.txt', 'r') as file:
            IP_EC2 = file.read().strip()
    else:
        IP_EC2 = "none"

    subprocess.run(["ansible-playbook", f"{playbook_name}.yml", "-e", f"mode={mode}", "-e", f"IP_EC2={IP_EC2}", "-e", "supp=false", "--ask-become-pass"])

    scenario = playbook_name.split("/")[0]

    if mode == "local":
        print("Test de connexion à la base de données réussi.")
        conn = psycopg2.connect(
            database="guacamole_db",
            host="127.0.0.1",
            user="guacamole_user",
            password="password",
            port="5432")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS scenarios (name VARCHAR(25) PRIMARY KEY, connections_id INTEGER[])")
        conn.commit()
        inscription.inscription_guacamole(conn, scenario)
    elif mode == "aws": 
        print("Test de connexion à la base de données réussi.")
        conn = psycopg2.connect(
            database="guacamole_db",
            host=IP_EC2,
            user="guacamole_user",
            password="password",
            port="5432")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS scenarios (name VARCHAR(25) PRIMARY KEY, connections_id INTEGER[])")
        conn.commit()
        inscription.inscription_guacamole(conn, scenario)


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

    subprocess.run(["ansible-playbook", "clean_docker.yml", "-e", f"mode={mode}", "-e", f"second_mode={second_mode}", "--ask-become-pass"])


if __name__ == "__main__":
    main()
