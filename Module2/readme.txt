Name: Max McKie (mmckie2)

Module Info: Module 2 Assignment: Compound Interest due on 09/07/2025 at 11:59 EST

Approach: 

interest.py - I created 4 variables to represent the principal, interest rate, term,
and number of times interest is compounded yearly for a CD to plug into the 
provided compound interest equation. The user is prompted to input these values,
and then they are cast to int, float, int, and int, respectively, during
assignment. I then calculate the final total value of the CD at the end of the
term using the provided equation and calculate the total interest accrued by
subtracting the principal from this final value. I then use an f-string to
insert the principal, interest rate as a percent (i.e., entered value times 100),
loan term, accrued interest, and total payout into the required output format,
and finally print this string as output.


rate.py - The steps I used for this are largely the same as for interest.py,
except the user is now prompted for the final payout instead of the interest rate
and I use this information to calculate the interest rate. Here the total payout 
is casted to a float upon input, and the principal is now casted to a float as
well. The loan term and number of times interest is compounded annually are still
casted to ints. I manipulated the compound interest equation to isolate the
interest rate and use the entered information to calculate this rate. I then use
an f-string again to format the principal, payout, loan term, and calculated
interest rate (again as a percent) into the required output format and print
this output string.

Known Bugs:
There are no known bugs.

Citations:

Question 1
-Representing Rational Numbers With Python Fractions – Real Python 
-15. Floating-Point Arithmetic: Issues and Limitations — Python 3.13.7 documentation

Question 2
-14. Floating Point Arithmetic: Issues and Limitations — Python 2.7.18 documentation
-15. Floating-Point Arithmetic: Issues and Limitations — Python 3.13.7 documentation