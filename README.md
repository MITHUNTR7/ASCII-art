# ASCII Art Creator

This is a Python project that allows you to convert an image into ASCII art. The program takes an input image, processes it, and generates an ASCII representation of the image.

## Dependencies

- Python 3.x
- PIL (Python Imaging Library)

## Usage

1. Clone the repository or download the source code.
2. Install the required dependencies (`PIL` library).
3. Place the image you want to convert into ASCII art in the same directory as the Python script.
4. Modify the Python script to specify the image file name.
5. Run the Python script.

## Project Structure

- `ascii.py`: The main Python script containing the logic to convert an image into ASCII art.
- `ascii-pineapple.jpg`: Example input image (can be replaced with any image of your choice).

## Functionality

The project includes the following main functions:

- `get_pixel_matrix(img, height)`: Resizes the image to the specified height and returns a matrix representation of the image pixels.
- `get_intensity_matrix(pixels_matrix, algo_name)`: Calculates the intensity values for each pixel in the matrix based on the specified algorithm.
- `normalize_intensity_matrix(intensity_matrix)`: Normalizes the intensity values in the matrix to a range between 0 and 255.
- `convert_to_ascii(intensity_matrix, ascii_chars)`: Converts the normalized intensity values into ASCII characters using a predefined character set.
- `print_ascii_matrix(ascii_matrix)`: Prints the ASCII representation of the image.

Feel free to explore and modify the code to experiment with different image processing algorithms, character sets, or additional functionalities.

## Example

Below is an example of the ASCII art generated from the provided `ascii-pineapple.jpg` image:

![ASCII Art](art.png "ASCII Art")

## Acknowledgments

The project is inspired by the concept of converting images into ASCII art and utilizes the Python Imaging Library (PIL) for image processing.


