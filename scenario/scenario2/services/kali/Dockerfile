# KALI DU SCENARIO 2 NOT THE SAME COMPONENT AS THE SCENARIO 1
FROM kalilinux/kali-last-release

# Updating and upgrading the system
RUN apt update && apt upgrade -y

# Installing the necessary tools based on the kali-tools-web --> add less packages / iputils-ping/iputils-arping / iproute2 net-tools iptables man / lynx
RUN apt install -y ncrack nikto nmap ftester openssh-server openssh-client sudo \
httprint hydra dirb webshells \
# Some tools to identify if it's really usefull to have them
hamster-sidejack sqlmap weevely

# Creating the ssh keys -- > a modif pas forcement besoin
RUN ssh-keygen -A 

# Creating an user to be used in the lab --> 
RUN addgroup labuser && adduser labuser --ingroup labuser

# Setting the password for the labuser
RUN echo "labuser:password" | chpasswd

# Adding the labuser to the sudo group  --> fixer le shell bin/bash pour la colorisation 
RUN adduser labuser sudo

# Create the directory for the sshd --> mkdir -p pour créer arbo 
RUN mkdir /run/sshd

# Adding the entrypoint script to set the network configuration
# COPY ../entry.sh /
# ENTRYPOINT ["/entry.sh"]

# Starting the ssh and ftp servers
CMD ["/usr/sbin/sshd","-D"] 