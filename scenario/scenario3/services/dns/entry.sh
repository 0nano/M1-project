#!/bin/sh
if [ -n "$GW" ]; then
	echo "Setting GW to $GW" 
	/sbin/route del default 
	/sbin/route add default gw $GW
else
	echo "GW env parameter not set"
	echo "Keeping defaults"
fi
echo $'port=53\nlisten-address=127.0.0.1,10.1.3.4\ninterface=eth0\ndomain-needed
bogus-priv\nexpand-hosts\nno-resolv\nserver=1.1.1.1\nserver=8.8.8.8\ncache-size=1000\n' >> /etc/dnsmasq.conf
dnsmasq
exec $@