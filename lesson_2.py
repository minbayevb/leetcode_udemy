# def powerOfTwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerOfTwo(n - 1)
#         return power * 2


# print(powerOfTwo(n = 2))
# ex_1
# def ex_1(word):
#     if len(word) == 1 or len(word) == 2:
#         return word
#     return word[0] + '(' + ex_1(word[1:-1]) + ')' + word[-1]

# word = input('please write some word: ')

# print(ex_1(word))

# ex_2

def ex_2(word):
    if len(word) == 1:
        return word
    return word[0] + "*" + ex_2(word[1:-1]) + "*" + word[-1]

word = input("please enter a word: ")
print(ex_2(word))
