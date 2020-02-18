#!/usr/bin/env python
start=8
to=20
filename=f"../out/repetative{start}-{to}.txt"
cnt=1
with open(filename,"w") as f:
    f.write("1234567890")
    f.write("\n")
    for i in range(8,to+1):
        print(f"Now Generating for {i} series..")
        strz=""
        for z in range (1,i+1):
                strz+=str(z)

        f.write(strz)
        f.write("\n")
        f.write(strz[::-1])
        print("Writing...",strz[::-1])
        f.write("\n")
        revz="0"+strz
        f.write(revz)
        f.write("\n")
        f.write(revz[::-1])
        f.write("\n")
        print("Writing...",revz)
        print("Writing...",revz[::-1])
        cnt+=4
        for k in range(10):
                _=f"{k}"*i
                f.write(_)
                cnt+=1
                f.write("\n")
                print("Writing ...",_)d
print("Total record written..",cnt)
print(f"Done Generating to {filename} .")
input()
        
