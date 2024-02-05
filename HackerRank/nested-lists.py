if __name__ == '__main__':
    n = int(input())
    while n < 1 and n > 5:
        n = int(input())

    records = []
    for _ in range(n):
        name = input()
        score = float(input())
        result = []
        result.append(name)
        result.append(score)
        records.append(result)
        # print(records)


    sorted_records = sorted(records, key=lambda x: x[1])

    # find second least
    distinct_scores = []
    for i in range(len(sorted_records)):
        if sorted_records[i][1] not in distinct_scores:
            distinct_scores.append(sorted_records[i][1])



    to_print = []
    # to_print.append(sorted_records[1][0]))
    for i in range(len(sorted_records)):
        if sorted_records[i][1] == distinct_scores[1]:
            to_print.append(sorted_records[i][0])

    for name in sorted(to_print):
        print(name)
