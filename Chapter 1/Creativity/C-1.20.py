from random import randint


def shuff(lst):
    for i in range(0, len(lst)):
        n = randint(0, len(lst) - 1)
        a, b = lst[i], lst[n]
        lst[i] = b
        lst[n]= a
     
    return lst


lst = [i for i in range(0, 10)]

print(shuff(lst))


