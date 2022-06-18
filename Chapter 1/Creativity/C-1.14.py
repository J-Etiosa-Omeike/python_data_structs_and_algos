# inefficient brute force approach -  check each 
# multiple and if we get one odd, return True
def product_odd1(lst):
    for index_i, i in enumerate(lst):
        for index_j, j in enumerate(lst):
            if index_i != index_j:
                if i * j % 2 != 0:
                    return True
    
    return False 

lst = [0, 2]

print(product_odd1(lst))

# more efficient solution: if there is more than 
# odd number in the lst, we know there multiple is odd
# won't work if lst isn't fully integers 
def product_odd2(lst):
    odd_counter = 0

    for i in lst:
        if i % 2 != 0:
            odd_counter = odd_counter + 1
        if odd_counter >= 2:
            return True
    
    return False 
            