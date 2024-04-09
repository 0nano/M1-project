FROM bkimminich/juice-shop

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh
ENTRYPOINT ["/entry.sh"]

# Starting the ssh and ftp servers
CMD ["/usr/sbin/sshd","-D"] 