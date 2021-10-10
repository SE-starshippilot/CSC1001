import re


class Polynomial:
    def __init__(self, polynomial, letter):
        if polynomial[0] != '-':
            polynomial = '+'+polynomial
        self.__polynomial = polynomial + '-'
        self.__letter = letter

    def __differentiate(self):
        def get_numb(string):
            raw_num = re.findall(r'[0-9\.\+\-]+', string)
            num = '1' if not(raw_num) else raw_num[0]
            if not(re.findall(r'[0-9]', num)):
                num += '1'
            if '.' in num:
                return float(num)
            else:
                return int(num)

        def get_derivative(term):
            tmp = ''
            cef, pwr = map(get_numb, re.split(r'[A-Za-z]', term))
            cef *= pwr
            pwr = 0 if pwr == 1 else pwr - 1
            sgn = '+' if cef >= 0 else ''
            tmp += f'{sgn}'
            if cef != 1:
                tmp += f'{cef}'
            if pwr != 0:
                tmp += f'*{self.__letter}'
                if pwr != 1:
                    tmp += f'^{pwr}'
            return tmp
        bgn, end = 0, 1
        ans = []
        while end < len(self.__polynomial):
            if self.__polynomial[end] in ['+', '-']:
                term = self.__polynomial[bgn:end]
                if self.__letter in term:
                    ans.append(get_derivative(term))
                bgn = end
                end = bgn + 1
            else:
                end += 1
        return ''.join(ans)[1:]

    def __str__(self):
        return self.__differentiate()


def main():
    ipt = input('Please input polynomial:')
    letters = list(set(re.findall(r'[A-Za-z]', ipt)))
    if len(letters) == 1:
        print(Polynomial(ipt, letters[0]))
    elif ipt.isdecimal():
        print('0')


if __name__ == '__main__':
    main()
