import os  # Importez le module os pour utiliser les variables d'environnement
import subprocess
#import inscription
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

    with open('../guacamole/ec2_adress.txt', 'r') as file:
        IP_EC2 = file.read().strip()

    subprocess.run(["ansible-playbook", f"{playbook_name}.yml", "-e", f"mode={mode}", "-e", f"IP_EC2={IP_EC2}", "--ask-vault-pass"])

    if mode == "local":
        print("Test de connexion à la base de données réussi.")
        conn = psycopg2.connect(
            database="guacamole_db",
            host="127.0.0.1",
            user="guacamole_user",
            password="password",
            port="5432")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS scenarios (id INTEGER PRIMARY KEY, name VARCHAR(25))")
        conn.commit()
        inscription.inscription_guacamole(conn)
    elif mode == "aws": 
        print("Test de connexion à la base de données réussi.")
        conn = psycopg2.connect(
            database="guacamole_db",
            host=IP_EC2,
            user="guacamole_user",
            password="password",
            port="5432")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS scenarios (id INTEGER PRIMARY KEY, name VARCHAR(25))")
        conn.commit()
        inscription.inscription_guacamole(conn)

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


# Fonction d'inscription à Guacamole
def inscription_guacamole(conn):
    cur = conn.cursor()
    # Insertions pour Kali sshd
    cur.execute("INSERT INTO guacamole_connection (connection_id, connection_name, protocol) VALUES ('1', 'KALI', 'ssh')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('1', 'hostname', '10.1.1.4')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('1', 'password', 'password')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('1', 'username', 'labuser')")
    # Insertions pour Alpine sshd
    cur.execute("INSERT INTO guacamole_connection (connection_id, connection_name, protocol) VALUES ('2', 'ALPINE', 'ssh')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('2', 'hostname', '10.1.1.2')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('2', 'password', 'password')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('2', 'username', 'labuser')")
    # Insertions pour FTP Alpine sshd
    cur.execute("INSERT INTO guacamole_connection (connection_id, connection_name, protocol) VALUES ('3', 'FTP', 'ssh')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('3', 'hostname', '10.1.1.3')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('3', 'password', 'password')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('3', 'username', 'labuser')")
    conn.commit()

# Fonction de suppression dans Guacamole
def suppression_guacamole(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM guacamole_connection_parameter WHERE connection_id = '1'")
    cur.execute("DELETE FROM guacamole_connection WHERE connection_id = '1'")
    cur.execute("DELETE FROM guacamole_connection_parameter WHERE connection_id = '2'")
    cur.execute("DELETE FROM guacamole_connection WHERE connection_id = '2'")
    cur.execute("DELETE FROM guacamole_connection_parameter WHERE connection_id = '3'")
    cur.execute("DELETE FROM guacamole_connection WHERE connection_id = '3'")
    conn.commit()









if __name__ == "__main__":
    main()
