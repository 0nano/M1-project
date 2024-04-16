FROM kalilinux/kali-last-release

# Updating and upgrading the system
RUN apt update && apt upgrade -y

# Installing the necessary tools based on the kali-tools-web
RUN apt install -y ncrack nikto nmap ftester openssh-server openssh-client sudo \
httprint hydra dirb webshells tcpdump nano vim dnsutils \
less iproute2 iptables net-tools man-db iputils-ping iputils-arping lynx \
# Some tools to identify if it's really usefull to have them
hamster-sidejack mitmproxy sqlmap wafw00f weevely

# Creating an user to be used in the lab
RUN addgroup labuser && adduser labuser --ingroup labuser

# Verifying if the user home was created
RUN mkdir -p /home/labuser

# Setting the password for the labuser
RUN echo "labuser:password" | chpasswd

# Adding the labuser to the sudo group
RUN sed -i "s/\(^sudo\:.*\)/\1labuser/" /etc/group && sed -i "s/^\#[[:space:]]\(\%sudo.*\)/\1/" /etc/sudoers

# Create the directory for the sshd
RUN mkdir -p /run/sshd

# Adding the entrypoint script to set the network configuration
COPY ../entry.sh /entry.sh
RUN chmod a+x /entry.sh
ENTRYPOINT ["/entry.sh"]

# Starting the ssh server
CMD ["/usr/sbin/sshd", "-D"] 