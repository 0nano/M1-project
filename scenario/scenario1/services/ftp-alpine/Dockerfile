FROM alpine:latest

# Updating the system
RUN apk update 

# Installing the ftp and ssh servers
RUN apk add vsftpd openssh sudo --no-cache

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

# Editing the ftp server configuration
RUN sed -i "s/#\(anonymous_enable=\)YES/\1NO/" /etc/vsftpd/vsftpd.conf
RUN echo "seccomp_sandbox=NO" >> /etc/vsftpd/vsftpd.conf
RUN echo "local_enable=YES" >> /etc/vsftpd/vsftpd.conf
RUN echo "write_enable=YES" >> /etc/vsftpd/vsftpd.conf
RUN echo "local_umask=022" >> /etc/vsftpd/vsftpd.conf
RUN echo "chroot_local_user=YES" >> /etc/vsftpd/vsftpd.conf
RUN echo "allow_writeable_chroot=YES" >> /etc/vsftpd/vsftpd.conf
RUN echo "passwd_chroot_enable=YES" >> /etc/vsftpd/vsftpd.conf
RUN echo "ftpd_banner=Welcome to vsftpd" >> /etc/vsftpd/vsftpd.conf
RUN echo "max_clients=10" >> /etc/vsftpd/vsftpd.conf
RUN echo "max_per_ip=5" >> /etc/vsftpd/vsftpd.conf

# Adding the entrypoint script to set the network configuration
COPY ../entry.sh /entry.sh
ENTRYPOINT ["/entry.sh"]

# Starting the ssh and ftp servers
CMD ["/usr/sbin/sshd","-D"] 