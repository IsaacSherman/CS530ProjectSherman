#!/bin/bash
n=1
while (($n <= 1000))
	do
		gettemp>>temp.txt
		getvolts>>volts.txt
		sleep 5
		n=$((n+1))
		echo loop
	done
