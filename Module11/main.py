'''
When run as a script, this module will execute three examples of message
encryption and decryption with the Hill Cipher algorithm using the HillCipher
class.
'''
from hillcipher import HillCipher
import numpy as np


def main():
    plaintext = 'ATTACKATDAWN'
    modulus = 26

    key_matrix_1 = np.array([[19, 8, 4], [3, 12, 7]])
    key_matrix_2 = np.array([[7, 8], [11, 11]])
    key_matrix_3 = np.array([[5, 15], [4, 12]])

    cipher_1 = HillCipher(plaintext, key_matrix_1, modulus)
    cipher_2 = HillCipher(plaintext, key_matrix_2, modulus)
    cipher_3 = HillCipher(plaintext, key_matrix_3, modulus)

    # For each example
    for cipher in [cipher_1, cipher_2, cipher_3]:
        #  If key is invertible, encrypt and decrypt
        # Else, continue to next cipher
        if cipher.invertible():
            ciphertext = cipher.encrypt()
            cipher.decrypt(ciphertext)


if __name__ == '__main__':
    main()
