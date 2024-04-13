FROM debian:buster-slim

# Mettre à jour les dépôts et installer les packages nécessaires
RUN apt-get update && \
    apt-get install -y \
        git \
        openssh-server \
        sudo \
        vim \
        nano \
        nodejs \
        npm \
        sqlite3 \
        ca-certificates \
        curl

RUN git clone --depth 1 -c http.sslVerify=false https://github.com/juice-shop/juice-shop.git

RUN cd juice-shop && npm install 

#CMD cd juice-shop && npm start # can't use CMD ere it will cut all only one CMD by Dockerfile
# RUN cd juice-shop && npm start

# # Installation et configuration d'OpenSSH
RUN mkdir /var/run/sshd && \
    ssh-keygen -A && \
        sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Création de l'utilisateur labuser avec des privilèges sudo
RUN useradd -m labuser && \
    echo 'labuser:password' | chpasswd && \
    usermod -aG sudo labuser

# Exposer le port 80 sur lequel l'application s'exécute
EXPOSE 80
EXPOSE 3000
# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh

# Removing windows /r character
RUN sed -i -e 's/\r$//' /entry.sh 

ENTRYPOINT ["/entry.sh"]

# Démarrer Apache et SSH au lancement du conteneur
CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D && cd juice-shop && npm start"]

#CMD ["/usr/sbin/sshd","-D"] 



# # Supprimer le répertoire /var/www/html s'il existe déjà
# # RUN rm -rf /var/www/html



