# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:06:09 2018

@author: Avishan
"""

def MG(D,c,k):
	MG(Dic1, i, 9)

for i in data1:
	if (c in D):
		D[c]+=1
	elif (len(D) < k):
		D[c] = 1
	else:
		d = ''
		for key,val in D.items():
			if(val == 0):
				d = key
		if (d != ''):
			del D[d]
			D[c] = 1
		else:
			for key,val in D.items():
					D[key] -= 1
		d = ''
	
	
def main():
	file1 = open("S1.txt", "r")
	data1 = file1.readline()
	file2 = open("S2.txt", "r")
	data2 = file2.readline()
	Dic1 = {}
	Dic2 = {}
	print (len(data1))
	print (len(data2))
	for i in data1:
		MG(Dic1,i,9)
	for i in data2:
		MG(Dic2,i,9)
		
	acount1 = 0
	acount2 = 0
	for i in data1:
		if(i == 'c'):
			acount1 += 1
	#for i in data2:
	#	if(i == 'c'):
	#		acount2 += 1
			
	#print acount1
	#print acount2
	print (Dic1)
	print (Dic2)
	
	target = open('1.txt','w')
	target.write(str(Dic1))
	target.write('\n')
	target.write(str(Dic2))
	target.write('\n')
	
	
	
	
if __name__ == "__main__":
    main()