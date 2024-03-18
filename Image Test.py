import json
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageOps import scale

#Test Data
groups = [{'group': 10, 'right': 20, 'left': 10}, {'group': 11, 'right': 30, 'left': 21}]
mice_info = {'subjects': 120}
strand_info = {'strand': 'B6CF1'}
gender_info = {'gender': "female"}
list_greys = {2.6, 5.2}

#Make Image
image = Image.new('RGB', (1500, 1000), 'white')
draw = ImageDraw.Draw(image)

#Font
font_path = "./fonts/ARIAL.TTF"
font_size = 15
fontW = ImageFont.truetype(font_path, font_size)

#Draw Mouse Icon
mouse_icon_path = 'mouse_folder/mouse_icon.png'
mouse_icon = Image.open(mouse_icon_path)
new_mouse_size = (100, 100)
mouse_icon_resized = mouse_icon.resize(new_mouse_size)
image.paste(mouse_icon_resized, (20, 350), mouse_icon_resized.convert('RGBA'))
draw.text((20, 475), f"Number of Subjects: {mice_info['subjects']}", fill='black', font=fontW)
draw.text((20, 500), f"Strand: {strand_info['strand']}", fill='black', font=fontW)
draw.text((20, 525), f"Gender: {gender_info['gender']}", fill='black', font=fontW)


#Outputting Groups
u, v = (150, 50)
for group in groups:
    title = f"Group #{group['group']}"
    num_of_mice_in_group = group['right'] - group['left'] + 1

    draw.text((u, v), title, fill='black', font=fontW)
    v += 100


#Outputting Radiation Data
base_scale_factor = 10
x, y = (250, 50)
for gray in list_greys:
    radiation_icon_path = 'icon_folder/radiation_icon.png'
    radiation_icon = Image.open(radiation_icon_path)

    new_size = int(base_scale_factor * gray), int(base_scale_factor * gray)
    radiation_icon_resized = radiation_icon.resize(new_size)

    image.paste(radiation_icon_resized, (x, y), radiation_icon_resized.convert('RGBA'))
    draw.text((x, y + new_size[1] + 10), f"{gray} cGy", fill='black', font=fontW)

    arrow_start = (x + new_size[0], y + new_size[1] // 2)
    arrow_end = (arrow_start[0] + 200, arrow_start[1])
    draw.line([arrow_start, arrow_end], fill='black', width=2)

    y += 150


image.save('output_image.png')
