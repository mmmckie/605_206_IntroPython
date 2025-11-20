Name: Max McKie (mmckie2)

Module Info: Module 3 Assignment: Luhn's Algorithm due on 09/14/2025 at 11:59 EST

Approach: 

luhn_verify.py - First, a counter variable is instantiated to count the number
of iterations that the while loop will execute. The while loop is then created
that will terminate once two iterations have completed. Inside the loop, the user
is prompted for a credit card number as input, and then a running total called
'checksum' is instantiated to 0, along with a boolean variable 'is_valid' that
is instantiated to false. A for loop is created that runs over index 0 to the
length of the in the credit card input number minus 1. An if statement checks
whether the iteration number is even by evaluating the iteration number modulo
2 and checking if it is equal to 0. If so, the character of the input number at
that index will be selected by slicing and then cast to an int and multiplied by
2. If this number is less than 10 (i.e., single digit), then it will be added
directly to the checksum running total. If it is 2 digits, then the sum of both
digits will be added to checksum. This is done by taking the modulus 10 of that
number and adding 1, since that number modulo 10 will return the second digit,
and the first digit will always be 1. If the for loop iteration number is not
even, then the character of the credit card number at the index of the iteration
number will be selected via slicing, casted to an int, and added directly to the
checksum. The final checksum modulus 10 will be evaluated and if it is 0 then
the 'is_valid' variable will be set to True. The checksum modulo 10 will be
printed, and then an if statement will print out whether the entered number is
a valid or invalid credit card number based on the value of 'is_valid'. After
this, the counter variable for the number of credit card inputs checked is
incremented to repeat the process. The loop will cease after 2 total iterations
have been completed.


luhn_generate.py - First, the user is prompted to input an identifier for an
incomplete credit card number. A running total checksum is
again instantiated to 0 and a counter variable 'digits_checked' is also
instantiated to 0. In contrast to luhn_verify.py, this script instead scans
the input from right to left. Instead of looping over a range from 0 to a
positive number, this script sets the range start, stop, and step parameters
to the length of the input minus 1, -1, and -1, respectively, so that the
iteration index starts at the index of the last character of the input, counts
down towards index 0 one at a time, and stops before reaching -1 (so that the
very last iteration is index 0). Inside the loop an if statement will evaluate
the modulus of 'digits_checked' to determine if it is even or odd. If it is even
(meaning the very last digit of the input number, 3rd to last digit, etc.), then
the character of the input at that loop iteration index will again be accessed
via slicing, casted to an int, and multiplied by two. If this is a single digit
number, then it will be added directly to checksum, and if it is a double digit
number, then the sum of both digits will be added to checksum using the same 
method as in luhn_verify.py. If the number of digits checked is odd (i.e., now
processing the 2nd to last digit of the input, 4th to last, etc), then the
character of the input at that iteration index will be accessed via slicing,
casted to an int, and added to the checksum. The 'digits_checked' counter will
then be incremented so that digits_checked alternates between even and odd for
each successive loop iteration. Once the loop is complete, the check digit will
be calculated as 10 minus the modulo 10 of checksum, and then this expression
modulus 10 is evaluated to handle the case of (10-0) returning a check digit of
10 (instead of 0 as would be desired in this case). Finally, this check digit is
appended to the original input number, and the completed valid number is printed
along with the check digit that was generated and appended to it.

Known Bugs:
There are no known bugs.

Citations:

None