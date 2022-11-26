# Python Project-11
# Group's members details:
#    Name             Registration No.    Batch        Roll.no
# 1. Nikhil Raj        12221212           koc07          34
# 2. Mehul Anand       12220251           koc07          33
# 3. Narendran R       12220680           koc07          35


import random
a = int(input("Enter the starting range : "))
b = int(input("Enter the end range : "))
num1 = random.randint(a, b)
c = str(a)
d = str(b)
print("Range is" + " (" + c + "," + d + ")", "and randomly picked number is", num1)
print("Then the properties followed by this number are :")
if num1 > 0:
    print(num1, "is a positive number")
elif num1==0:
    print(num1,"is neither positive nor negative")
else:
    print(num1, "is a negative number")

if num1 % 2 == 0:
    print(num1, "is an even number")
else:
    print(num1, "is an odd number")

if num1 > 1:
    for i in range(2, num1):
        if (num1 % i) == 0:
            print(num1, "is a composite number")
            break
    else:
        print(num1, "is a prime number")

elif num1 == 0 or num1 == 1:
    print(num1, "is neither prime nor composite")
else:
    print(num1, "is negative number ,so this is composite Number")



