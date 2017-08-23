darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

from PIL import Image
im = Image.open("img_2268.jpg")      #image can be replaced by any .jpg/.png file on the user's laptop
im.show()
pixels = im.getdata()
for i in pixels:
    print(i)
	
color_pixels = list(im.getdata())
list_length = len(color_pixels)

for i in range(list_length):
	red = color_pixels[i][0]
	blue = color_pixels[i][1]
	green = color_pixels[i][2]
	sum = red + blue + green
    
	print(sum)
	if sum < 182:
		color_pixels[i] = darkBlue
	elif sum >= 182 and sum < 364:
		color_pixels[i] = red
	elif sum >= 364 and sum < 546:
		color_pixels[i] = lightBlue
	else:
		color_pixels[i]= yellow 
        
im.putdata(color_pixels)

im.show()

#If you want the new image to be saved, uncommment line 37.
#new_image.save(“output.jpg”, “jpeg”)