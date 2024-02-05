def create_phone_number(n):
    first = "".join(map(str, n[:3]))
    second = "".join(map(str, n[3:6]))
    last = "".join(map(str, n[-4:]))
    phone_num = f"({first}) {second}-{last}"

    #phone_num = "(" + "".join(map(str, first)) + ")" + " " + "".join(map(str, second)) + "-" + "".join(map(str, last))
    #number = ("({}) {}-{}".format(first, second, last))
    return phone_num


def create_phone_number(n):
    first = n[:3]
    second = n[3:6]
    last = n[-4:]
    phone_num = "(" + "".join(map(str, first)) + ")" + " " + "".join(map(str, second)) + "-" + "".join(map(str, last))
    number = ("({}) {}-{}".format(first, second, last))
    return phone_num

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
