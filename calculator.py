import math

def squareroot(x)
	return math.sqrt(x)
# Function adds two numbers
def add(first_number, second_number):
    return first_number + second_number


# Function subtracts two numbers
def subtract(first_number, second_number):
    return first_number - second_number


# Function multiplies two numbers
def multiply(first_number, second_number):
    return first_number * second_number


# Function divides two numbers
def divide(first_number, second_number):
    return first_number / second_number

def hex_add(a, b):
	return hex(int(a, 16) + int(b, 16))
	
def hex_sub(a, b):
	return hex(int(a, 16) - int(b, 16))
	
def hex_mul(a, b):
	return hex(int(a, 16) * int(b, 16))
	
def hex_div(a, b):
	return hex(int(a, 16) / int(b, 16))
	
print('Select options.')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('for hexadecimal number')
print('1h. Add')
print('2h. Subtract')
print('3h. Multiply')
print('4h. Divide')


while True:
    # Take input from the console
    choice = input('Enter choice(1/2/3/4/1h/2h/3h/4h or n to cancel): ')
    # Check if choice is one of the five options
    if choice in ('1', '2', '3', '4', '1h', '2h', '3h', '4h'):
        first_number = float(input('Enter first number: '))
        second_number = float(input('Enter second number: '))

        if choice == '1':
            print(first_number, '+', second_number, '=', add(first_number, second_number))

        elif choice == '2':
            print(first_number, '-', second_number, '=', subtract(first_number, second_number))

        elif choice == '3':
            print(first_number, '*', second_number, '=', multiply(first_number, second_number))

        elif choice == '4':
            print(first_number, '/', second_number, '=', divide(first_number, second_number))
        elif choice == '1h':
            print(first_number, '+', second_number, '=', hex_add(first_number, second_number))

        elif choice == '2h':
            print(first_number, '-', second_number, '=', hex_sub(first_number, second_number))

        elif choice == '3h':
            print(first_number, '*', second_number, '=', hex_mul(first_number, second_number))

        elif choice == '4h':
            print(first_number, '/', second_number, '=', hex_div(first_number, second_number))
    elif choice == 'n':
        print('Your are successfully logged out!')
        break
    else:
        print('Please enter correct input among these 1/2/3/4/n')
