def first_last_three_chars(s):
    if len(s) < 6:
        return "nedostatnyo symbols"
    else:
        return s[:3] + s[-3:]

s = "Nvidia Geforce"
print(first_last_three_chars(s)) 
