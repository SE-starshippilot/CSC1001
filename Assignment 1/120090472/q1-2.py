while True:
    try:
        x = int(input("Please input a positive integer:"))
        if x > 0:
            break
        else:
            raise Exception
    except:
        print("Invalid Input!\n")    
str_x = str(x)
for i in str_x:
    print(i)