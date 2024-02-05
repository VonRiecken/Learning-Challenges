def digital_root(n):
    x = Sum(n)
    root = x.sum_digits(n)
    return root


class Sum(object):
    def __init__(self, number):
        self.number = number
        self.run_sum = 0


    def sum_digits(self, num):
        for dig in str(num):
            self.run_sum += int(dig)
        num = self.run_sum
        self.run_sum = 0
        return num if num < 10 else Sum(num).sum_digits(num)
