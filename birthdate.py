years=[1980,1981]
import time
month=[31,29,31,30,31,30,31,31,30,31,30,31]
filename="../out/birthdays.dictxt"
with open(filename,"w") as f:
	for year in range(years[0],years[1]+1):
		for mnth in range(12):
			for days in range(1,month[mnth]+1):

				lst=[]
				daystr="%02d"%(days)
				mnthstr="%02d"%(mnth+1)
				yearstr="%04d"%(year)
				lst.append(f"{daystr}{mnthstr}{yearstr}")
				lst.append(f"{yearstr}{mnthstr}{daystr}")
				lst.append(f"{yearstr}{daystr}{mnthstr}")
				lst.append(f"{daystr}{yearstr}{mnthstr}")
				lst.append(f"{mnthstr}{daystr}{yearstr}")
				lst.append(f"{mnthstr}{yearstr}{daystr}")
				for strz in lst:
					f.write(strz)
					f.write("\n")
					print(f"Writing {strz}",end="\r")


print("\nWritten to ",filename)
time.sleep(3)


