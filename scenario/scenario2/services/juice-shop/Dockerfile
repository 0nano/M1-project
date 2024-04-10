# Utiliser Debian Buster Slim comme base

FROM debian:buster-slim

# Mettre à jour les dépôts et installer les packages nécessaires
RUN apt-get update && \
    apt-get install -y \
        git \
        openssh-server \
        sudo \
        vim \
        nano \
        --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Supprimer le répertoire /var/www/html s'il existe déjà
RUN rm -rf /var/www/html
# weird but need to ignore SSL certificat 
RUN git clone --depth 1 -c http.sslVerify=false https://github.com/juice-shop/juice-shop.git

RUN  cd juice-shop

RUN npm install

RUN npm start 

# Installation et configuration d'OpenSSH
RUN mkdir /var/run/sshd && \
    ssh-keygen -A && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Création de l'utilisateur labuser avec des privilèges sudo
RUN useradd -m labuser && \
    echo 'labuser:password' | chpasswd && \
    usermod -aG sudo labuser


# Exposer le port 80 pour qu'il s'execute pas sur le 3000 et que guaca le trouve
EXPOSE 80   

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh
ENTRYPOINT ["/entry.sh"]

# Démarrer Apache et SSH au lancement du conteneur
CMD ["/usr/sbin/sshd -D"]






