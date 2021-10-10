def isValid(number):
    if number.isnumeric():
        listed = list(map(int, str(number)))
        if all([12 < len(number) < 17,
                number.startswith(('4', '5', '37', '6'), 0),
                (not(sumOfDoubleEvenPlace(listed) 
                     + sumOfOddPlace(listed)) % 10)]):
            return True
    else:
        return False


def sumOfDoubleEvenPlace(number):
    ans = 0
    for curr_num in list(number)[-2::-2]:
        ans += getDigit(curr_num * 2)
    return ans


def getDigit(number):
    return number if number < 10 else sum(divmod(number, 10))


def sumOfOddPlace(number):
    return sum(list(number)[::-2])


temp_card = input('Please input a card number:')
prompt = 'a valid' if isValid(temp_card) else 'an invalid'
print(f'This is {prompt} card')