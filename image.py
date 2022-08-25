from PIL import Image
from io import BytesIO
filename='your'

'''
# Convert image to bytes
import PIL.Image as Image
pil_im = Image.fromarray(image)
b = io.BytesIO()
pil_im.save(b, 'jpeg')
im_bytes = b.getvalue()  ''' 



with open('images/mypng.png', 'rb') as f:
        image=Image.open(f)
        image=image.convert('RGB')
        image_io = BytesIO()
        image.save(fp=image_io, format='png')
        name=f'{filename}.jpeg'
