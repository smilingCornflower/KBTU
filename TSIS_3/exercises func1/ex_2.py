# Read in a Fahrenheit temperature. 
# Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def get_Celci(f_temp: int) -> int:
    C = (5 / 9) * (f_temp - 32)
    return C


fahrenheit = 68
c_temp = get_Celci(fahrenheit)
print(f"Fahrenheit temperature is {fahrenheit}")
print(f"Celsius temperature is {c_temp}")

