def reverse(lst: list):

    length = len(lst)

    a, b = lst[0], lst[-1]
    lst[0] = b
    lst[-1] = a

    for i in range(1, length // 2 - 1 ):
        a, b = lst[i], lst[-i]
        lst[i] = b
        lst[-i] = a

    return lst

lst = [0, 1, 2, 3]

print(reverse(lst))

