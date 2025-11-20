'''
This script accepts user inputs for the initial principal, final total amount,
term length in years, and number of times interest is compounded yearly for a CD

It will then calculate the interest rate of that CD given the provided
information and print a statement out to the console

The interest rate is calculated as:

r = ((A/P)^(1/nt) - 1)*n

with
A = Final total
P = Initial principal
t = CD term
n = number of times interest is compounded per year
'''

principal = float(input('Principal: '))
final_total = float(input('Total: '))
term = int(input('Term: '))
compound = int(input('Compound: '))

interest_rate = ((final_total/principal)**(1/(compound*term)) -1)*compound

output_str = f'The interest rate on a ${principal} CD that pays out \
${final_total} over a {term} year term is {interest_rate*100}%'

print(output_str)
