Name: Max McKie (mmckie2)

Module Info: Module 8 Assignment: Linear Feedback Shift Registers due on
                                    10/19/2025 at 11:59 PM EST

Approach: 

lfsr.py - The LFSR class is defined with an __init__() method that accepts 2
explicit arguments, 'seed' and 'tap' and then assigns the instance variables of
the same names to these values. A 'bit()' method is defined that accepts an int
index to return the bit at that index from the seed as an int, and then a 'step'
method is defined to implement the LFSR algorithm to step the seed by 1 iteration.
This consists of first getting the tap index from the tap value, calculated as
'len(seed) - self.tap' since tap is 1-indexed counted from right to left, but
indexing bits from the seed is 0-indexed from left to right. Then, the leftmost
bit is obtained by calling 'bit(0)' and the new bit is computed by an XOR
operation between the leftmost bit and the tap bit. The seed is then updated by
dropping the leftmost bit and concatenating the new bit to the right, and the
new bit is returned. The __str__ method is also overloaded to return the seed
value. Outside of the class definition, a main() function is defined that creates
5 instances of the LFSR class with different seeds and taps. A for loop iterates
over all of these instances, calling the 'step()' method once and printing the
new seed and the newly computed bit for each instance. Finally, an if name equals
main dunder statement executes the main() function only if this module is executed
as a script.

image_encrypter.py - First the Image class is imported from PIL and the LFSR
class is imported from lfsr.py. Then the ImageEncrypter class is defined such
that it accepts an instance of the LFSR class and a string 'file_name' in its
__init__ method. An open_image() method is defined to read file_name's image data
using the PIL library. A pixelate() method is defined that first gets the size of
this image and loads the RGB values of the pixels. An empty list is created to 
contain all rows of pixel data, and then a new sublist is created for each row to
contain all pixels per row. All pixels of the input image are iterated through
and appened to these sublists to ultimately create a 2D array of RGB pixel data
that gets returned. Next, an encrypt() method calls pixelate() to obtain this 2D
array, and another empty list is created to contain all rows of encrypted pixel
data. Sublists are also created within this list to contain each row of data for
the encrypted pixels. The encrypted pixel values are obtained by calling
self.lfsr.step() once for each of the R, G, and B values in each pixel, and then
taking the result of an XOR operation between the updated value of self.lfsr.seed
with each of the original R, G, B values. A tuple of the newly encrypted (R,G,B)
data is then created and added to the 2D array 'encrypted_rgb_vals' which is then
returned after the full 2D array is populated. A save_image() method calls this
encrypt() method to obtain this 2D array of encrypted values, then stores the
height and width of this array, flattens it by turning it into a 1D list of
values from top left to bottom right, creates a new PIL.Image instance of the
same size as the original image, and then loads the flattened data into this new
Image object and saves the image to disk with the given file name. Lastly a main()
function is created outside of the ImageEncrypter class that creates an LFSR
instance with a seed and tap of '10011010' and 5, then creates an ImageEncrypter
object called 'football' using this LFSR and an image's filename 'football.png'.
'football.save_image('football_encrypted.png')' is called to encrypt 'football.png'
and save it to a new file on disk as 'football_encrypted.png'. A new LFSR
instance is then created with the same seed and tap as before, and a new
ImageEncrypter instance again called 'football' is created with this LFSR and the
new filename 'football_encrypted.png' passed as parameters to its __init__
method. 'football.save_image('football_decrypted.png')' is then called to decrypt
'football_encrypted.png' and save the result to disk as 'football_decrypted.png'.
Finally, an if name equals main dunder statement executes the main() function
only if this module is executed as a script.


Known Bugs:
There are no known bugs.

Citations:
-https://pillow.readthedocs.io/en/stable/reference/Image.html#