from PIL import Image

# Take list of paths for images
images = ['E1.1.jpg','E1.2.jpg','E2.jpg','E3.jpg']

# Create a list of image objects
image_list = [Image.open(file) for file in images]

# Save the first image as a GIF file
image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[:], # append rest of the images
            duration=200, # in milliseconds
         loop=0   )