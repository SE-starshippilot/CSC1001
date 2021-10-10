def isAnagram(li_words):
    li_words[0].sort()
    li_words[1].sort()
    return True if li_words[0] == li_words[1] else False


while True:
    try:
        wd_1, wd_2 = input('Please input 2 words separated by space:').split()
    except ValueError:
        print('Invalid input for words.')
    else:
        break
prompt = 'are' if isAnagram([list(wd_1), list(wd_2)]) else "aren't"
print(f'{wd_1} and {wd_2} {prompt} anagram of each other.')
