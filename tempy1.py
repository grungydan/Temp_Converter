'''
Simple temperature converter written in Python3. Handles conversions between Fahrenheit, Celcius, Kelvin, and Rankine.
'''
# global variables


# converter function
def converter(a,b,c):
    if start_unit[0] == 'f':
        if convert == 'c':
            new_temp = (temp - 32) * 5/9
        elif convert == 'k':
            new_temp = (temp + 459.67) * 5/9
        elif convert == 'r':
            new_temp = temp + 459.67

    elif start_unit[0] == 'c':
        if convert == 'f':
            new_temp = temp * 9/5 + 32
        elif convert == 'k':
            new_temp = temp + 273.15
        elif convert == 'r':
            new_temp = (temp + 273.15) * 9/5

    elif start_unit[0] == 'k': 
        if convert == 'f':
            new_temp = temp * 9/5 - 459.67
        elif convert == 'c':
            new_temp = temp - 273.15
        elif convert == 'r':
            new_temp = temp * 9/5

    elif start_unit[0] == 'r':
        if convert == 'f':
            new_temp = temp - 459.67
        elif convert == 'c': 
            new_temp = (temp - 491.67) * 5/9
        elif convert == 'k':
            new_temp = temp * 5/9

    return new_temp 

# function to ask if continue
def another():

    return input("Would you like to convert another temperature? (Y/N): ").lower().startswith('y')


while True:
    new_temp = 0
    temp = float(input("temp: "))
    start_unit = input("starting unit: ")
    convert = input("new unit: ")


    output = converter(temp, start_unit, convert)
    print(str(output))

  
    
    if not another():
        break

