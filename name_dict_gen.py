#!/usr/bin/env python
import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs
import getsize 
url =' https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'


lst=["raj","aman","vishal"]

filename=f"../out/name_dict_indian.txt"
lst.sort()

if len(lst)==0:
	print("NO name Found\nExiting ")
	time.sleep(3)
	exit()
"""initialize count variables"""
size_bytes=0
cnt=0
combos=["123","1234","12345","123456","12345678"]
for combo in combos:
	if combo==combos[0]:
		mode="w"
	else:
		mode="a"
	with open(filename,mode) as f:
		for z in lst:
				print(f"writing {z} to file",end="\r")
				str1=combo+z
				if len(str1)>=8:
					f.write(str1.upper())
					f.write("\n")
					f.write(str1.lower())
					f.write("\n")
					cz=combo+z.capitalize()
					f.write(cz)
					f.write("\n")
					str2=z+combo
					f.write(str2.upper())
					f.write("\n")
					f.write(str2.lower())
					f.write("\n")
					f.write(str2.capitalize())
					f.write("\n")
					size_bytes+=(6*((len(z)+len(combo)+1)))
					cnt+=6

getsize.printSize(size_bytes)
print(f"\nwritten total {cnt} Series to {filename}\n\n")
cnt=0
time.sleep(5)
 