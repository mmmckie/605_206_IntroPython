'''
This script will ask for a credit card number, then use Luhn's verification
algorithm to check whether the entered number is valid and print the answer.
It will ask for another credit card number to repeat the process until 2 total
iterations have been completed.

A running total is instantiated to 0 at the start of each iteration, and the
input number is read from left to right.

For every other digit starting from the first, the digit is
multiplied by two and then added to the running total if the result is <10.
If the result is >=10, then both digits of the result are added to the running
total.

For every other digit starting from the second, the digit is added directly to
the running total.

Finally, the running total modulo 10 is calculated, and if this is 0 then a
print statement confirms the credit card number's validity. If the modulo of 10
is not 0, the print statement will state that it is invalid.
'''

numbers_checked = 0
while numbers_checked < 2:
    cc_number = input('Please enter a credit card number: ')

    checksum = 0
    is_valid = False

    for idx in range(len(cc_number)):
        # if idx is 0, 2, 4, 6, ..., multiply digit by 2
        if idx % 2 == 0:
            number = int(cc_number[idx]) * 2
            # if 1-digit result, add to checksum
            if number < 10:
                checksum += number
            # if 2-digit result, add the digits together
            # max is 9*2 = 18 so the first digit is always 1
            # and number % 10 returns second digit
            else:
                checksum += (number % 10) + 1

        # if idx is 1, 3, 5, etc., add to checksum
        else:
            checksum += int(cc_number[idx])

    # if checksum evenly divisible by 10, valid CC
    checksum %= 10
    if checksum == 0:
        is_valid = True

    print(f'Checksum = {checksum}')

    if is_valid:
        print(f'{cc_number} is a valid CC number.')
    else:
        print(f'{cc_number} is an invalid CC number.')

    numbers_checked +=1
