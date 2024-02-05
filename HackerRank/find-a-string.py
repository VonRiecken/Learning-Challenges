def count_substring(string, sub_string):
    count = 0
    for char in range(len(string) - len(sub_string) + 1):
        if string[char:char + len(sub_string)] == sub_string:
            count += 1
    return count
