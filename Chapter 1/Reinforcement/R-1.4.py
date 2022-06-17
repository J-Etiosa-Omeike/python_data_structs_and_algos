def sumSquares(n):
    total = 0
    
    for integer in range(1, n):
        
        total = total + (integer ** 2)
    
    return total

total = sumSquares(1)
print(total)