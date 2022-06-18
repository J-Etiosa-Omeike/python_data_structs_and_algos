def count_vowels(string):
    count = 0

    for character in string:
        if character in ('a', 'e', 'i', 'o', 'u'):
            count += 1
        
    return count

string = "abcdefghijklmnop"

print(count_vowels(string))
