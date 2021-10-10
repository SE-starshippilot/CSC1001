while True:
    try:
        m = int(input('Please input a number:'))
        break
    except:
        print("Invalid Input!\n")
n = 1
while n **2 < m:
    n +=1

print("n=%d"%n)