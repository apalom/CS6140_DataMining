# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:51:56 2018

@author: Avishan
"""

import math
import csv
import random
import hashlib


def myhash(x,c,d):
	md5 = hashlib.md5(str(hash(x)).encode('utf-8'))
    
	li = []
	for i in range(1,1+d):
		md5.update(str(i).encode('utf-8'))
		li.append(int(md5.hexdigest(), 16) % c + 1)
	return li
	
	
	
def main():
	file1 = open("S1.txt", "r")
	data1 = file1.readline()
	file2 = open("S2.txt", "r")
	data2 = file2.readline()
	Dic1 = {}
	Dic2 = {}
	t = 5
	c  = 10
	for i in range(1,t+1):
		for j in range(1,c+1):
			Dic1[str(i) + '-' + str(j)] = 0
			Dic2[str(i) + '-' + str(j)] = 0
			 
	for x in data1:
		h = myhash(x,c,t)
		for i in range(t):
			Dic1[str(i+1) + '-' + str(h[i])] += 1
	
	for x in data2:
		h = myhash(x,c,t)
		for i in range(t):
			Dic2[str(i+1) + '-' + str(h[i])] += 1
	
	for i in 'abc':
		hs = myhash(i,c,t)
		li = []
		for j in range(t):
			li.append(Dic1[str(j+1)+'-'+str(hs[j])])
		print ('for char = ' + i)
		print (min(li))
	
	for i in 'abc':
		hs = myhash(i,c,t)
		li = []
		for j in range(t):
			li.append(Dic2[str(j+1)+'-'+str(hs[j])])
		print ('for char = ' + i)
		print (min(li))
	
	#target = open('2.txt','w')
	#target.write(str(Dic1))
	#target.write('\n')
	#target.write(str(Dic2))
	#target.write('\n')
	
	
if __name__ == "__main__":
    main()