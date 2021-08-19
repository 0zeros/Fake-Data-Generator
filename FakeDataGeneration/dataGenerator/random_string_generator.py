import random


# take length of string as parameter
# had a list of all alphabets
# randomly choose alphabets and make string by joining them
def string_of_length(length):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    str1 = ""
    return str1.join(random.choices(alphabets, k=length))
