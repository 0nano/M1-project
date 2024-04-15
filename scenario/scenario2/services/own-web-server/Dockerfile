# Utiliser Debian Buster Slim comme base
FROM debian:buster-slim

# Mettre à jour les dépôts et installer les packages nécessaires
RUN apt-get update && \
    apt-get install -y \
        apache2 \
        php \
        php-gd \
        php-mysqli \
        php-curl \
        git \
        openssh-server \
        sudo \
        vim \
        nano \
        mariadb-server \
        mariadb-client \
        --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*


# Installation et configuration d'OpenSSH
RUN mkdir /var/run/sshd && \
    ssh-keygen -A && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Création de l'utilisateur labuser avec des privilèges sudo
RUN useradd -m labuser && \
    echo 'labuser:password' | chpasswd && \
    usermod -aG sudo labuser


# Copier les fichiers de votre application web dans le conteneur
COPY html/ /var/www/localhost/htdocs/

# Configurer Apache et PHP
RUN sed -i 's#DocumentRoot /var/www/html#DocumentRoot /var/www/localhost/htdocs#' /etc/apache2/apache2.conf && \
    sed -i 's#<Directory /var/www/html>#<Directory /var/www/localhost/htdocs>#' /etc/apache2/apache2.conf && \
    mkdir -p /run/apache2

RUN mkdir -p /var/run/mysqld
RUN chown mysql:mysql /var/run/mysqld

# Attention httpd doit être demarrer systemcl 
# voir alpine ssh 
# Pour rendre l'apahce indépendant du docker 

# Configurer MySQL pour écouter sur toutes les interfaces
RUN sed -i 's/bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/' /etc/mysql/my.cnf


EXPOSE 80

EXPOSE 3306 

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh

# Removing windows /r character
RUN sed -i -e 's/\r$//' /entry.sh 

ENTRYPOINT ["/entry.sh"]

# demarraer apache et mariadb 
CMD ["/usr/sbin/sshd","-D"] 

