# Partie 1 ssh 
FROM debian:buster-slim
LABEL stage=debian


RUN apt-get update && \
    apt-get install -y \
        php \
        php-gd \
        php-mysqli \
        php-curl \
        git \
        openssh-server \
        sudo \
        vim \
        nano \
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

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh

# Removing windows /r character
RUN sed -i -e 's/\r$//' /entry.sh 

ENTRYPOINT ["/entry.sh"]

# demarraer apache et mariadb 
CMD ["/usr/sbin/sshd","-D"] 

# Partie 2 apache

FROM php:apache AS php-apache
LABEL stage=php-apache

# Copiez le contenu de l'application dans le répertoire web
COPY html /var/www/html

# Exposez le port 80
EXPOSE 80

# Stage 3 mysql
FROM mysql AS mysql
LABEL stage=mysql

# Définissez les variables d'environnement pour MySQL
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=website

# Copiez le script SQL de création d'utilisateurs dans le conteneur
COPY create_users.sql /docker-entrypoint-initdb.d/

# Exposez le port 3306
EXPOSE 3306
