def count_vowels_and_consonants(string):
    vowels = 0
    consonants = 0
    for i in string:
        if i in "aeiouAEIOU":
            vowels += 1
        elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants += 1
    print(f"There are {vowels} vowels and {consonants} consonants in the string.")
    return vowels, 
