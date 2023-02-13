import paramiko
import hashlib
import time
import struct
import hmac
import base64
#import subprocess
#import pyperclip

##workdir is HT-files mother file
workdir="/global/homes/j/jiaao/accounts/jiaao/GCN/trainingset"
hostname='cori.nersc.gov'
port=22
username='jiaao'
YourOwnSeries='M34OITU7YKHAILNXBKHZZ2LL2QXY54KV'

command='cd '+workdir+';python3 queue-state.py'
command1='cd '+workdir+';python3 sbatch1.py'


from datetime import datetime
from pytz import timezone

now_time = datetime.now(timezone('America/Chicago'))
ttime="Updated Time "+str(now_time.strftime('%I:%M:%S %p'))+" Central Time (CT) GMT-06:00"


import matplotlib.pyplot as plt
import numpy as np

jobname="".join(filter(str.isalpha, workdir))
FJ=12
UF=13#int(output[0].split()[2])
PJ=14#int(output[0].split()[3])
RJ=16#int(output[0].split()[4])
fontsize=7
dpi=100

plt.figure(figsize=(10,3)).suptitle(' ',x=0.9,y=0.5,rotation=90)


############Job Monitor########


y = np.array([FJ, UF])
ax1=plt.subplot(1, 2, 1)
ax1.pie(y,
        labels=[str(FJ)+' Finished Job(s)',str(UF)+' Unfinished Job(s)'], # 设置饼图标签
        colors=["#d5695d", "#5d8ca8"], # 设置饼图颜色
        explode=(0, 0.2), # 第二部分突出显示，值越大，距离中心越远
        autopct='%.3f%%', # 格式化输出百分比
    textprops ={"fontsize":fontsize}   )
ax1.set_title("\n \n Workdir: "+str(workdir)+"\nTotal High Throughput Jobs: "+str(FJ+UF),fontsize=fontsize)
#ax1.xlabel(ttime, color = 'gray')

#plt.show()


#plt.savefig("/var/www/html/images/"+jobname+"_job.png")

######################queue monitor#######################



y = np.array([PJ, RJ])
ax2=plt.subplot(1, 2, 2)
ax2.pie(y,
        labels=[str(PJ)+' Pending Job(s)',str(RJ)+' Running Job(s)'], # 设置饼图标签
        colors=["#5d8ca8", "#d5695d"], # 设置饼图颜色
        explode=(0, 0.2), # 第二部分突出显示，值越大，距离中心越远
        autopct='%.3f%%', # 格式化输出百分比
       textprops ={"fontsize":fontsize})
ax2.set_xlabel("\n"+ttime, color = 'gray',fontsize=fontsize)
ax2.set_title("\nServer Load\nTotal Queued Jobs: "+str(PJ+RJ),fontsize=fontsize)
#plt.text(0, 0, 'First')
plt.savefig("/var/www/html/images/"+jobname+"_queue.png", dpi=dpi)

plt.show()


