'''
This module defines the Linear Feedback Shift Register (LFSR) class. If run as a
script, it will create 5 LFSR instances with different initial seeds and tap
positions, then step them once and print the newly computed bit along with the
new seed value.
'''

class LFSR:
    def __init__(self, seed: str, tap: int):
        self.seed = seed
        self.tap = tap


    def bit(self, i: int):
        '''Returns the bit at index i from the seed value as an int.'''
        return int(self.seed[i])


    def step(self):
        '''
        Computes the new bit by XOR operation with the leftmost bit and the tap
        bit, then updates the seed value.

        Returns:
        new_bit: int
        '''

        # Tap position is defined from the right end of the seed value
        tap_idx = len(self.seed) - self.tap

        # XOR leftmost bit with tap bit
        new_bit = self.bit(0) ^ self.bit(tap_idx)

        # Drop leftmost bit and concatenate new bit to the right
        self.seed = self.seed[1:] + str(new_bit)
        
        return new_bit


    def __str__(self):
        return self.seed


def main():
    # Create 5 different LFSR instances
    lfsr_1 = LFSR('0110100111', 2)
    lfsr_2 = LFSR('0100110010', 8)
    lfsr_3 = LFSR('1001011101', 5)
    lfsr_4 = LFSR('0001001100', 5)
    lfsr_5 = LFSR('1010011101', 7)

    #Step each once and print the new seed value and the new bit
    for lfsr in [lfsr_1, lfsr_2, lfsr_3, lfsr_4, lfsr_5]:
        new_bit = lfsr.step()
        print(lfsr, new_bit)


if __name__ == '__main__':
    main()