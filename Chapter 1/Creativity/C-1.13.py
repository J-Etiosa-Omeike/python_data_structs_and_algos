def reverse(lst: list):

    length = len(lst)

    for i in range(0, length // 2 ):
        a, b = lst[i], lst[length - 1 - i]
        lst[i] = b
        lst[length - 1 - i] = a

    return lst

lst = [0, 1, 2, 3, 4]

print(reverse(lst))

