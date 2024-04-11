#!/bin/sh
if [ -n "$GW" ]; then
	echo "Setting GW to $GW" 
	/sbin/route del default 
	/sbin/route add default gw $GW
else
	echo "GW env parameter not set"
	echo "Keeping defaults"
fi
exec $@

