
zoo_file = open("zoo.csv","rt")

read_zoo = zoo_file.readlines()

water = 0
# total water drinken by elephant
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='elephant'):
        water = water + int(split[2])
        

print 'total water dirnk by elephant is=',water  
zoo_file.close()
water = 0
#total water drinken  by tiger
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='tiger'):
        water = water + int(split[2])
e=0        

print 'total water dirnk by tiger is =',water
water =0
#total water drinken  by zebra
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='zebra'):
        water = water + int(split[2])
e=0        

print 'total water dirnk by zebra is =',water
water =0      
#total water drinken  by lion
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='lion'):
        water = water + int(split[2])
e=0        

print 'total water dirnk by lion is =',water
water =0
#total water drinken  by kangaroo
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='kangaroo'):
        water = water + int(split[2])
e=0        

print 'total water dirnk by kangaroo is =',water

