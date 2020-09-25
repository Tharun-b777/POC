#!/usr/bin/env python3
import csv
attendees={}
print("Enter the end time of class in hh:mm:ss ")
h,m,s=input().split(":")
h,m,s=int(h),int(m),int(s)
h*=3600
m*=60
end_time=h+m+s
# end_time=4*3600+30*60
duration=float(input("Enter minimum duration to be attended "))
with open('attendance.csv', encoding='utf-16le') as f:
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
            else:
                attendees[l[0]]-=total_time
                

        else:
            attendees[l[0]]=total_time
            attendees[l[0]]=end_time -attendees[l[0]]
for key in attendees:
    if float(attendees[key]/60) > (duration):
        print(str(key)+"\t\t"+str(float(attendees[key]/60)))

        
