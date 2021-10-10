ls = [False] * 100
for student in range(1, 101):
    for locker in range(student - 1, len(ls), student):
        ls[locker] = not(ls[locker])
openned = ''
for idx in range(len(ls)):
    if ls[idx]:
        openned += (f'{idx + 1} ')
print(f'The following lockers are open:\n {openned}')
