FROM kalilinux/kali-rolling

# Updating and upgrading the system
RUN apt update && apt upgrade -y

# Installing the necessary tools based on the kali-tools-web
RUN apt install -y ncrack nikto nmap ftester \
httprint hydra dirb webshells tcpdump \
# Some tools to identify if it's really usefull to have them
hamster-sidejack mitmproxy sqlmap wafw00f weevely
