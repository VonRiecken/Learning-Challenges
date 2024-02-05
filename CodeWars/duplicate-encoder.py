def duplicate_encode(word):
    print(word)
    W = word.lower()[:]
    new = ""
    char_count = {}
    for char in W:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)
    for char in W:
        if char_count[char] > 1:
            new += ")"

        else:
            new += "("

    print(new)
    return new
