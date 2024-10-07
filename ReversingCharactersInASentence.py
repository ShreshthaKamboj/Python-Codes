import re
def reverse_chars():
    string = "Hello Guys"
    words_list = re.split(r'\s+', string)
    reversed_words = words_list[::-1]
    print(' '.join(reversed_words))
reverse_chars()