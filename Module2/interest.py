'''
This script accepts user inputs to calculate the final return and amount of
interest earned on a CD using a compounding interest equation.

The inputs are initial principal, interest rate, term in years, and number of
times interest is compounded yearly.

After entering the inputs, the final total yield and amount of interest earned
over the term will be printed out.
'''
principal = int(input('Principal: '))
interest_rate = float(input('Rate: '))
term = int(input('Term: '))
compound = int(input('Compound: '))

final_total = principal*(1+interest_rate/compound)**(compound*term)
interest_total = final_total - principal

output_str = f'Investing ${principal} in a CD with an {interest_rate*100}% \
interest rate for a term of {term} year(s) will earn ${interest_total} in \
interest for a total payout of ${final_total}'

print(output_str)
