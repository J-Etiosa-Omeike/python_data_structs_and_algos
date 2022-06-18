def write(lst, idx, val):
    try:
        lst[idx] = val
    except:
        print("Don't try buffer overflow attacks in Python!")