import requests
import urllib.request
import time
from bs4 import BeautifulSoup as bs
import re
url =' https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'
state_to_extract="UE" #if set to None all state is considered
telecom_to_extracted=None #if set to none all operator from particular city is extracted

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
				lst.append(no)
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

		else:
			pass
			#currently not the desired State...

		print(res)

		print("-"*20)
print(lst)
stateName="india" if state_to_extract==None else state_to_extract
opName="all_operator" if telecom_to_extracted==None else telecom_to_extracted
filename=f"{stateName}__{opName}.txt"
lst.sort()
with open(filename,"w") as f:
	for z in lst:
		if len(z)==4:
			print(f"writing {z} to file")
			f.write(z)
			f.write("\n")



 