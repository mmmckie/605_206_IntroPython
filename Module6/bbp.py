'''
This module implements the Bailey-Borwein-Plouffe (BBP) formula for an infinite
series truncated at n terms to estimate the value of pi. If executed as a script,
this series will be computed for n = 10 and the value will be printed along with
the math module's value of pi for comparison.
'''

import math

def recursive_pi(n: int) -> float:
    '''Recursively calculates pi to arbitrary precision using the BBP series sum
    up to n terms.

    Arguments:
    n --> int representing highest term of BBP series to calculate.

    Returns:
    series_element --> float approximation of pi from summing BBP series over
                        terms 0 to n.
    
    '''
    # Calculate nth term of the BBP series
    term1 = 4 / (8*n + 1)
    term2 = 2 / (8*n + 4)
    term3 = 1 / (8*n + 5)
    term4 = 1 / (8*n + 6)
    series_element = (1 / 16**n) * (term1 - term2 - term3 - term4)

    # Print current contribution to series sum
    print(f'{n}\t{series_element}')

    if n >0: # Recursively calculate series sum down to n = 0
        return series_element+recursive_pi(n-1)
    else: # Base case, n = 0
        return series_element

def main():
    pi_char = '\u03C0' # Unicode escape sequence for lowercase pi
    print(f'k\tContribution to the value of {pi_char}')

    # Calculate BBP approximation for n = 0 to 10
    pi = recursive_pi(10)

    # Print results
    print(f'\nThe BBP value of {pi_char} = {pi}')
    print(f'The Math module value of {pi_char} = {math.pi}')

if __name__ == '__main__':
    main()
