def split_the_bill(x):
    total = sum(x.values())
    average = total / len(x)

    for key, value in x.items():
        x[key] = round(value - average, 2)


#     print(x)
    return x
