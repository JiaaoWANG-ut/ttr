import paramiko
import hashlib
import time
import struct
import hmac
import base64
import sys
import datetime
#import subprocess
#import pyperclip

command1='date;python3 ~/scripts/nodesview.py;squeue -u $USER;echo "<br/>";squeue'
##workdir is HT-files mother file
workdir="/home1/08197/jiaao/Scratch/GCN/trainingset_addLi"
hostname='login2.stampede2.tacc.utexas.edu'
port=22
username='jiaao'
YourOwnSeries='NRYKB66RYGM75JKJ7T6UANAWCIVRALHP'
key_filename="id_rsa"

#command='cd '+workdir+';python3 queue-state.py'
#command1='python3 ~/scripts/nodesview1.1.py;squeue;date'


refresh: int=30       ###refresh time
token_length: int=6  ###token_length
timestamp = time.time()
counter = int(timestamp) // refresh
msg = struct.pack('>Q', counter)
digest = hmac.new(base64.b32decode(YourOwnSeries), msg, hashlib.sha1).digest()
ob = digest[19]
pos = ob & 15
base = struct.unpack('>I', digest[pos:pos + 4])[0] & 0x7fffffff
token = base % (10**token_length)
password=str(token)

if len(password)!=6:
    print(password)
    print("Please Refresh webpage in 30 sec. Waiting for new Token Generation ")
    sys.exit()


#print(len(password))
#print(password)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
try:
    ssh.connect(hostname=hostname, port=port,username=username,password=password,key_filename=key_filename,timeout=30,compress=True)
except:
    print("Busy, Down or Under Maintaining,Try Refresh web in 30 sec.,  Or Check Server Status: https://portal.tacc.utexas.edu/")
    sys.exit()

stdin, stdout, stderr = ssh.exec_command(command1, bufsize=-1, timeout=None, get_pty=False)

output=stdout.readlines()


del stdin, stdout, stderr


ssh.close()



#current_datetime = datetime.datetime.now()
#print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

if len(password)!=6:
    d=1
else:
    output_new=[]
    for line in output:
        output_new.append(line.rjust(25," "))

    ms=' '.join(map(str,output_new))
    output_f=ms.replace("\n","<br/>")
    #print(output_f)
    open("temp","w").writelines(output_f)
    print("Updated to now!")
    sys.exit()
    #print(output)
    #print(output.replace("\n","<br/>"))
#print(output)

#now_time = datetime.now(timezone('America/Chicago'))
#ttime="Updated Time "+str(now_time.strftime('%I:%M:%S %p'))+" Central Time (CT) GMT-06:00"

#print(ttime) 

