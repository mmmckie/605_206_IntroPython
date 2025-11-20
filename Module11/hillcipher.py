'''
Class implementation of Hill Cipher encryption and decryption algorithm.
'''
import numpy as np

class HillCipher():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def __init__(self, plaintext: str, key_matrix, modulus: int):
        self.p = plaintext
        self.key = key_matrix
        self.m = modulus

    def determinant(self):
        '''Return determinant of key matrix.'''
        # Numpy's linalg.det returns float with floating point error,
        # so round and cast to int
        return int(round(np.linalg.det(self.key),0))
    
    def invertible(self):
        '''Test if key matrix is invertible.'''
        # Invertible matrix must be square
        shape = self.key.shape
        if shape[0] != shape[1]:
            print('The matrix is not square.\n')
            return False
        
        # Determinant of invertible matrix must != 0
        det = self.determinant()
        if det == 0:
            print('The determinant = 0.\n')
            return False

        # If both conditions are satisfied, key matrix is invertible
        print('The matrix is invertible.\n')
        return True
    
    def mod_inverse(self, n):
        '''Returns modular multiplicative inverse (MMI) of n (w.r.t self.m).'''
        # For 1 to m, test if n*i = 1 mod m
        for i in range(1, self.m):
            # If true, i is the MMI --> return i
            if (n * i) % self.m == 1:
                return i
            
    def encode(self, str_):
        '''Encode a string of letters to a list of 2x1 column vectors using the
        index of each letter in the alphabet.'''
        # Append index of each letter in str_ to a list
        encoded_msg = []
        for letter in str_:
            encoded_msg.append(self.alphabet.index(letter))
        # Reshape list into array of 1x2 row vectors
        # (will reshape to 2x1 column vectors later)
        encoded_msg = np.array(encoded_msg).reshape(-1, 2)
        return encoded_msg

    def decode(self, numbers):
        '''Accepts flattened array of numbers and decodes them according to the
        letters in the alphabet at those indices.'''
        
        decoded_msg = ''
        for letter_index in numbers:
            decoded_msg += self.alphabet[letter_index]
        return decoded_msg

    def encrypt(self):
        '''Encrypts plaintext message and returns list of 2x1 encrypted vectors.'''
        
        print(f'Plaintext: {self.p}')
        # List to store all 2x1 column vectors of encoded message
        encoded_chunks = []
        encoded_msg = self.encode(self.p)
        for chunk in encoded_msg:
            # Reshape 1x2 row vectors to 2x1 column vectors
            encoded_chunks.append(chunk.reshape(2,-1))
        
        print(f'Plaintext column vectors: {encoded_chunks}\n')

        # Now encrypt each 2x1 column vector using encryption algorithm and
        # append encrypted vectors to list
        encrypted_columns = []
        for column in encoded_chunks:
            encrypted_col = np.matmul(self.key, column) % self.m
            encrypted_columns.append(encrypted_col)

        # Decode encrypted column vectors to obtain encrypted message text
        ciphertext = self.decode(np.array(encrypted_columns).flatten())
        
        # Print encrypted text and column vectors
        print(f'Ciphertext: {ciphertext}')
        print(f'Ciphertext column vectors: {encrypted_columns}\n')
        return encrypted_columns
    
    def get_decryption_key(self):
        '''Returns modular multiplicative inverse of key matrix.'''
        # Storing elements of key matrix for easy permutation to obtain inverse
        # Key matrix = [[a, b],
        #               [c, d]]
        a = self.key[0][0]
        b = self.key[0][1]
        c = self.key[1][0]
        d = self.key[1][1]
        
        # Compute determinant of key matrix and then its MMI
        det = self.determinant()
        det_mmi = self.mod_inverse(det)
        
        # Compute inverse of key matrix mod m
        inverse = np.array([[d, -b], [-c, a]]) % self.m
        
        # Finally compute MMI of key matrix and return
        key_inverse = det_mmi * inverse % self.m
        return key_inverse

    def decrypt(self, ciphertext):
        '''Decrypts list of 2x1 column vectors to obtain plaintext message.'''
        # Get MMI of key matrix for decryption
        decryption_key = self.get_decryption_key()
        
        # Now decrypt each 2x1 column vector using decryption algorithm and
        # append decrypted vectors to list
        decrypted_columns = []
        for column in ciphertext:
            decrypted_col = np.matmul(decryption_key, column) % self.m
            decrypted_columns.append(decrypted_col)
        
        # Decode decrypted 2x1 column vectors to get original plaintext message
        plaintext = self.decode(np.array(decrypted_columns).flatten())

        # Print decrypted/decoded message and the decrypted column vectors
        print(f'Plaintext: {plaintext}')
        print(f'Plaintext column vectors: {decrypted_columns}\n')
        return decrypted_columns
