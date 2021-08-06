from datetime import datetime
import time
import random

deadline = input("输入截止时间：")

if(len(deadline) == 10):
    end_time = datetime.strptime(deadline, "%Y-%m-%d")
else:
    end_time = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")

while True:
    cur = datetime.now()

    if(cur > end_time):
        break

    timeleft = (end_time-cur).total_seconds()

    days = 0
    if(timeleft > (24*60*60)):
        days =  int(timeleft/(24*60*60))
        timeleft -= days * (24*60*60)
    
    hours = 0
    if(timeleft > (60*60)):
        hours = int(timeleft/(60*60))
        timeleft -= hours * 60 * 60

    minutes = 0
    if(timeleft > 60):
        minutes = int(timeleft/60)
        timeleft -= minutes * 60

    print('{} days {} hours {} minutes {} seconds left...'.format(days, hours, minutes, int(timeleft)))
    time.sleep(random.randint(30, 60))

print("DEADLINE!")
