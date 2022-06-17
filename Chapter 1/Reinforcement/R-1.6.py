def odd_sum(n):
    
    total = 0
    for i in range(0, n):
        if i % 2 != 0:
            total = total + i ** 2
        else:
            pass
    
    return total
    
print(odd_sum(3))
