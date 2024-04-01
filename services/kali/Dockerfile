FROM kalilinux/kali-last-release

# Updating and upgrading the system
RUN apt update && apt upgrade -y

# Installing the necessary tools based on the kali-tools-web
RUN apt install -y ncrack nikto nmap ftester openssh-server openssh-client sudo \
httprint hydra dirb webshells tcpdump \
# Some tools to identify if it's really usefull to have them
hamster-sidejack mitmproxy sqlmap wafw00f weevely

# Creating the ssh keys
RUN ssh-keygen -A

# Creating an user to be used in the lab
RUN addgroup labuser && adduser labuser --ingroup labuser

# Setting the password for the labuser
RUN echo "labuser:password" | chpasswd

# Adding the labuser to the sudo group
RUN adduser labuser sudo

# Create the directory for the sshd
RUN mkdir /run/sshd

# Adding the entrypoint script to set the network configuration
COPY ../entry.sh /entry.sh
ENTRYPOINT ["/entry.sh"]

# Starting the ssh and ftp servers
CMD ["/usr/sbin/sshd","-D"] 