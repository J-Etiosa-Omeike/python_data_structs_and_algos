# probably not the most efficient solution -- repeatedly generates random copies to get all possible permutations -- probably a more systematic way of doing this 
lst = ['c', 'a', 't', 'd', 'o']

from math import factorial
import random

def all_possible_strings(lst):
    string = "".join(lst.copy())
    dct = {}
    dct[string] = 0
    to_return = []
    to_return.append(string)
    length = 1
    poss_permutations = factorial(len(lst))


    while length != poss_permutations:
        random.shuffle(lst)
        copy = lst.copy()
        string = "".join(copy)
        if string not in dct.keys():
            dct[string] = 0
            length += 1
            to_return.append(string)


    
    return to_return

print(all_possible_strings(lst))
        
