def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not(n % i):
            return False
    else:
        return True


def emirp(n):
    rev = int(str(n)[::-1])
    return True if all([prime(n), prime(rev), n != rev]) else False


def print_emirp(target_list):
    result = ''
    for index, num in enumerate(target_list, 1):
        result += f'{num:<5}\t'
        if not(index % 10):
            result += '\n'
    print(result)


def find_emirp():
    list_of_emirp = []
    num = 13
    while len(list_of_emirp) != 100:
        if emirp(num):
            list_of_emirp.append(num)
        num += 1
    return list_of_emirp


answer_list = find_emirp()
print_emirp(answer_list)
