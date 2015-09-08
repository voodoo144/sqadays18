#!/usr/bin/python
import sys
import subprocess

serf_payload=""

for line in sys.stdin:
    serf_payload+=line
    
command="ps aux | grep '%s' | grep -v 'grep' | tr -s ' ' | cut -d' ' -f2 "%serf_payload.rstrip()
pid = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE).stdout.read()
command="lsof -w -a -p%s -i4 | grep LISTEN | tr -s ' ' |cut -d' ' -f9 "%pid.rstrip()
port = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
print port.split(":")[1]
