FROM alpine:latest

# Updating the system
RUN apk update

# install apache 

RUN apk add apache2 mysql mysql-client --no-cache

# Copier les fichiers de votre application web dans le conteneur
COPY html/ /var/www/localhost/htdocs/

# Configurer Apache et PHP
RUN sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/httpd.conf && \
    sed -i 's#^DocumentRoot ".*#DocumentRoot "/var/www/localhost/htdocs"#g' /etc/apache2/httpd.conf && \
    sed -i 's#^ServerRoot ".*#ServerRoot "/var/www"#g' /etc/apache2/httpd.conf && \
    mkdir -p /run/apache2

# Démarrer les services Apache et MySQL au démarrage du conteneur
CMD httpd -D FOREGROUND && /etc/init.d/mysql start && tail -f /dev/null

# Adding the entrypoint script to set the network configuration
COPY ../entry.sh /entry.sh
ENTRYPOINT ["/entry.sh"]