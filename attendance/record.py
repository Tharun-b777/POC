#!/usr/bin/env python3
import csv
attendees={}
present={}
def parser(f):
    line=csv.reader(f,delimiter='\t',)
    next(line)
    for l in line:
        h, m, s = l[2].split(',')[1].split(':')
        s=s.split(" ")[0]
        h,m,s=int(h),int(m),int(s)
        h*=3600
        m*=60
        total_time=h+s+m
        if l[0] in attendees.keys():
            if l[1] == "Joined":
                attendees[l[0]]+=total_time
                del present[l[0]]
            else:
                attendees[l[0]]-=total_time
                present[l[0]]=attendees[l[0]]
        else:
            attendees[l[0]]=total_time
            attendees[l[0]]-=end_time
    for key in attendees:
        if key in present.keys():
            attendees[key]+=end_time
        if float(-attendees[key]/60) >= (duration):
            print("{} {}".format(key,-attendees[key]/60))
if __name__ == "__main__":
    print("Enter the end time of class in hh:mm:ss ")
    time = input().split(":")
    h, m, s = map(lambda x: int(x), time)
    h *= 3600
    m *= 60
    end_time = h+m+s
    # end_time=3*3600+30*60
    duration = float(input("Enter minimum duration to be attended "))
    # duration=55.00
    with open('attendance.csv', encoding='utf-16le') as f:
        parser(f)
