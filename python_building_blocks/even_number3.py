# Check if the user given number is Even or Odd.

input_number = int(input('Enter a number to check if it is Even or Odd:'))

if input_number % 2 == 0:
    print(input_number,'is an Even number')
else:
    print(f'{input_number} is an Odd number')