from json import tool
import string 

letters = input("inter sum letters: ")
# Converts letters to the numbers and concatenates them
def converter(letters):
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    all_numbers = []
    for letter in letters:
        all_numbers.append(str(alphabet_list.index(letter) + 1))
    s = "".join(all_numbers)
    return s

def transform(s):
    k = int(input("how many times it should sum up? "))
    y = 0
    while(y != k):
        y += 1
        total = 0
        for number in str(s):
            total += int(number)
        s = total
    return total

s = converter(letters)
print(transform(s))

# Solution from Leetcode 
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        all_numbers = []
        for letter in s:
            all_numbers.append(str(alphabet_list.index(letter) + 1))
        s = "".join(all_numbers)
        y = 0
        while(y != k):
            y += 1
            total = 0
            for number in str(s):
                total += int(number)
            s = total
        return total
