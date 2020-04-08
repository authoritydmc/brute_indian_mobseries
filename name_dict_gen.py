#!/usr/bin/env python
import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup as bs
import getsize 
baseurl ='http://www.20000-names.com/'  #sample url http://www.20000-names.com/male_a_names_2.htm
gender="male" #male or female
urllist=[]
print("PATH:",__file__)
alphabets=list("a")
for i in range(len(alphabets)):
	url=baseurl+gender+"_"+alphabets[i]+"_names"
	urllist.append(url)
print("_"*40)

for url in urllist:
	maxurl=2
	adder=""
	for i in range(1,maxurl):
		if i>1:
			adder="_"+str(i)
		finalurl=url+adder+".htm"
		print(finalurl)
		print("Connnecting ...")
		#finalurl .... 
		try:
			response=requests.get(finalurl)
			print(response,finalurl)
			soup=bs(response.content,'html.parser')
			# print(soup.prettify())
			# print(list(soup.children)[20])
			# input()
			nvnv=0

			with open("dump_data.txt","a") as f:
				for k in list(soup.children):
					print("------",nvnv,k,".....",nvnv)
					nvnv+=1
					strz=f"\n------{nvnv}{k}.....{nvnv}\n"
				f.write(strz)
				print("Writeten to file")
		except Exception as err:
			print("some error ",err)


		input()



# lst=["raj","aman","vishal"]

# filename=f"../out/name_dict_indian.txt"
# lst.sort()

# if len(lst)==0:
# 	print("NO name Found\nExiting ")
# 	time.sleep(3)
# 	exit()
# """initialize count variables"""
# size_bytes=0
# cnt=0
# combos=["123","1234","12345","123456","12345678"]
# for combo in combos:
# 	if combo==combos[0]:
# 		mode="w"
# 	else:
# 		mode="a"
# 	with open(filename,mode) as f:
# 		for z in lst:
# 				print(f"writing {z} to file",end="\r")
# 				str1=combo+z
# 				if len(str1)>=8:
# 					f.write(str1.upper())
# 					f.write("\n")
# 					f.write(str1.lower())
# 					f.write("\n")
# 					cz=combo+z.capitalize()
# 					f.write(cz)
# 					f.write("\n")
# 					str2=z+combo
# 					f.write(str2.upper())
# 					f.write("\n")
# 					f.write(str2.lower())
# 					f.write("\n")
# 					f.write(str2.capitalize())
# 					f.write("\n")
# 					size_bytes+=(6*((len(z)+len(combo)+1)))
# 					cnt+=6

# getsize.printSize(size_bytes)
# print(f"\nwritten total {cnt} Series to {filename}\n\n")
# cnt=0
# time.sleep(5)
#  