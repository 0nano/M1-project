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
        --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Supprimer le répertoire /var/www/html s'il existe déjà
RUN rm -rf /var/www/html

# Cloner DVWA depuis GitHub dans /var/www/html
RUN git clone --depth 1 -c http.sslVerify=false https://github.com/ethicalhack3r/DVWA /var/www/html

# Copier le fichier de configuration par défaut
RUN cp /var/www/html/config/config.inc.php.dist /var/www/html/config/config.inc.php

# Configurer Apache pour servir DVWA
RUN sed -i 's#AllowOverride None#AllowOverride All#' /etc/apache2/apache2.conf
#EXPOSE 80
# Installation et configuration d'OpenSSH
RUN mkdir /var/run/sshd && \
    ssh-keygen -A && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Création de l'utilisateur labuser avec des privilèges sudo
RUN useradd -m labuser && \
    echo 'labuser:password' | chpasswd && \
    usermod -aG sudo labuser


# Exposer le port 80 pour que guaca le trouve
EXPOSE 5000

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh

# Removing windows /r character
RUN sed -i -e 's/\r$//' /entry.sh 

ENTRYPOINT ["/entry.sh"]

# Démarrer Apache et SSH au lancement du conteneur
CMD ["/usr/sbin/sshd","-D"] 

