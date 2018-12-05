# open, read file from python
my_file = open("D:\\a.txt","rt")

# print my_file
print (my_file)

#read my_file
read_file = my_file.readline()

print (read_file)

my_file.close()

#read all data in list

my_file = open("D:\\a.txt","rt")

read_file = my_file.readlines()

print (read_file)

my_file.close()



