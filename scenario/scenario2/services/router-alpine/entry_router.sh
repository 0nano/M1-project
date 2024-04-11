#!/bin/sh
echo "Enabling forwarding"
echo 1 > /proc/sys/net/ipv4/ip_forward
if [ -n "$GW" ]; then
	echo "Setting GW to $GW"
	/sbin/route del default
	/sbin/route add default gw $GW
else
	echo "GW env parameter not set"
	echo "Keeping defaults"
fi

if [ "$NAT" = "true" ]; then 
	ETH=$(ip route sh | grep default | sed "s/.*dev \(.*$\)/\1/")
	echo "Setting NAT on $ETH"
	/sbin/iptables -t nat -A POSTROUTING -o $ETH -j MASQUERADE
fi
exec $@