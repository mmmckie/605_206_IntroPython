'''
This module utilizes the LFSR class to implement image encryption via the
ImageEncrypter class. If executed as a script, it will load 'football.png', save
the encrypted version as 'football_encrypted.png', then load in
'football_encrypted.png' and run the algorithm again to decrypt the image and
save it as 'football_decrypted.png'.
'''

from PIL import Image
from lfsr import LFSR

class ImageEncrypter:
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name


    def open_image(self):
        '''Read and return image data using PIL library.'''
        return Image.open(self.file_name)


    def pixelate(self):
        '''
        Load image file and return 2D array of pixels as a list of (R,G,B)
        values.

        Returns:
        rgb_vals: list
        '''
        # Read image data and get the image width/height in pixels
        img = self.open_image()
        width = img.size[0]
        height = img.size[1]

        # Load pixel data
        pixels = img.load()

        # Empty list to store rows of all pixel values
        rgb_vals = []

        # For each row of pixels in the image...
        for row in range(height):
            # Add empty list to store all pixels from this row
            rgb_vals.append([])

            # Now for each pixel in the row...
            for col in range(width):
                #Get the pixel's RGB value and add it to the current row list
                rgb_vals[-1].append(pixels[col,row])

        # Return 2D array of all pixel RGB values
        return rgb_vals


    def encrypt(self):
        '''
        Encrypts 2D array of RGB pixel data using LFSR, then returns a 2D array
        of the same size containing encrypted pixel values.

        Returns:
        encrypted_rgb_vals: list
        '''
        #Get 2D array of all pixel RGB values
        rgb_vals = self.pixelate()

        #Create list to store all encrypted pixel data
        encrypted_rgb_vals = []

        # For each row of pixel data
        for row in rgb_vals:
            # Create empty list to store row of encrypted pixel data
            encrypted_rgb_vals.append([])
            
            for pixel in row:
                # For R, G, B values in each pixel, step lfsr to obtain the
                # operand to be used with XOR
                self.lfsr.step()
                red_key = int(self.lfsr.seed, 2)
                
                self.lfsr.step()
                green_key = int(self.lfsr.seed, 2)

                self.lfsr.step()
                blue_key = int(self.lfsr.seed, 2)
                
                # Encrypted R, G, B values are result of XOR between original
                # R, G, B values and operands computed above
                new_red = red_key ^ pixel[0]
                new_green = green_key ^ pixel[1]
                new_blue = blue_key ^ pixel[2]

                # Encrypted pixel as a tuple of new R, G, B values
                new_pixel = (new_red, new_green, new_blue)
                
                # Add encrypted pixel to current row of encrypted data
                encrypted_rgb_vals[-1].append(new_pixel)
        
        # Return 2D array of encrypted pixels
        return encrypted_rgb_vals


    def save_image(self, file_name: str):
        '''Encrypts image data and saves encrypted image to file_name.'''

        # Encrypt image and get height/width as number of rows/columns
        img_data = self.encrypt()
        height = len(img_data)
        width = len(img_data[0])

        # Flatten the data to a 1D array for putdata() below
        flattened_data = []
        for row in img_data:
            flattened_data += row

        # Create new image object with same size as original in RGB mode
        new_img = Image.new('RGB', size=(width, height))

        # Transfer encrypted pixel data to new_img and save file
        new_img.putdata(flattened_data)
        new_img.save(file_name)
        return

def main():
    # Create LFSR instance and ImageEncrypter instance, then encrypt football.png
    # and save it as 'football_encrypted.png'
    lfsr = LFSR('10011010', 5)
    football = ImageEncrypter(lfsr, 'football.png')
    football.save_image('football_encrypted.png')

    # Create new LFSR instance with same seed/tap 'password'. Also create new
    # ImageEncrypter instance, then decrypt 'football_encrypted.png' and save to
    # 'football_decrypted.png'
    lfsr = LFSR('10011010', 5)
    football = ImageEncrypter(lfsr, 'football_encrypted.png')
    football.save_image('football_decrypted.png')


if __name__ == '__main__':
    main()