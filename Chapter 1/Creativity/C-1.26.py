# nonextensive, but the general idea is right
# wonder if there's a faster way to do this
def check_math(a, b, c):
    if a + b == c:
        return "a + b = c"
    if a == b + c:
        return "a = b + c"
    if a * b == c:
        return "a * b = c"
    if a == b * c:
        return "a = b * c"
    if a / b == c:
        return "a / b = c"
    if a == b / c:
        return "a = b / c"
    if a - b == c:
        return "a - b = c"
    if a == b - c:
        return "a = b - c"
    
