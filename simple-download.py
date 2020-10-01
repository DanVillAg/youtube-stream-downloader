# -*- coding: utf-8 -*-
import datetime
import time
import subprocess

### CHANGE THE URL HERE ####
URL = 'https://www.youtube.com/watch?v=XJfpbcIyETo'
quality = 'best' # can choose from 720p, 480p, 240p 

# define Job
def job_function():
    now = datetime.datetime.now()
    outputfile = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'-'+str(now.hour)+str(now.minute)+'.ts'
    
    command='streamlink ' + URL + ' '+ quality + ' --hls-start-offset 00:01:00 --hls-duration 00:01:00 -o ' + outputfile
    subprocess.call(command, shell=True)
    command2 = 'gsutil cp ' + outputfile + ' gs://transfer-bucket-cc/'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'/'
    subprocess.call(command2, shell=True)
    time.sleep(20)

# Schedules job_function
job_function()


#gsutil cp raulms-object-one.txt gs://transfer-bucket-cc
