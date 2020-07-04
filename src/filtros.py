# Apresentação de filtros
from PIL import Image, ImageFilter
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


if __name__ == "__main__":
    # Experimente outras imagens e tamanhos de filtros
    show_box_blur('ellie.jpg', 4)

