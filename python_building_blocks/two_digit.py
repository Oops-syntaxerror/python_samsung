# Check if user given number is 2 digit number

input_number = int(input('Enter a number:'))
temp = input_number

while(input_number != 0):
    input_number = input_number % 10
    input_number /= 10

if input_number == temp:
    print(input_number,'is a 2-Digit number')