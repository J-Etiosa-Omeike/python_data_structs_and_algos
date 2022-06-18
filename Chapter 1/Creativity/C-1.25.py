punctuatation = [",", '.', '?', '!', "'"]
def remove_punctuation(string):
    for idx, character in enumerate(string):
        if character in punctuatation:
            # strings are immutable, gotta make a list copy
            del string[idx]
    
    return string

string = "Hey there, pal!"

print(remove_punctuation(string))