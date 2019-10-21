from PIL import Image
from PIL import ImageDraw
from _io import BytesIO
from django.core.cache import cache

def generate(width,height,image_format='PNG'):
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    text = "{}x{}".format(width, height)
    isexst = cache.get(text)
    if isexst is None:
        textwidth,textheight = draw.textsize(text)
        if textwidth<width and textheight<height:
            texttop = (height - textheight)//2
            textleft = (width - textwidth)//2
            draw.text((textleft,texttop),text,fill=(255,0,0))
            
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        cache.set(text,content,60*60)
#     image.show()
    
    return isexst

# generate(100, 100)