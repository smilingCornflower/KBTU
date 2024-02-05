# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case. 


class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

manipulator = StringManipulator()

manipulator.getString()
manipulator.printString()