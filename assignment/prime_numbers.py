#looping
count = 2
while(count < 100):
    x = 1
    while x < count:
        x =x + 1
        if(count % x)==0:
            break
    if x == count:
        print count
    count = count + 1
