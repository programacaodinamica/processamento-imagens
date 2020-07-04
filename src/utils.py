from PIL import Image, ImageFilter
import os
import numpy as np

# Caminho relativo das pastas de entrada e saída de imagens
INPUT_DIR = os.path.join('data', 'input')
OUTPUT_DIR = os.path.join('data', 'output')


def in_file(filename):
    '''Retorna o caminho de um arquivo de entrada'''

    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    '''Retorna o caminho de um arquivo de saída'''

    return os.path.join(OUTPUT_DIR, filename)

def show_vertical(im1, im2):
    '''Retorna as imagens concatenadas na vertical'''

    im = Image.fromarray(np.vstack((np.array(im1), np.array(im2))))
    im.show()
    return im

def show_horizontal(im1, im2):
    '''Retorna as imagens concatenadas na horizontal'''

    im = Image.fromarray(np.hstack((np.array(im1), np.array(im2))))
    im.show()
    return im