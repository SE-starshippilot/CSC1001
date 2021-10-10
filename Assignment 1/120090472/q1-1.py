def get_correct_input(seq):
    prompt = ['final account value:','interest rate (in %):','number of years:'] 
    while True:
        try:
            curent_input = float(input('Input %s'%prompt[seq]))
            if curent_input > 0:
                break
            else:
                raise Exception    
        except:
            print('Invalid input for %s.\n'%prompt[seq])
    return curent_input/100 if seq ==1 else curent_input
final_value = get_correct_input(0)
interest_rate = get_correct_input(1)
years = get_correct_input(2)

init_value = final_value/(1+interest_rate)**years 
print("The initial value is: %f"%init_value)