if __name__ == '__main__':
    n = int(input())
    while n < 1 and n > 20:
        print("Constraint: 1 <= n <= 20")
        n = int(input())

    n2 = 0
    for i in range(n):
        n2 = i ** 2
        print(n2)
