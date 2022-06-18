def dot_prod(a, b):
    sum = 0
    # zip returns an iterator of tuples
    for i, j in zip(a, b):
        sum += i * j
    
    return sum

a = [1, 2, 3]
b = [1, 2, 3]

print(dot_prod(a, b))

