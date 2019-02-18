import time, os
from datetime import datetime, timedelta

now =  datetime.now()
today = now
next_date = today

def getData(time):
    year, month, day, hour = time.strftime("%Y,%m,%d,%H").split(',')
    return (year, month, day, hour)


def GetTime(today):
    global next_date
    t_hours = next_date.hour + next_date.minute / 60. + next_date.second / 3600.
    t_hour = t_hours // 6

    if today == next_date:
        next_date = today + timedelta(days=-1, hours=-(t_hours - t_hour*6))
    else:
        next_date = next_date + timedelta(hours=-(6))
        #print(next_date)
    return getData(next_date)
#
# WOrk with file 
#

script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
rel_path = "Output/New_All_UA/downloaded_files.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def addNull(num):
    if num < 9 and num > 0:
        return '0' + str(num)

print(abs_file_path)

f = open(abs_file_path, 'r')
last_line = f.readlines()[-1]
prefix = '\n' + last_line[:11]
date = last_line[11:24]
date_y = last_line[11:15]
date_m = last_line[16:18]
date_d = last_line[19:21]
date_h = last_line[22:24]
sufix = last_line[24:]

#date2 = str(date_y + date_m + date_d + date_h)
date2 = datetime(year=int(last_line[11:15]), month=int(last_line[16:18]), day=int(last_line[19:21]), hour=int(last_line[22:24]))
f.close()

print('last date in file - ', date2)

def getStr(date):
    
    global prefix, sufix
    s = prefix + date + sufix
    print(s)
    return str(s)

fw = open(abs_file_path, 'a')

i = 0
while date2 < next_date:
    all_time = GetTime(today)
    s_date = all_time[0] + '-' + all_time[1] + '-' + all_time[2] + '_' + all_time[3]
    fw.write(getStr(s_date))
    i = i + 1

fw.close()
