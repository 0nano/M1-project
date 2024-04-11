import os
import sys
import subprocess
from time import sleep
import inscription
import psycopg2
import yaml

def main():
    args = sys.argv[1:]

    if len(args) == 0 or args.__contains__("-h") or args.__contains__("--help"):
        print("Deploy program")
        if len(args) == 0:
            print("----------------------------")
            print("No parameter specified")
            print("----------------------------")
        print("Usage:")
        print("python3 scenario.py [scenario_id] [mode] [option]")
        print("")
        print("MODE")
        print("-d, --deploy : Deploy the scenario")
        print("-r, --remove : Remove the scenario")
        print("")
        print("OPTION")
        print("-a, --aws : AWS deployment")
        print("-gs, --guacamole-start : Start guacamole service if not started depending on the deployment local or aws")
        print("-gr, --guacamole-remove : Remove guacamole service if started depending on the deployment local or aws")
        print("-h, --help : Display help")
        print("-l, --local : Local deployment if no mode specified, it will be local by default") 
        print("-s, --scenarios : Display available scenarios")
        print("")

    elif args.__contains__("-s") or args.__contains__("--scenarios"):
        list_scenarios()

    elif args.__contains__("-gs") or args.__contains__("--guacamole-start"):
        opt = [arg for arg in args if arg in ["-a", "--aws", "-l", "--local"]]
        if opt == []:
            opt = "local"
        else:
            if opt[0] in ["-a", "--aws"]:
                opt = "aws"
            else:
                opt = "local"
        
        guacamole_start(opt)

    elif args.__contains__("-gr") or args.__contains__("--guacamole-remove"):
        opt = [arg for arg in args if arg in ["-a", "--aws", "-l", "--local"]]
        if opt == []:
            opt = "local"
        else:
            if opt[0] in ["-a", "--aws"]:
                opt = "aws"
            else:
                opt = "local"
        
        guacamole_remove(opt)

    else:
        opt = [arg for arg in args if arg in ["-a", "--aws", "-l", "--local"]]
        if opt == []:
            if len(args) < 2:
                print("No mode specified")
                return
            opt = "local"
        else:
            if opt[0] in ["-a", "--aws"]:
                opt = "aws"
            else:
                opt = "local"

        scenario_id = [arg for arg in args if arg not in ["-a", "--aws", "-l", "--local", "-d", "--deploy", "-r", "--remove"] and arg.isnumeric()]
        if scenario_id == []:
            print("No scenario id specified")
            return
        scenario_id = scenario_id[0]

        mode = [arg for arg in args if arg in ["-d", "--deploy", "-r", "--remove"]]
        if mode == []:
            print("No mode specified")
            return
        
        mode = mode[0]
        if mode in ["-d", "--deploy"]:
            deploy(scenario_id, opt)
        else:
            remove(scenario_id, opt)


def get_all_scenarios():
    return [d for d in os.listdir(".") if os.path.isdir(d) and d.startswith("scenario")]


def scenario_info(scenario_id):
    with open("scenario" + scenario_id + "/docker-compose.yml") as stream:
        try:
            data = yaml.safe_load(stream)
            return data["x-info"]
        except yaml.YAMLError as exc:
            print(exc)

def list_scenarios():
    scenarios = get_all_scenarios()
    for scenario in scenarios[::-1]:
        id = scenario.removeprefix("scenario")
        scenario_info(id)
        print(id + " : " + scenario_info(id))


def test_guacamole_stoped(mode):
    if mode == "local":
        try:
            psycopg2.connect(
            database="guacamole_db",
            host="127.0.0.1",
            user="guacamole_user",
            password="password",
            port="5432")
            return False
        except:
            return True
    else:
        try:
            open('../guacamole/ec2_adress.txt', 'r')
            return False
        except:
            return True


def guacamole_start(mode):
    if not test_guacamole_stoped(mode):
        print("Guacamole service already started")
        return
    
    subprocess.run(["ansible-playbook", "../guacamole/guacamole.yml", "-e", f"mode={mode}", "-e", "supp=false", "--ask-become-pass"])


def test_guacamole_started(mode):
    if mode == "local":
        try:
            conn = psycopg2.connect(
            database="guacamole_db",
            host="127.0.0.1",
            user="guacamole_user",
            password="password",
            port="5432")
        except:
            print("Guacamole service not started yet")
            print("Use -gs or --guacamole-start to start it")
            return
    else:
        try:
            with open('../guacamole/ec2_adress.txt', 'r') as file:
                IP_EC2 = file.read().strip()
            conn = psycopg2.connect(
            database="guacamole_db",
            host=IP_EC2,
            user="guacamole_user",
            password="password",
            port="5432")
        except:
            print("Guacamole service not started yet")
            print("Use -gs or --guacamole-start to start it")
            return
    return conn


def guacamole_remove(mode):
    conn = test_guacamole_started(mode)

    if conn is None:
        return

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM scenarios")
        if cur.fetchone() is not None:
            print("Scenarios are still deployed, please remove them first")
            return
    except:
        pass
    
    subprocess.run(["ansible-playbook", "../guacamole/guacamole.yml", "-e", f"mode={mode}", "-e", "supp=true", "--ask-become-pass"])    


def check_scenario_deployed(scenario_id, conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM scenarios WHERE name = 'scenario" + scenario_id + "'")
        if cur.fetchone() is None:
            return False
        return True
    except:
        return False


def deploy(scenario_id, mode):
    conn = test_guacamole_started(mode)

    if conn is None:
        return

    if check_scenario_deployed(scenario_id, conn):
        print("Scenario already deployed")
        return

    if mode == "aws":
        with open('../guacamole/ec2_adress.txt', 'r') as file:
            IP_EC2 = file.read().strip()
    else:
        IP_EC2 = "none"

    playbook_name = "scenario" + scenario_id + "/scenario" + scenario_id + "_all_in_oneEC2"
    
    subprocess.run(["ansible-playbook", f"{playbook_name}.yml", "-e", f"mode={mode}", "-e", f"IP_EC2={IP_EC2}", "-e", "supp=false", "--ask-become-pass"])

    scenario = playbook_name.split("/")[0]
    
    if mode == "local":
        conn = psycopg2.connect(
            database="guacamole_db",
            host="127.0.0.1",
            user="guacamole_user",
            password="password",
            port="5432")
    else:
        with open('../guacamole/ec2_adress.txt', 'r') as file:
            IP_EC2 = file.read().strip()
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


def remove(scenario_id, mode):
    if test_guacamole_stoped(mode):
        print("Guacamole service not started yet")
        return
    
    if mode == "aws":
        with open('../guacamole/ec2_adress.txt', 'r') as file:
            IP_EC2 = file.read().strip()
    else:
        IP_EC2 = "none"

    if mode == "local":
        conn = psycopg2.connect(
            database="guacamole_db",
            host="127.0.0.1",
            user="guacamole_user",
            password="password",
            port="5432")
    elif mode == "aws": 
        conn = psycopg2.connect(
            database="guacamole_db",
            host=IP_EC2,
            user="guacamole_user",
            password="password",
            port="5432")
        
    if not check_scenario_deployed(scenario_id, conn):
        print("Scenario not deployed")
        return

    playbook_name = "scenario" + scenario_id + "/scenario" + scenario_id + "_all_in_oneEC2"
    
    subprocess.run(["ansible-playbook", f"{playbook_name}.yml", "-e", f"mode={mode}", "-e", f"IP_EC2={IP_EC2}", "-e", "supp=true", "--ask-become-pass"])

    scenario = playbook_name.split("/")[0]
    
    inscription.suppression_guacamole(conn, scenario)


if __name__ == "__main__":
    main()