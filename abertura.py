from PIL import Image
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def in_file(filename):
    return os.path.join(INPUT_DIR, filename)

# abre a imagem
image = Image.open(in_file("pensador.jpg"))
# exibe o valor do pixel na posição (500, 500)
print(image.getpixel((500,500)))
# exibe a imagem
image.show()

# Vídeo: O que é uma imagem? 
# https://youtu.be/T9V_axU6jU8