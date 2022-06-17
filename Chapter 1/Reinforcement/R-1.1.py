from tokenize import Triple


def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

n = 10
m = 3

print(is_multiple(n , m))