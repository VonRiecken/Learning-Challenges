def even_chars(st):
    arr = []
    if 1 < len(st) < 101:
        for i in range(1, len(st), 2):
            arr.append(st[i])
        return arr
    else:
        return "invalid string"
