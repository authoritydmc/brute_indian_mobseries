#!/usr/bin/env python
import os
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
cnt_rec=0
with open("../out/"+selectedFile,"r") as f:
	prev="1"
	for k in f:
		cnt_rec+=1
		print("Current k",k,len(k))
		if len(k)==5:
			num=k.replace("\n","")
			if prev!=k[0]:
				print(f"Now Generating for {k[0]} series")
				mode="w"
			else:
				mode="a"
			file_z=selectedFile[7:-4]
			gen_file_name="Series "+k[0]+" "+file_z+".dictxt"
			with open("../out/"+gen_file_name,mode) as genf:
				for qqq in range(10**6):
					s=str(qqq)
					l=len(s)
					if l<6:
						s=num+"0"*(6-l)+s
					else:
						s=num+s
					print(f"Writing \t{s} ")
					genf.write(s)
					genf.write("\n")
		prev=k[0]		
print(f"done writing for {selectedFile[7:]} ")
print(f"Total Record Wriiten = {(cnt_rec)*(10**6)} for {cnt_rec} series")
input()
			
		