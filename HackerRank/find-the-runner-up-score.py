if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newlist = list(arr)
    newlist.sort(reverse = True)

    for score in newlist:
        if score != newlist[0]:
            print(score)
            break
