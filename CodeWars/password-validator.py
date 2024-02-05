def password(string):
    upper = False
    lower = False
    digit = False
    length = False

    for char in string:
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
        if char.isdigit():
            digit = True
        if len(string) >= 8:
            length = True

    if upper and lower and digit and length:
        return True

    return False
