#Task 2
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

#Task 4
def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
fib_n = fibonacci(n)
print(f"The {n}th element of the Fibonacci sequence is: {fib_n}")