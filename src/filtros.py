# Apresentação de filtros
from PIL import Image, ImageFilter
from math import sqrt
import os
from utils import show_vertical, show_horizontal, in_file, out_file


# IMPC06 | "Borrando uma Imagem em Python": https://youtu.be/IgQfpMPblR0
def show_box_blur(filename, r=1):
    '''Aplica um filtro BoxBlur à imagem, exibe e salva o resultado'''

    original = Image.open(in_file(filename))
    filtered = original.filter(ImageFilter.BoxBlur(r))

    #Mostrar as imagens lado a lado
    show_horizontal(original, filtered)
    filtered.save(
        out_file(
            '{}_boxblur_{}.jpg'.format(filename[:filename.index('.')], r)
        )
    )

# IMPC07 | "DETECTANDO ARESTAS na Imagem com Filtro Sobel": https://youtu.be/uHT4qDzq1bY
def show_edges(filename, direction='x',offset=0):
    '''Aplica um filtro Sobel à imagem, exibe e salva o resultado'''

    original = Image.open(in_file(filename)).convert('L')
    XSOBEL = ImageFilter.Kernel((3, 3),
                                [-1, 0, 1,
                                -2, 0, 2,
                                -1, 0, 1],
                                1, 
                                offset)
    YSOBEL = ImageFilter.Kernel((3, 3),
                                [-1, -2, -1,
                                0, 0, 0,
                                1, 2, 1],
                                1,
                                offset)
    if direction == 'x':
        filtered = original.filter(XSOBEL)
    elif direction == 'y':
        filtered = original.filter(YSOBEL)
    else:
        vsobel = original.filter(XSOBEL)
        hsobel = original.filter(YSOBEL)
        w, h = original.size
        filtered = Image.new('L', (w, h))

        for i in range(w):
            for j in range(h):
                value = sqrt(
                    vsobel.getpixel((i, j))**2 + hsobel.getpixel((i, j))**2
                )
                value = int(min(value, 255))
                filtered.putpixel((i, j), value)

    # Mostrar as imagens lado a lado
    show_horizontal(original, filtered)
    filtered.save(
        out_file(
            '{}_{}sobel_{}.jpg'.format(
                                    filename[:filename.index('.')], 
                                    direction,
                                    offset)
        )
    )


if __name__ == "__main__":
    # Experimente outras imagens e tamanhos de filtros
    # show_box_blur('ellie.jpg', 4)
    show_edges('sam.jpg', 'a', 0)

