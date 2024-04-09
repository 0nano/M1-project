import yaml

def suppression_guacamole(conn, scenario) :
    cur = conn.cursor()
    cur.execute("SELECT connections_id FROM scenarios WHERE name = '" + scenario + "'")
    connections_id = cur.fetchone()[0]
    connections_id = connections_id[0]
    for connection_id in connections_id:
        cur.execute("DELETE FROM guacamole_connection_parameter WHERE connection_id = '" + str(connection_id) + "'")
        cur.execute("DELETE FROM guacamole_connection WHERE connection_id = '" + str(connection_id) + "'")
    cur.execute("DELETE FROM scenarios WHERE name = '" + scenario + "'")
    conn.commit()


def inscription_guacamole(conn, scenario) :
    with open("/home/isen/M1-project/scenario/" + scenario + "/docker-compose.yml") as stream:
        try:
            data = yaml.safe_load(stream)
            connections_id = []
            for service in data["services"]:
                if "x-inscription" not in data["services"][service] or data["services"][service]["x-inscription"] == "none":
                    continue
                cur = conn.cursor()
                cur.execute("INSERT INTO guacamole_connection (connection_name, protocol) VALUES ('" + service + "_" + scenario + "', 'ssh')")
                conn.commit()
                cur.execute("SELECT connection_id FROM guacamole_connection WHERE connection_name = '" + service + "_" + scenario + "'")
                connection_id = cur.fetchone()[0]
                cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('" + str(connection_id) + "', 'hostname', '" + data["services"][service]["x-inscription"] + "')")
                cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('" + str(connection_id) + "', 'password', 'password')")
                cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('" + str(connection_id) + "', 'username', 'labuser')")
                conn.commit()
                connections_id.append(connection_id)
            cur.execute("INSERT INTO scenarios (name, connections_id) VALUES ('" + scenario + "', ARRAY[" + str(connections_id) + "])")
            conn.commit()
        except yaml.YAMLError as exc:
            print(exc)