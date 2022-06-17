def one_liner(n):

    return sum([i ** 2 if i % 2 != 0 else 0 for i in range(0, n)])

