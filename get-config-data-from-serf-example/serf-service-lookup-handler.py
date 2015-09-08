#!/usr/bin/python
import sys
import subprocess

serf_payload=""

for line in sys.stdin:
    serf_payload+=line
    
def exec_command(command):
    return subprocess.Popen(command,shell=True, stdout=subprocess.PIPE).stdout.read()

pid=exec_command("ps aux | grep '%s' | grep -v 'grep' | tr -s ' ' | cut -d' ' -f2 "%serf_payload.rstrip())    
port=exec_command("lsof -w -a -p%s -i4 | grep LISTEN | tr -s ' ' |cut -d' ' -f9 "%pid.rstrip())

print port.split(":")[1]
