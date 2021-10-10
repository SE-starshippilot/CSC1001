def sqrt(ini, n):
    aft = (ini + (n / ini)) / 2
    if abs(ini - aft) < 1e-10:
        return aft
    return sqrt(aft, n)


def get_input():
    while True:
        try:
            temp = float(input('Please input a positive number:'))
            if temp <= 0:
                raise ValueError
        except ValueError:
            print('The input is invalid!')
        else:
            return temp


ques = get_input()
print(f'The square root of {ques} is {sqrt(3, ques):.9f}')
