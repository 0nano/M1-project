# FROM alpine:latest

# # Mise à jour du système et installation des outils nécessaires
# RUN apk update && \
#     apk add --no-cache openssh-server nodejs npm git

# # Configuration du service SSH
# RUN mkdir /var/run/sshd

# # Création des clés SSH
# RUN ssh-keygen -A

# # Téléchargement de Juice Shop depuis GitHub
# RUN git clone https://github.com/juice-shop/juice-shop.git --depth 1 /juice-shop

# # Installation des dépendances de Juice Shop
# WORKDIR /juice-shop
# RUN npm install --production

# # Création d'un utilisateur pour être utilisé dans le lab
# RUN adduser -D -s /bin/bash labuser

# # Définition du mot de passe pour l'utilisateur labuser
# RUN echo "labuser:password" | chpasswd

# # Exposition du port 3000 utilisé par Juice Shop
# EXPOSE 3000

# # Adding the entrypoint script to set the network configuration
# COPY entry.sh /entry.sh
# ENTRYPOINT ["/entry.sh"]

#FROM bkimminich/juice-shop

# apk add openssh-server


# Utilisation de l'image node:20-buster comme base
# FROM node:20-buster as installer

# # Mise à jour et installation des outils nécessaires
# RUN apt-get update && \
#     apt-get install -y openssh-server

# # Configuration du service SSH
# RUN mkdir /var/run/sshd

# # Création des clés SSH
# RUN ssh-keygen -A

# # Nettoyage du cache npm
# RUN npm cache clean --force

# # Installation de Juice Shop et reconstruction
# RUN npm install -g juice-shop && npm rebuild

# # Configuration du service SSH
# CMD ["/usr/sbin/sshd", "-D"]

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

RUN 
git clone https://github.com/juice-shop/juice-shop.git --depth 1

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

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh
ENTRYPOINT ["/entry.sh"]

# Démarrer Apache et SSH au lancement du conteneur
CMD ["/usr/sbin/sshd -D"]






