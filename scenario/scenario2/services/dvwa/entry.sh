#!/bin/sh
if [ -n "$GW" ]; then
	echo "Setting GW to $GW" 
	/sbin/route del default 
	/sbin/route add default gw $GW
else
	echo "GW env parameter not set"
	echo "Keeping defaults"
fi
#exec $@ # Aussi fou que ça soit cette ligne est considéré comme un fin de ligne Windows et donc en peut être executé sur debian 
