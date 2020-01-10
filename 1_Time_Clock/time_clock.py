import time
import os

def two_digits(string):
    if len(string) <2:
        string = '0'+string
    return string

def subtract_time(t1, t2):
    start, end = convert_time_to_seconds(t1, t2)
    total = end - start;
    return convert_seconds_to_time(total)

def add_time(t1, t2):
    start, end = convert_time_to_seconds(t1,t2)
    total = start + end;
    return convert_seconds_to_time(total)
  
def convert_time_to_seconds(start, end):
    time1 = start[0]*3600 + start[1]*60 + start[2]
    time2 = end[0]*3600 + end[1]*60 + end[2]
    return time1, time2
    
def convert_seconds_to_time(total):
    secs = total % 60
    mins = int(total /60) %60
    hr = int(total/3600)
    return [hr,mins,secs]
    
def format_time(tm):
    string = two_digits(str(tm[0]))+':'
    string += two_digits(str(tm[1]))+':'
    string += two_digits(str(tm[2]))+'\n'
    return string

def remove_temp_files():
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")

def parse_date():
    localtime = time.localtime(time.time())
    string = str(localtime)
    string = string.replace('(',',')
    string = string.replace(')','')
    string = string.replace('=',',')
    arr = string.split(',')
    temp = {}
    temp['year'] = arr[2]
    temp['month'] = two_digits(arr[4])
    temp['day'] = two_digits(arr[6])
    temp['hour'] = two_digits(arr[8])
    temp['min'] = two_digits(arr[10])
    temp['sec'] = two_digits(arr[12])
    return temp

def day_heading():
    date = parse_date()
    fh = open("time.txt","a+")
    fh.write(str(date['month'])+"/"+str(date['day'])+'/'+str(date['year'])+'\n');

def clock_in():
    date = parse_date()
    fh = open('time.txt','a+')
    fh_temp = open("temp.txt","a+")
    clock('In: ',fh,fh_temp,date)

def clock_out():
    date = parse_date()
    fh = open("time.txt","a+")
    fh_temp = open("temp.txt","a+")
    clock('Out: ',fh, fh_temp,date)

def log_hours():
    work_time = calc_total();
    fh = open("time_log.txt","a+")
    date = parse_date()
    string = "Logged: "+date['month']+'/'+date['day']+'/'+date['year']+' Hours Worked: '+ work_time
    fh.write(string)
    remove_temp_files()
    

def clock(string,fh, fh_temp,date):
    fh.write('\t'+string+str(date['hour'])+":"+str(date['min'])+":"+str(date['sec'])+'\n');
    fh_temp.write(string+str(date['hour'])+":"+str(date['min'])+":"+str(date['sec'])+'\n');
       
def calc_total():
    tm = [0,0,0]
    temp_tm = [0,0,0]
    fh = open('temp.txt','r')
    line = fh.readline()
    while line:
        arr = str(line).split(':')
        arr[0] = arr[0].strip()
        if arr[0] =='In':
            temp_tm = int(arr[1]),int(arr[2]),int(arr[3])
        elif arr[0] == 'Out':
            temp_tm = subtract_time(temp_tm,[int(arr[1]),int(arr[2]),int(arr[3])])
            tm = add_time(tm, temp_tm)
        line = fh.readline()
    return format_time(tm)        

def UI():
    run = True
    while run:
        #run = False
        print("Thesis Time Clock")
        print("1. Clock-in\n2. break-out\n3. break-in\n4. Clock-out\n5. Log Hours\nAnything Else to quit\n")
        choice = input();
        if choice == '1':
            day_heading()
            clock_in()
        elif choice == '2' or choice == '4':
            clock_out()
        elif choice == '3':
            clock_in()
        elif choice == '5':
            log_hours()
        else:
            #run = True
            run = False
    
    
UI()
