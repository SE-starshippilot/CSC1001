def prime(num):
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
    return flag
ans = ''
count = 0 
while True:
    try:
        N = int(input('Please input a positive integer:'))
        if N > 1:
            break
        else:
            raise Exception
    except:
        print('Invalid Input!\n')

for i in range(2,N):
    if prime(i):
        ans += '%-4d'%i
        count += 1
        if count % 8 == 0:
            ans += '\n'
print("The prime numbers smaller than %d include:\n%s"%(N,ans))