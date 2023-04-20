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

# Task 6
def scalar_product(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The two lists must have the same length.")

    return sum([list1[i] * list2[i] for i in range(len(list1))])
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = scalar_product(list1, list2)
print(result)

#Task 8
def sort_by_age(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
    return sorted_list
list_of_tuples = [('Yevhen', 44), ('Maria', 7), ('Ivan', 7)]
sorted_list = sort_by_age(list_of_tuples)
print(sorted_list)