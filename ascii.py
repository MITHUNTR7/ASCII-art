from PIL import Image

img = Image.open('ascii-pineapple.jpg')


width, height = img.size

pixels = list(img.getdata())
pixel_matrix =[pixels[i:i+width] for i in range(0,len(pixels),width)]


brightness_matrix = []
brightness_array = []

for i in range(len(pixel_matrix)):
    for j in range(len(pixel_matrix[i])):
        brightness = (pixel_matrix[i][j][0]+pixel_matrix[i][j][1]+pixel_matrix[i][j][2])/3
        brightness_array.append(brightness)
    
    brightness_matrix.append(brightness_array)
    brightness_array = []
    
print("Successfully constructed brightness matrix!")
print("Brightness matrix size:",len(brightness_matrix[0]),"x",len(brightness_matrix))

print(pixel_matrix[0][0])
print(brightness_matrix[0][0])