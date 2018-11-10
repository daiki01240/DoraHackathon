# init
from PIL import Image
import numpy as np
import os
import helper
import shutil

# input   = '/Users/Yoshiharu/Desktop/dora/images/dog_sample1.jpeg'
# path    = os.path.dirname(input)
# nCrop   = 3
def image_cropper(input, path, nCrop):

    # prepare
    im      = Image.open(input)
    imgwidth, imgheight     = im.size
    cropwidth, cropheight   = imgwidth/nCrop, imgheight/nCrop

    # crop
    k = 1
    p = os.path.join(path, "tmp")
    if not os.path.isdir(path):
        os.mkdir(p)
    else:
        shutil.rmtree(p)
        os.mkdir(p)
    for i in range(0, imgheight, cropheight):
        for j in range(0, imgwidth, cropwidth):
            if not (i + cropheight > imgheight or j + cropwidth > imgwidth):
                box = (j, i, j+cropwidth, i+cropheight)
                a = im.crop(box)
                a.save(os.path.join(p, "IMG-%s.png" % k))
                k += 1

    # return save path
    return(p)