#!/usr/bin/env python
import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs
import getsize 
url =' https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'
print("Please Enter Values as CircleName operatorName  [t/f](should_null_state_included)")
ins=input().split()

state_to_extract=ins[0].upper() if len(ins)>=1 else None#if set to None all state is considered
telecom_to_extracted=ins[1].upper() if len(ins)>=2 else None #if set to none all operator from particular city is extracted
should_null_state_included=True if len(ins)>=3 and ins[2].lower()=="t" else False #True or False only
stateName="Whole india" if state_to_extract==None else state_to_extract
opName="all_operator" if telecom_to_extracted==None else telecom_to_extracted
nullcheck="WithNull" if should_null_state_included else "WithoutNull"
print(f"currently accessing {stateName} for {opName} {nullcheck}")
print("Connecting...")
response = requests.get(url)
print(response)
soup = bs(response.text,"html.parser")
one_a_tag = soup.findAll('tr')[35:]
lst=[]

for k in one_a_tag:
	s=k.findAll('td')
	limit=len(s)
	i=0
	while True:
		if i==limit:
			break
		
		no=s[i].text
		i+=1
		if i==limit:
			break
		operator=s[i].text
		i+=1
		if i==limit:
			break
		state=s[i].text
		i+=1
		if i==limit:
			break

		res=f"{no} {operator} {state}"

		if state_to_extract is  None :
			if telecom_to_extracted is None:
				if should_null_state_included:
					if len(state)!=2:
						lst.append(no) #all india all operator only where no state value present
				else:
					pass # all india all operator all no 
			elif telecom_to_extracted in res:
					lst.append(no)
			else:
				print("please specify either state or operator or both")
				input()
				break
		elif state_to_extract in res:
			if telecom_to_extracted is None:
				lst.append(no)
			elif telecom_to_extracted in res :
					lst.append(no) #inteded operator of intended state found
			else:
				pass
				#currently not the intended operator

		elif should_null_state_included:
			if telecom_to_extracted is None:
				if len(state)!=2:
					lst.append(no)
			elif telecom_to_extracted in res:
					if len(state)!=2:
						lst.append(no)
			else:
				pass #not desired telcom op
		else:
			pass
			#currently not the desired State...



filename=f"../out/{stateName}_{opName}-{nullcheck}.txt"
lst.sort()
cnt=0
with open(filename,"w") as f:
	for z in lst:
		if len(z)==4:
			print(f"writing {z} to file",end="\r")
			f.write(z)
			cnt+=1
			f.write("\n")
size_bytes=(cnt*5)+1
getsize.printSize(size_bytes)
print(f"\nwritten total {cnt} Series to {filename}\n\n")
time.sleep(5)
 