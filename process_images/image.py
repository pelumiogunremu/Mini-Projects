from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
img = img.resize((300, 300))
print(img.format, img.size, img.mode)

grey_img = img.convert("L")
grey_img.save("grey.png", "png")
# grey_img.show()

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")
filtered_img.show()

box = (50, 50, 200, 200)
region = grey_img.crop(box)
region.save("cropped_grey.png", "png")