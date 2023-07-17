from PIL import Image

# Open the image
image = Image.open('/path/to/image.jpg')

# Resize the image
image = image.resize((width, height))

# Save the resized image
image.save('/path/to/resized_image.jpg')
