import os
from PIL import Image, ImageFont, ImageDraw


def openimage(filename):
    return Image.open(os.path.join("data/input/", filename))

def negative(img:Image)->Image:
    """Retorna uma nova imagem correspondente ao negativo de img"""

    negated = Image.new(img.mode, img.size, "red")
    w, h = negated.size
    for i in range(w):
        for j in range(h):
            if img.mode == "RGB":
                r, g, b = img.getpixel((i,j))
                negated.putpixel((i,j), (255-r, 255-g, 255-b))
            elif img.mode == "RGBA":
                r, g, b, a = img.getpixel((i,j))
                negated.putpixel((i,j), (255-r, 255-g, 255-b, a))
            else:
                # silent failure
                pass
    return negated


# based on https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
def compute_fontsize(msg, fontname, reference, fraction=0.8):
    fontsize = 12
    font = ImageFont.truetype(fontname, fontsize)

    while font.getsize(msg)[0] < fraction * reference:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(fontname, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    return fontsize

def process_text(text):
    """Coloca a mensagem em maiúsculas e decide quebrar linhas ou não"""

    msg = text.upper()
    words = msg.split()
    lines = 1
    if len(text) > 16:
        newmsg = []
        for word in words:
            newmsg.extend(list(word))
            if len(newmsg) > 16 and lines == 1:
                newmsg.append('\n')
                lines = 2
            else:
                newmsg.append(' ')
        
        msg = ''.join(newmsg)

    return msg, lines
    

def write_text(img:Image, text:str, color:tuple=(255, 255, 0), 
                    fontname=None, fontsize=None, position=None)->Image:
    """Escreve uma mensagem em uma imagem"""

    meme = img.copy()
    msg, lines = process_text(text)

    if fontname is None:
        fontname = "data/fonts/Rubik-Medium.ttf"
    if fontsize is None:
        if lines == 2:
            parts = msg.split('\n')
            reftext = parts[0] if len(parts[0]) > len(parts[1]) else parts[1]
        else:
            reftext = msg
        fontsize = compute_fontsize(reftext, fontname, meme.size[0])

    textfont = ImageFont.truetype(fontname, fontsize)

    if position is None:
        w, h = meme.size
        x, y = w/10, 9*h/10 - textfont.getsize(msg)[1]
    else:
        x, y = position[0], position[1]

    draw = ImageDraw.Draw(meme)

    shadowcolor = "black"

    # thin border
    draw.text((x-1, y), msg, font=textfont, fill=shadowcolor)
    draw.text((x+1, y), msg, font=textfont, fill=shadowcolor)
    draw.text((x, y-1), msg, font=textfont, fill=shadowcolor)
    draw.text((x, y+1), msg, font=textfont, fill=shadowcolor)

    # thicker border
    draw.text((x-1, y-1), msg, font=textfont, fill=shadowcolor)
    draw.text((x+1, y-1), msg, font=textfont, fill=shadowcolor)
    draw.text((x-1, y+1), msg, font=textfont, fill=shadowcolor)
    draw.text((x+1, y+1), msg, font=textfont, fill=shadowcolor)

    draw.text((x, y), msg, color, font=textfont)
    return meme

if __name__ == '__main__':
    img = openimage("yt-space.jpg")
    neg = negative(img)

    write_text(neg, "Programação Estática").show()
