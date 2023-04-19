def unique_list(lst):
    unique_lst = [lst[0]]
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

