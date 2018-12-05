numbers = list(input("Enter numbers with comma seprated:"))
max1 = max(numbers)
min1 = min(numbers)
numbers.remove(max1)
numbers.remove(min1)
sum1=sum(numbers)
count = len(numbers)
print sum1/count
