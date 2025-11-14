from PIL import Image
import numpy as np
from random_key import generate_key
import glob
from itertools import combinations

#random noise
key = generate_key(600,600)
arr_key= np.array(key)

list_img =[]
list_arr = []
list_out_img = []

# Get all PNGs
image_paths = glob.glob("input/*.png")
for ip in image_paths:
    list_img.append(Image.open(ip).convert("RGBA"))







for i in list_img:
    print(i.size,key.size)
    # Ensure images and key are the same size
    if i.size != key.size:
        
        raise ValueError("Images must be the same size as key")
    
    #convert each imageto a numpy array
    list_arr.append(np.array(i))
    
for a in list_arr:

    # XOR RGB channels of each image_array with key
    result = np.empty_like(a)
    result[:, :, :3] = np.bitwise_xor(a[:, :, :3], arr_key[:, :, :3])

    # Make fully opaque
    result[:, :, 3] = 255
    
    # Convert back to image
    result_image = Image.fromarray(result, "RGBA")
    list_out_img.append(result_image)

for i,o in enumerate(list_out_img):

    #save the encrypted images
    o.save(f"enc/encrypted_{i}.png")
    #update the arrlist with the encrypted images
    list_arr[i] = np.array(o)
i = 0
for a,b in combinations(list_arr,2):
    #xor each image pairwise with every other image
    result[:, :, :3] = np.bitwise_xor(a[:, :, :3], b[:, :, :3])
    result[:, :, 3] = 255

    result_image = Image.fromarray(result, "RGBA")
    result_image.save(f"out/out{i}.png")
    i += 1

