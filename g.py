
Locate.py
import os
import re
import sys
from datetime import datetime
 
response = os.popen(wmic logicaldisk get caption)
list1 = []
for line in response.readlines():
line = line.strip(\n)     # this line strip the \n
line = line.strip(\r)  # this line strip the \r means carriage return
line = line.strip( )  # use to strip blank space
if (line == Caption or line == ):  # if caption and  appears this line ignore
continue
list1.append(line)  # list1 now contain all drives of windows
a = \\
def search1(list1):
tf = 0
td = 0
for each in list1:      # take each drive one by one
print In , each
for root, dir, files in os.walk(each, topdown = True):   # this line return the root dir (means start from drive),  sub driectory and files in the root dir
for file in files:    # start search from files
if re.search(sys.argv[1].lower(), file.lower()):  # this line match the substring given in command line argument with files one by one
print root+a+file # if match found then make a path to print
tf = tf+1 # to count the files
for d in dir:
if re.search(sys.argv[1].lower(), d.lower()):  # this line for directories
print root+a+d  #print the path
td = td+1 # print the number of dirs matched
print Total File(s) are , tf
print Total Directores are , td
print \nThank you for using l4wisdom.com\n
 
t1= datetime.now()
search1(list1)   # call the function.
t2= datetime.now()
total =t2-t1  # to calculate the total time taken in process
print Searchingcompleted in  , total
