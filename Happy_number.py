import math
n = int(input("Inter number: "))
total = 0
result = []
all_numbers = []
def isHappy(n):
    total = 0
    result = []
    all_numbers = []
    while(n >= 1):
        #1 Saving all records to the all_numbers list
        all_numbers.append(n)
        #2 converting to the string format, then using for loop adding as int to the list
        for x in str(n):
            result.append(int(x))
        for number in result:
            total += int(math.pow(number, 2))
        n = total
        result.clear()
        if total == 1:
            return True
        total = 0
        if n in all_numbers:
            return False

print(isHappy(n))