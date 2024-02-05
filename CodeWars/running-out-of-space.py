def spacey(array):
    nospace = [array[0]]
    for i in range(1, len(array)):
        nospace.append(nospace[i - 1] + array[i])
    # print(nospace)
    return nospace
