def inscription_guacamole(conn) :
    cur = conn.cursor()
    # insert for kali sshd
    cur.execute("INSERT INTO guacamole_connection (connection_id, connection_name, protocol) VALUES ('1', 'KALI', 'ssh')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('1', 'hostname', '10.1.1.4')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('1', 'password', 'password')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('1', 'username', 'labuser')")
    # insert for alpine sshd
    cur.execute("INSERT INTO guacamole_connection (connection_id, connection_name, protocol) VALUES ('2', 'ALPINE', 'ssh')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('2', 'hostname', '10.1.1.2')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('2', 'password', 'password')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('2', 'username', 'labuser')")
    # insert for ftp alpine sshd
    cur.execute("INSERT INTO guacamole_connection (connection_id, connection_name, protocol) VALUES ('3', 'FTP', 'ssh')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('3', 'hostname', '10.1.1.3')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('3', 'password', 'password')")
    cur.execute("INSERT INTO guacamole_connection_parameter (connection_id, parameter_name, parameter_value) VALUES ('3', 'username', 'labuser')")
    conn.commit()


def suppression_guacamole(conn) :
    cur = conn.cursor()
    cur.execute("DELETE FROM guacamole_connection_parameter WHERE connection_id = '1'")
    cur.execute("DELETE FROM guacamole_connection WHERE connection_id = '1'")
    cur.execute("DELETE FROM guacamole_connection_parameter WHERE connection_id = '2'")
    cur.execute("DELETE FROM guacamole_connection WHERE connection_id = '2'")
    cur.execute("DELETE FROM guacamole_connection_parameter WHERE connection_id = '3'")
    cur.execute("DELETE FROM guacamole_connection WHERE connection_id = '3'")
    conn.commit()



