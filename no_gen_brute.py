#!/usr/bin/env python
import os
import getsize
import time
o=os.popen(" ls ../out/*.txt")
output=o.read()
lst=list(output.split("\n"))
lst.sort(key=str.lower)
for k in range(len(lst)):
	if ".txt" in lst[k]:
		print(f"{k} {lst[k][7:]}")

print("\n\n")
print("Please Enter the No of the file\nfor which you want to brute_force gen>",end="")
option=int(input())
selectedFile=lst[option]
print("selected file=",selectedFile)
lst_series=[]
with open("../out/"+selectedFile,"r") as f:
	for k in f:
		if len(k)==5:
			lst_series.append(k[:-1])#append to list
lst_series.sort()#sort the list

dicsize={}
for z in lst_series:
	dicsize[z[0]]=dicsize.get(z[0],0)+1
cnt=0
prev="-"
for k in lst_series:

	if prev!=k[0]:
		if prev!="-":
			print(f"Done Writing to {gen_file_name} for {k[0]} series\n\n")
		time.sleep(1)
		print(f"\t\t\aNow Generating for {k[0]} series")
		print("-"*50)
		u,s=getsize.getSizeDecimal((((dicsize[k[0]])*(10**6))*11)+1)
		print(f"For {k[0]} series FileSize will Be :{s} {u}")
		print("-"*50)
		mode="w"
		time.sleep(1)
		cnt=1
	else:
		mode="a"
		cnt+=1
	print(f"\t\tWriting {cnt}/{dicsize[k[0]]} for {k[0]} Series")
	gen_file_name="Series "+k[0]+" "+selectedFile[7:-4]+".dictxt"
	with open("../out/"+gen_file_name,mode) as genf:
		for qqq in range(10**6):
			s=str(qqq)
			l=len(s)
			if l<6:
				s=k+"0"*(6-l)+s
			else:
				s=k+s
			print(f"Writing \t{s} ",end="\r")
			genf.write(s)
			genf.write("\n")
	print(f"->                         written {cnt}/{dicsize[k[0]]} for {k[0]}                            ")
	prev=k[0]		
print(f"\n\nDONE WRITING FOR FILE {selectedFile[7:]} ")

print(f"\nTotal Record Writen = {(len(lst_series))*(10**6)}")

getsize.printSize((((len(lst_series))*(10**6))*11)+1)

time.sleep(5)
			
		