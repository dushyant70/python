import hashlib
import os
import csv

with open('zoo.csv') as read_zoo:
    read_zoo = csv.reader(read_zoo,delimiter=',')
    
    for i in read_zoo:
        print hashlib.sha1(i[2])
