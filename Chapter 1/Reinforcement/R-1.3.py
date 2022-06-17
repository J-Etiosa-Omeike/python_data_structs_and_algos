def minmax(data):
    min = data[0]
    max = data[0]

    for number in data:
        if number > max:
            max = number
        
        if number < min:
            min = number

    return max, min

lst = range(0, 100)

a, b = minmax(lst)

print(a, b)