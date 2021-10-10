while True:
    try:
        N = int(input('Please input a positive integer:'))
        if N > 0:
            break
        else:
            raise Exception
    except:
        print('Invalid Input!\n')
print('%-8s%-8s%-8s'%('m','m+1','m**(m+1）'))
for i in range(1,N+1):
    print('%-8d%-8d%-8d'%(i,i+1,i**(i+1)))