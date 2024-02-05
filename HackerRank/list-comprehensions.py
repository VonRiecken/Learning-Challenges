if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    array = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if sum([i, j, k]) != n]

    # newlist = [sublist for sublist in array if sum(sublist) != n]

    print(array)
