def most_frequent(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = 0
    most_common_num = None
    for num, f in freq.items():
        if f > max_freq:
            max_freq = f
            most_common_num = num
        elif f == max_freq:
            most_common_num = min(most_common_num, num)
    return most_common_num
numbers = [1, 2, 3, 2, 2, 4, 5, 4, 4, 4]
print(most_frequent(numbers))
