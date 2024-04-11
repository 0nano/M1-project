FROM alpine:latest

# Updating the system
RUN apk update

# Installing the openssh server
RUN apk add openssh sudo --no-cache

# Installing optional tools
RUN apk add tshark tcpdump vim nano --no-cache

# Creating the ssh keys and the sudo group
RUN ssh-keygen -A && addgroup sudo

# Creating an user to be used in the lab
RUN adduser -D labuser labuser

# Setting the password for the labuser
RUN echo "labuser:password" | chpasswd

# Adding the labuser to the sudo group
RUN sed -i "s/\(^sudo\:.*\)/\1labuser/" /etc/group && sed -i "s/^\#[[:space:]]\(\%sudo.*\)/\1/" /etc/sudoers

# Adding the entrypoint script to set the network configuration
COPY entry.sh /entry.sh
ENTRYPOINT ["/entry.sh"]

# Starting the ssh server
CMD ["/usr/sbin/sshd","-D"] 