def multiply_list(numbers):
    return eval('*'.join([str(i) for i in numbers]))

numbers = [1, 2, 3, 4]
print(multiply_list(numbers))
