def is_uppercase(inp):
    for char in inp:
        if char.islower():
            return False
    return True
