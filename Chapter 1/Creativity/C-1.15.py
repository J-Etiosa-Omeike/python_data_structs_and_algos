def distinct(lst):
    dct = {}
    for i in lst:
        if i in dct.keys():
            return False
        else:
            dct[i] = 0

    return True

lst = [0, 1, 1]

print(distinct(lst))
