from PIL import Image


asciiScale = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
img = Image.open('ascii-pineapple.jpg')

def get_pixel_matrix(img):
    img.thumbnail((img.width, 200))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

def get_brightness_matrix(pixel_matrix):
    brightness_matrix = []
    for i in range(len(pixel_matrix)):
        brightness_array = []
        
        for j in range(len(pixel_matrix[i])):
            brightness = (pixel_matrix[i][j][0] + pixel_matrix[i][j][1] + pixel_matrix[i][j][2]) / 3
            brightness_array.append(brightness)
            
        brightness_matrix.append(brightness_array)
    return brightness_matrix

def normalise_brightness_matrix(brightness_matrix):
    maxPix = max(map(max,brightness_matrix))  
    minPix = min(map(min,brightness_matrix))
    normalised_matrix = []
    for row in brightness_matrix:
        normalised_row = []
        for pix in row:
            r = 255*((pix - minPix)/(maxPix - minPix))
            normalised_row.append(r)
        normalised_matrix.append(normalised_row)
        
    return normalised_matrix

def get_ascii_matrix(brightness_matrix):
    ascii_matrix = []
    for i in range(len(brightness_matrix)):
        ascii_array = []
        for j in range(len(brightness_matrix[i])):
            ascii_array.append(asciiScale[int(brightness_matrix[i][j]/255 * 64)])
        
        ascii_matrix.append(ascii_array)
    return ascii_matrix


def print_ascii(ascii_matrix):
    for row in ascii_matrix:
        line = [c+c+c for c in row]
        print("".join(line))


pixel_matrix = get_pixel_matrix(img)
brightness_matrix = get_brightness_matrix(pixel_matrix)
brightness_matrix = normalise_brightness_matrix(brightness_matrix)
ascii_matrix = get_ascii_matrix(brightness_matrix)
print_ascii(ascii_matrix)