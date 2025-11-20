'''
This script implements luhns generation algorithm. The user is asked to input
a credit card number and a running total is instantiated at 0. The entered
number is then scanned from right to left. The 1st, 3rd, 5th, etc. digits
checked will be multiplied by 2, and if the result is <10 then that result will
be added to the running total. If it is >= 10, then both digits of the result
will be added to the running total. Once the entire number is scanned, the check
digit will be computed as the difference of 10 and the running total modulo 10.
The valid credit card number and this check digit will then both be printed.
'''

cc_number = input('Please enter an identifier: ')

checksum = 0
digits_checked = 0

#start at the last digit, stop at the 0th digit, step of -1
for idx in range(len(cc_number)-1, -1, -1):
    # if the last digit, 3rd to last, 5th to last, etc., multiply by 2
    if digits_checked % 2 == 0:
        number = int(cc_number[idx]) * 2 
        
        #if new number is single digit, add directly to checksum 
        if number < 10:
            checksum += number
        # if it's 2 digits, add the digits together
        # first digit is always 1, so add modulo 10 +1 to checksum
        else:
            checksum += (number % 10) + 1
    # if 2nd, 4th, 6th to last, etc, add digit to checksum
    else:
        checksum += int(cc_number[idx])
    
    digits_checked += 1

# check digit is going to be the amount needed to make the mod 10 equal 0
# if the modulus is 0, we need this expression to evaluate to 0, not 10
# so take the modulus of the result to handle this case
check_digit = (10 - (checksum % 10)) % 10

cc_number += str(check_digit)
print(f'The valid credit card number is: {cc_number} and the newly computed \
check digit is: {check_digit}')
