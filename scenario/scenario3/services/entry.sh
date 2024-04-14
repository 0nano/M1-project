#!/bin/sh
if [ -n "$GW" ]; then
	echo "Setting GW to $GW" 
	/sbin/route del default 
	/sbin/route add default gw $GW
else
	echo "GW env parameter not set"
	echo "Keeping defaults"
fi
if [ -n "$DNS" ]; then
	echo "Setting DNS to $DNS"
	sed -i "s/nameserver */nameserver $DNS/" /etc/resolv.conf
else
	echo "DNS env parameter not set"
	echo "Keeping defaults"
fi
exec $@