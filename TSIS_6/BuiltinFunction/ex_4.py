import time

def square_root(num) -> float:
    return num ** .5

delay = int(input('Miliseconds: '))
number = int(input('Number: '))
time.sleep(delay / 1000)
print(f"Square root of {number} after {delay} miliseconds is {square_root(number)}")
