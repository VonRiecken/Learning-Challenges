if __name__ == '__main__':
    N = int(input())

    newlist = []

    for i in range(N):
        given_command = (input())
        cmd = given_command.split()
        command = cmd[0]
        first = int(cmd[1]) if len(cmd) > 1 else 1
        second = int(cmd[2]) if len(cmd) > 2 else 1

        if command == "insert":
            newlist.insert(first, second)
        elif command == "print":
            print(newlist)
        elif command == "remove":
            newlist.remove(first)
        elif command == "append":
            newlist.append(first)
        elif command == "sort":
            newlist.sort()
        elif command == "pop":
            newlist.pop()
        elif command == "reverse":
            newlist.reverse()
        else:
            print("Command not found")
            continue







    # print(newlist)
