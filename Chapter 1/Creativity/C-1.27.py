def p_norm(v, p = None):
    norm = 0
    if p is None:
        for val in v:
            norm += val ** 2
        
        return (pow(norm, 1/2))
    
    else:
        for val in v:
            norm += val ** p

        return (pow(norm, 1/p))


print(p_norm([4, 3]))
