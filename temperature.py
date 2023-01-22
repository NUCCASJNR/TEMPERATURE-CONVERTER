temp = input("Input the  temperature you like to convert : ")
degree = int(temp[:-1])

temp_to_be_converted_to = input("Enter temperature to be converted to unit: ")
if temp_to_be_converted_to.upper() == "C" :
    kelvin_result = degree + 273
    print( "Your converted temperature from celcius to kelvin is "  +  str(kelvin_result) + 'K')
elif temp_to_be_converted_to.upper() == "K" :
 celcius_result = degree - 273
print(str(celcius_result) + 'C')