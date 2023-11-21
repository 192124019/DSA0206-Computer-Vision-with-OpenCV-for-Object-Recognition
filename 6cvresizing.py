from PIL import Image

# Open the image
input_image = Image.open(r'C:/Users/USER/Downloads/cvimages.jpg')

# Function to resize using Nearest Neighbor Interpolation
def nearest_neighbor_resize(image, new_width, new_height):
    return image.resize((new_width, new_height), Image.NEAREST)

# Function to resize using Bilinear Interpolation
def bilinear_resize(image, new_width, new_height):
    return image.resize((new_width, new_height), Image.BILINEAR)

# Resize to a bigger size
bigger_image_nearest = nearest_neighbor_resize(input_image, new_width=800, new_height=600)
bigger_image_bilinear = bilinear_resize(input_image, new_width=800, new_height=600)

# Resize to a smaller size
smaller_image_nearest = nearest_neighbor_resize(input_image, new_width=200, new_height=150)
smaller_image_bilinear = bilinear_resize(input_image, new_width=200, new_height=150)

# Save the resized images
bigger_image_nearest.save('bigger_image_nearest.jpg')
print('Bigger image with Nearest Neighbor Interpolation saved.')
bigger_image_nearest.show()

bigger_image_bilinear.save('bigger_image_bilinear.jpg')
print('Bigger image with Bilinear Interpolation saved.')
bigger_image_bilinear.show()

smaller_image_nearest.save('smaller_image_nearest.jpg')
print('Smaller image with Nearest Neighbor Interpolation saved.')
smaller_image_nearest.show()

smaller_image_bilinear.save('smaller_image_bilinear.jpg')
print('Smaller image with Bilinear Interpolation saved.')
smaller_image_bilinear.show()
5
