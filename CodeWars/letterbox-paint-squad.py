def paint_letterboxes(start, finish):
    digits_count = [0] * 10

    for i in range(finish - start + 1):
        letterbox = str(start + i)
        for digit in letterbox:
            digits_count[int(digit)] += 1

    print(digits_count)
    return digits_count
