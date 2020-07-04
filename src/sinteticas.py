from PIL import Image
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

# IMPC02 | Sintetizando Imagens: https://youtu.be/kb8S06dpZiM
def triangulo(size):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    image = Image.new("RGB", (size, size), WHITE)
    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x,y), BLACK)
    
    return image

# IMPC02 | Sintetizando Imagens https://youtu.be/kb8S06dpZiM
def bandeira_franca(height):
    WHITE = (255, 255, 255)
    BLUE = (0, 85, 164)
    RED = (239, 65, 53)
    width = 3*height//2
    offset = width//3

    image = Image.new("RGB", (width, height), WHITE)
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2*offset, y), RED)

    return image

# IMPC02 | Sintetizando Imagens https://youtu.be/kb8S06dpZiM
def bandeira_japao(height):
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)
    width = 3*height//2
    r = 3*height//10
    c = (width//2, height//2)

    image = Image.new("RGB", (width, height), WHITE)
    for x in range(c[0]-r, c[0]+ r):
        for y in range(c[1]-r, c[1]+ r):
            if (x-c[0])**2 + (y-c[1])**2 <= r**2:
                image.putpixel((x, y), RED)

    return image


if __name__ == "__main__":
    teste = triangulo(700)
    teste.save(os.path.join(OUTPUT_DIR, "triangulo.jpg"))
    teste = bandeira_franca(700)
    teste.save(os.path.join(OUTPUT_DIR, "bandeira_franca.jpg"))
    teste = bandeira_japao(700)
    teste.save(os.path.join(OUTPUT_DIR, "bandeira_japao.jpg"))
    print("Imagem salvas na pasta {}".format(OUTPUT_DIR))
    teste.show()