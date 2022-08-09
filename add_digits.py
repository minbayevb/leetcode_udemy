num = int(input("Inter number please: "))

print(len(str(num)))
while(len(str(num)) != 1):
    total = 0
    for x in str(num):
        total += int(x)
    num = total
print(num)