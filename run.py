import os
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
rel_path = "Output/New_All_UA/downloaded_files.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def addNull(num):
    if num < 9 and num > 0:
        print('0' + str(num))
        return '0' + str(num)

print(abs_file_path)

f = open(abs_file_path, 'r')
last_line = f.readlines()[-1]
prefix = last_line[:11]
date = last_line[11:24]
date_y = last_line[11:15]
date_m = last_line[16:18]
date_d = last_line[19:21]
date_h = last_line[22:24]
sufix = last_line[24:]

print(date)
s_date = '2019-02-18_18'

def getStr(date):
        global prefix, sufix
        s = prefix + date + sufix
        print(s)
        return str(s)

f.close()

fw = open(abs_file_path, 'a')

fw.write(getStr(s_date))
fw.close()