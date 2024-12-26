"""i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1
count = 0
while count < 100:
    print(count)
count = 0
while count < 100:
    count += 1
number = eval(input("Enter an integer: "))
max = number
while number != 0:
    number = eval(input("Enter an integer: "))
    if number > max:
        max = number
print("max is", max)
print("number", number)
number = 0
sum = 0
for count in range(5):
    number = eval(input("Enter an integer: "))
    sum += number
print("sum is", sum)
print("count is", count+1)
sum=0
i=0
while i<=1000:
    sum= sum+i
    i=i+1
print(sum)
sum = 0
for i in range(1001):
    sum = sum + i
print(sum)
sum=0
for i in range(10001):
    sum=sum+i
print(sum)

print(" Multiplication Table")
print("|", end="")
for j in range(1,11):
    print("",j,end='')
print()
print("——————————————————————————————————————————")
for i in range(1,11):
    print("|",end="")
    for j in range(1,11):
        print(i*j, end="")
    print()
for i in range(1, 5):
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1   
i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end = " ")
    print("****")
    i += 1"""
i = 5
while i >= 1:
    num = 1
    for j in range(1, i + 1):
        print(num, end = "xxx")
        num *= 2
    print()
    i -= 1




    