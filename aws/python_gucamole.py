from time import sleep
import subprocess
import os

try:
    import psycopg2
except ImportError:
    print("Le module psycopg2 n'est pas installé. Installation en cours...")
    os.system('pip install psycopg2')
    import psycopg2

try:
    import ansible_runner
except ImportError:
    print("Le module ansible_runner n'est pas installé. Installation en cours...")
    os.system('pip install ansible-runner')
    import ansible_runner

os.environ['ANSIBLE_BECOME_PASS'] = 'isen'


def test_db_connection() -> bool:
    try:
        conn = psycopg2.connect(
            database="guacamole_db",
            host="127.0.0.1",
            user="guacamole_user",
            password="password",
            port="5432")
        return True
    except Exception as e:
        print(e)
        return False


def main():
    # Récupération de la racine du projet
    tree = os.path.dirname(os.path.abspath(__file__))
    print("Voulez vous lancer Guacamole en local ou via AWS ?")
    # print("1. Lancer Guacamole en local")
    # print("2. Lancer Guacamole via AWS")

    # choice = input("Votre choix: ")

    # if choice == "1":
    #     mode = "local"
    # elif choice == "2":
    #     mode = "aws"
    
    print("Lancement Guacamole...")

    # Execution du script ansible pour la configuration des serveurs en affichant les logs
    # subprocess.run(["ansible-playbook", "guacamole.yml", "-e", f"mode={mode}", "--ask-vault-pass"])
    
    subprocess.run(["ansible-playbook", "guacamole.yml", "--ask-vault-pass"])

    sleep(5)

    print("Guacamole a terminé son exécution.")
    print("Test de connexion à la base de données...")

    if test_db_connection():
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
    else:
        print("Test de connexion à la base de données échoué.")
        exit(1)

    print('Affichage des scénarios...')
    print('Scénario 1: Serveur FTP')

    scenario = input('Entrez le numéro du scénario: ')

    if scenario == '1':
        cur.execute("INSERT INTO scenarios (id, name) VALUES (1, 'Serveur FTP')")
        conn.commit()
        print('Configuration du serveur FTP...')
        ftp_locate = tree + '/ftp.yml'
        r = ansible_runner.run(private_data_dir=tree, playbook=ftp_locate, verbosity=4)
        print('Configuration du serveur FTP terminée.')


if __name__ == "__main__":
    main()
    #input("Appuyez sur Entrée pour quitter...")
