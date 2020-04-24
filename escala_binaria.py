import os
from PIL import Image

def binary(grayscale, threshold):
    w, h = grayscale.size
    img = Image.new("L", (w, h), (255) )

    for x in range(w):
        for y in range(h):
            pixel = grayscale.getpixel((x,y))
            if (pixel[0] < threshold):
                img.putpixel((x,y), (0))
    return img

if __name__ == "__main__":
    img_grayscale = Image.open("output/pb_baloes2.jpg")
    
    # Ao adicionar o algoritmo do otsu se encontra o ponto de corte ideal
    image = binary(img_grayscale,75)
    image.show()
    image.save(os.path.join("output", "baloes-binario.jpg"))