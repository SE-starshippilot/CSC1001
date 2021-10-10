from math import sin,cos,tan
def integrate(function,low,high,partitian): 
    length = (high-low)/partitian
    sum = 0
    for i in range (1,partitian+1):
        sum += length*(function(low+length*(i-0.5)))
    return sum
while True:
    chosen_func = input("From 'sin','cos','tan'  which function would you like to integrate?\n")
    if chosen_func in ['sin','cos','tan']:
        break
    else:
        print('Invalid Function Name!\n')
while True:
    try:
        lower,upper = map(float,list(input('Input the lower & upper bound with space in between:').split(' ')))
        if lower <= upper:
            break
        else:
            print('Lower bound larger than upper bound.',end=' ')
            raise Exception
    except:
        print('Invalid Input of lower and/or upper bound!\n')
while True:
    try:
        intv = int(input('Input number of subintervals:'))
        if intv > 0:
            break
        else:
            raise Exception
    except:
        print('Number of sub-intervals must be a positive integer!\n')
print("The integration of function y=%s(x) from %f to %f in %d sub-interval is %f"%(chosen_func,lower,upper,intv,integrate(eval(chosen_func),lower,upper,intv)))