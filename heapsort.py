#!/usr/bin/env python2
#
# $Id: heapsort.py,v 0.37 2017/10/31 15:19:21 kc4zvw Exp kc4zvw $

# Favorite:
#  I am trying to figue out how to make the following Code for Heap
#  sort work with many data types:

import os

def swap(i, j):                    
	wordlist[i], wordlist[j] = wordlist[j], wordlist[i] 

def heapify(end, i):   
	l = 2 * i + 1  
	r = 2 * (i + 1)   
	max = i   
	if l < end and wordlist[i] < wordlist[l]:   
		max = l   
	if r < end and wordlist[max] < wordlist[r]:   
		max = r   
	if max != i:   
		swap(i, max)   
		heapify(end, max)   

def heapsort():     
	end = len(wordlist)   
	start = end // 2 - 1 # use // instead of /
	for i in range(start, -1, -1):   
		heapify(end, i)   
	for i in range(end-1, 0, -1):   
		swap(i, 0)   
		heapify(i, 0)   
	return wordlist

### ====================================================================

def get_home_directory():
	home = os.getenv("HOME")
	print("My home directory is %s" % home)
	return home

def print_header(str):
	n = len(str)
	print("\n" + ' ' + str)
	print('-' * (n + 2))

def open_text_file():
    
	myHome = get_home_directory()
	text_file = myHome + os.sep + 'alphabet.txt'
	words = []

	print("Reading text file : %s" % text_file)

	f = open(text_file, 'r')

	for a in f.readlines():
		a = a.rstrip("\n")
		words.append(a)
		#print("%s" % a)

	f.close()

	return words

### ====================================================================

numlist = [2, 7, 1, -2, 56, 5, 3]

print_header("Numbers listing:")
for num in numlist:
	print("%10d" % num)

wordlist = numlist
listing = heapsort()

print_header("Sorted numbers:")
for num in listing:
	print("%10d" % num)
print("\n")

### ====================================================================

''' Main Program '''

del wordlist[:]

chars = ['z', 'x', 'a', 'c', 'r', 'd', '3']

print_header("Character listing:")
for char in chars:
	print("%9c" % char)

wordlist = chars
listing = heapsort()

print_header("Sorted character listing:")
for char in listing:
	print("%9c" % char)
print("\n")

### ====================================================================

unsorted = []
unsorted = open_text_file()

print_header("Unsorted word listing:")
for word in unsorted:
	print("   %s" % word)

wordlist = unsorted
listing = heapsort()

print_header("Sorted word listing:")
for word in listing:
	print("   %s" % word)

# End of script
