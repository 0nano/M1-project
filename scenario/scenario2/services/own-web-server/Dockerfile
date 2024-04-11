FROM alpine:latest

# Updating the system
RUN apk update

# install apache 

RUN apk add openssh sudo apache2 mysql mysql-client --no-cache

# Creating the ssh keys and the sudo group
RUN ssh-keygen -A && addgroup sudo

# Creating an user to be used in the lab
RUN adduser -D labuser labuser

# Setting the password for the labuser
RUN echo "labuser:password" | chpasswd

# Adding the labuser to the sudo group
RUN sed -i "s/\(^sudo\:.*\)/\1labuser/" /etc/group && sed -i "s/^\#[[:space:]]\(\%sudo.*\)/\1/" /etc/sudoers

# Copier les fichiers de votre application web dans le conteneur
COPY html/ /var/www/localhost/htdocs/

# Configurer Apache et PHP
RUN sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/httpd.conf && \
    sed -i 's#^DocumentRoot ".*#DocumentRoot "/var/www/localhost/htdocs"#g' /etc/apache2/httpd.conf && \
    sed -i 's#^ServerRoot ".*#ServerRoot "/var/www"#g' /etc/apache2/httpd.conf && \
    mkdir -p /run/apache2

# Démarrer les services Apache et MySQL au démarrage du conteneur
CMD /etc/init.d/apache2 start && /etc/init.d/mysql start && tail -f /dev/null
# Attention httpd doit être demarrer systemcl 
# voir alpine ssh 
# Pour rendre l'apahce indépendant du docker 

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh

# Removing windows /r character
RUN sed -i -e 's/\r$//' /entry.sh 

ENTRYPOINT ["/entry.sh"]

# Starting the ssh server
CMD ["/usr/sbin/sshd","-D"] 