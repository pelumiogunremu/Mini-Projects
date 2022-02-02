import sys
import os
from PIL import Image

# grab first and second argument
input_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(input_folder, output_folder)

# check if new\ exists, if not create it
if not os.path.isdir(output_folder):
	os.mkdir(output_folder)
 
# loop through pokedex
# convert images to png
# save to the new folder
for filename in os.listdir(input_folder):
	img = Image.open(f'./{input_folder}/{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png', 'png')

print("Conversion is complete!")
"""