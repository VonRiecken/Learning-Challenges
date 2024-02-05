def number(lines):
    index_lines = []
    for index, line in enumerate(lines):
        index_lines.append(f"{index + 1}: {line}")

    return index_lines
