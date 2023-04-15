def sort_by_age(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
    return sorted_list
list_of_tuples = [('Yevhen', 44), ('Maria', 7), ('Ivan', 7)]
sorted_list = sort_by_age(list_of_tuples)
print(sorted_list)
