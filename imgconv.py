# Caroline Winakur 2022
# File to save images of clubs converted to blue - run once

from PIL import Image
import numpy as np
from pathlib import Path

blue_color = (8, 50, 160)
 
# get the path/directory
folder_dir = 'cards'
 
# iterate over files in that directory, selecting only clubs
images = Path(folder_dir).glob('*clubs.png')
for image in images: # image is a pathname!
    img = Image.open(image)

    width = img.size[0] 
    height = img.size[1] 
    for i in range(0,width): # process all pixels
        for j in range(0,height):
            data = img.getpixel((i,j))
            if (data[0]<250 and data[1]<250 and data[2]<250): # since ace has shading, not looking for exact value
                # img.putpixel((i,j),(0, 0, 255)) # convert to blue
                img.putpixel((i,j),blue_color)
    # img.save("cards/blue_" + str(image)[6:])
    img.save(str(image)[6:])