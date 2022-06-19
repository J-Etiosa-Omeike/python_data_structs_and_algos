# non exhaustive list of punctuatation 
punctuatation = [",", '.', '?', '!', "'"]

def remove_punctuation(string: str):
    copy = list(string)
    for idx, character in enumerate(copy):
        if character in punctuatation:
            # strings are immutable, gotta make a list copy
            del copy[idx]
    

    return ''.join(copy)

string = "Hey there, pal!"

print(remove_punctuation(string))