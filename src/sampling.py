from PIL import Image, ImageFilter
import numpy as np
from math import sqrt, cos, sin, pi


NEAREST_NEIGHBOR = 0
BILINEAR = 1

def show(img, res=1080, kernel=NEAREST_NEIGHBOR):
    todisplay = img
    if img.shape[0] != res:
        todisplay = upscale(np.toarray(img), (res, res), kernel)
    todisplay.show()

def circles(x, y, w, n=100):
    r = sqrt(x**2 + y**2)
    value = (cos(2*pi * r/w * n) + 1)/2
    return 255 if 255*value > 127 else 0

def circlescenter(x, y, w, n=20):
    r = sqrt((x - w/2)**2 + (y-w/2)**2)
    ratio = n
    frac = r/sqrt(2*w**2)
      
    value = (cos(2*pi * r/w * n*frac) + 1)/2
    return 255 if 255*value > 127 else 0


def sample_circle(width = 512, n=10, f=circles):
    height = width
    pixels = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            pixels[i, j] = f(j, i, width, n)
    return Image.fromarray(pixels)


def upscale_NN_channel(pixels, nsize):
    nh, nw = nsize
    height, width = pixels.shape[0], pixels.shape[1]

    npixels = np.zeros(nsize)
    dx = (width-1)/(nw-1)
    dy = (height-1)/(nh-1)

    for i in range(nh):
        for j in range(nw):
            x, y = j*dx, i*dy
            intx, inty = int(x), int(y)
            distx, disty = x - intx, y - inty
            if distx > 0.5:
                intx = intx + 1
            npixels[i, j] = (pixels[inty, intx] 
                                if disty <= 0.5 else pixels[inty + 1, intx])
    print(npixels.shape, npixels[0, 0])
    return npixels


def upscale_bilinear_channel(pixels, nsize):
    nh, nw = nsize
    height, width = pixels.shape[0], pixels.shape[1]

    npixels = np.zeros(nsize)
    dx = (width-1)/(nw-1)
    dy = (height-1)/(nh-1)

    for i in range(nh):
        for j in range(nw):
            x, y = j*dx, i*dy
            intx, inty = int(x), int(y)
            distx, disty = x - intx, y - inty
            try:
                h1 = pixels[inty, intx]*distx + (1-distx)*pixels[inty, intx+1]
                h2 = pixels[inty+1, intx]*distx + (1-distx)*pixels[inty+1, intx+1]
                # cast to int
                npixels[i, j] = int(disty*h1 + (1-disty)*h2)
            except IndexError as e:
                x = width-1 if intx + 1 == width else intx + 1
                y = height-1 if inty + 1 == height else inty + 1
                npixels[i, j] = pixels[y, x]

    return npixels

def upscale_nearest_neighbor(pixels, nsize):
    nh, nw = nsize
    pixels = np.transpose(pixels, (2, 0, 1))
    height, width = pixels.shape[1], pixels.shape[2]
    npixels = np.zeros((pixels.shape[0], nh, nw), np.uint8)
    print(npixels.shape, pixels.shape)
    for c in range(pixels.shape[0]):
        npixels[c] = upscale_NN_channel(pixels[c], nsize)
    return Image.fromarray(np.transpose(npixels, (1, 2, 0)))


def upscale(img, nsize, method=NEAREST_NEIGHBOR):
    nh, nw = nsize
    pixels = np.transpose(np.asarray(img, np.uint8), (2, 0, 1))
    # height, width = pixels.shape[1], pixels.shape[2]
    channels = pixels.shape[0]
    npixels = np.zeros((channels, nh, nw), np.uint8)

    if method == NEAREST_NEIGHBOR:
        for c in range(channels):
            npixels[c] = upscale_NN_channel(pixels[c], nsize)
    else:
        for c in range(channels):
            npixels[c] = upscale_bilinear_channel(pixels[c], nsize)
    
    return Image.fromarray(np.transpose(npixels, (1, 2, 0)))
    

if __name__ == "__main__":
    img = sample_circle(512, n=200, f=circlescenter)
    img.show()
    newimg = upscale(img.filter(ImageFilter.BoxBlur(2)), (512, 512), BILINEAR)
    # newimg = upscale(newimg, (512, 512), BILINEAR)
    newimg.show()
    # newimg.save("output/test.png")

    