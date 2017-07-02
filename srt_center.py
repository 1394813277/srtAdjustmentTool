#!/usr/bin/python  
# coding:utf-8
# Filename: hello.py
import sys
import re
import platform
import os
#调整srt字幕

def adjustment(plusorminus,str1,str2):

    hour1 = int(str1[0:2])
    minu1 = int(str1[3:5])
    sec1 = int(str1[6:8])
    millisecond1 = int(str1[9:12])

    hour2 = int(str2[0:2])
    minu2 = int(str2[3:5])
    sec2 = int(str2[6:8])
    millisecond2 = int(str2[9:12])

    millisecond3 = 0
    sec3 = 0
    minu3 = 0
    hour3 = 0

    if plusorminus.endswith('+'):        
        millisecond3 = (millisecond1 + millisecond2)%1000
        sec3 = (sec1 + sec2 + millisecond3/1000)%60
        minu3 = (minu1 + minu2 + sec3/60)%60
        hour3 = (hour1 + hour2) + minu3/60

        #add
    else:
        hour3 = hour1 - hour2
        minu3 = minu1 - minu2
        sec3 = sec1 - sec2
        millisecond3 = millisecond1 - millisecond2

        if hour3 < 0:
            hour3 = 0

        if minu3 < 0:
            hour3 = hour3 - 1
            minu3 = minu3 + 60

        if sec3 < 0:
            minu3 = minu3 - 1
            sec3 = sec3 + 60

        if millisecond3 < 0:
            sec3 = sec3 - 1
            millisecond3 = millisecond3 + 1000
        

    return '%02d:%02d:%02d,%03d' % (hour3,minu3,sec3,millisecond3) 
        #jian
    

def dispose(filename,ss,ad):

    
    
    # 

    (filepath,tempfilename) = os.path.split(filename)
    (filename1,extension) = os.path.splitext(tempfilename)
    newResultPath = os.path.join(filepath,filename1 + '_adjusted'+extension)
    print(newResultPath)

    result = ''
    f1 = open(newResultPath,'w')

    with open(filename,'r') as f:
        for lines in f.readlines():
            if re.match(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d',lines,flags = 0):
                string1 = lines[0:12]
                string2 = lines[17:29]
                result = result + adjustment(ad,string1,ss) + ' --> ' + adjustment(ad,string2,ss) + '\n'
            else:
                result = result + lines

        
        # print(result)
    f1.write(result)
    f1.close()

    print('完毕，新地址在',newResultPath)

try:
    if (int(platform.python_version().split('.')[0]) >= 3):
        if sys.argv[1].endswith('srt'):
            ss = input('请输入调整时间：,举例：00:00:00,001\n')
            ad = input('请输入字幕延后或者提前，延后输入+，提前输入-:\n')
            dispose(sys.argv[1],ss,ad)
        else:
            print("请使用本工具调整srt字幕，其他字幕暂不支持")
    else:
        print('请在python3上运行')
except:
    print('请在python后面附带srt完整路径')



