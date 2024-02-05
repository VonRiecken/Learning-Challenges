def find_it(seq):
    counter = {}
    for char in seq:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    for key in counter:
        if counter[key] % 2 != 0:
            print(key)
            return key

    return None
