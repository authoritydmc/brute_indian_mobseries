#!/usr/bin/env python
import getsize
import time
start=8
to=10
filename=f"../out/repetative{start}-{to}.dictxt"
cnt=1
total_bytes=12
with open(filename,"w") as f:
    f.write("1234567890")
    f.write("\n")
    for i in range(start,to+1):
        print(f"Now Generating for {i} series..",end="\r")
        strz=""
        for z in range (1,i+1):
                strz+=str(z)
        f.write(strz)
        f.write("\n")
        f.write(strz[::-1])
        print("Writing...",strz,end="\r")
        print("Writing...",strz[::-1],end="\r")
        f.write("\n")
        revz="0"+strz
        f.write(revz)
        f.write("\n")
        f.write(revz[::-1])
        f.write("\n")
        print("Writing...",revz,end="\r")
        print("Writing...",revz[::-1],end="\r")
        total_bytes+=(len(strz)+1)*2+(len(strz)+2)*2
        cnt+=4
        for k in range(10):
                _=f"{k}"*i
                f.write(_)
                cnt+=1
                f.write("\n")
                total_bytes+=len(_)+1
                print("Writing ...",_,end="\r")
print(" "*((to-start)+40))
print("Total record written..",cnt)
print(f"Done Generating to {filename}")
getsize.printSize(total_bytes)
time.sleep(5)
        
