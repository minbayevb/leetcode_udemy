from collections import Counter
from operator import le
numbers = [1, 5, 5, 4, 1, 8, 11, 2, 22, 3, 21]

# counts = Counter(numbers)
# print(max(counts.keys(), key = counts.get))
# print(max(counts.keys(), key = counts.get))
# def highest_num(numbers):
#     for i in range(len(numbers) - 1):
#         if numbers[i - 1] < numbers[i] >  numbers[i + 1]:
#             return numbers[i]

# print(highest_num(numbers))

L = ['hi', 'Bula', 'fdfs', 'fsldfknsdlf']
def get_words_from_line_list(L):
    """
    Parse the given list L of text lines into words.
    Return list of all words found.
    """
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list = word_list + words_in_line
    return word_list

print(get_words_from_line_list(L))
