def queue_time(customers, n):
    if len(customers) <= n and len(customers) != 0:
        return max(customers)
    if len(customers) == 0:
        return 0

    till = 1
    dict = {}
#     create dict for each til
    for _ in range(n):
        dict['till_'+str(till)] = []
        till += 1

#     assigning customers to tills
    till = 1
    next_till = till + 1
    for i in range(len(customers)):
        till_total = {key: sum(times) for key, times in dict.items()}
        least_till_key = min(till_total, key=till_total.get)
        dict[least_till_key].append(customers[i])

        max_time = max(sum(values) for values in dict.values())

    return max_time

print(queue_time([1, 2, 3, 4], 3))
