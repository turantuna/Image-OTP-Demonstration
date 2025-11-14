from PIL import Image
import numpy as np
from random_key import generate_key

name_list= ["pengu","brot"]
original_1 = f"img/{name_list[0]}.png"
original_2 = f"img/{name_list[1]}.png"

#random noise
key = generate_key(600,600)
arr_key= np.array(key)
# Pengu and Brot are opened
img1 = Image.open(original_1).convert("RGBA")
img2 = Image.open(original_2).convert("RGBA")

list_img =[img1,img2]
list_arr = []
list_out_img = []

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
    o.save(f"img/encrypted_{name_list[i]}.png")
    #update the arrlist with the encrypted images
    list_arr[i] = np.array(o)

result = list_arr[0]
for i in range(1,len(list_arr)):
    # XOR RGB channels of each encrypted image_array with eachother
    
    result[:, :, :3] = np.bitwise_xor(list_arr[i][:, :, :3], result[:, :, :3])

    # Make fully opaque
    result[:, :, 3] = 255
    
# Convert back to image
result_image = Image.fromarray(result, "RGBA")
result_image.save("img/out.png")