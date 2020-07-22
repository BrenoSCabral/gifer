import imageio
import os

def is_jpg(files):
    jpgs = []
    for i in files:
        if i[-4:] == '.jpg':
            jpgs.append(i)
    return jpgs

def is_png(files):
    pngs = []
    for i in files:
        if i[-4:] == '.png':
            pngs.append(i)
    return pngs

images =  is_png(os.listdir()) # calling it here to get all files from my folder which are .png
# images = is_jpg(os.listdir()) # calling it here to get all files from my folder which are .jpg

images.sort() # if you wish to compile the gif in a certain order, I strongly advice you to name your files accordingly and use this line

fps = 1 # fps stands for frames per second

gif_path = "my_gif.gif" # this gif_path variable is the relative path where I'll store my gif

with imageio.get_writer(gif_path, mode='I', fps = fps ) as writer:
    for i in images:
        frames_path = i
        writer.append_data(imageio.imread(frames_path.format(i)))
