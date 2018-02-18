import base64
from PIL import Image
import io
import os
import numpy as np
import sys
import keras_mnist

s = sys.argv[1]
s = bytes(s,encoding='utf-8')
r = base64.decodestring(s)

image_string = io.BytesIO(r)
im = Image.open(image_string)
pwd = os.path.dirname(os.path.abspath(__file__))
g_img = im.convert('LA')
g_img.save(pwd + '/g.png')
img2 = np.array(Image.open(pwd + '/g.png'))[:,:,1]
img3 = img2 / 255

# predict
p = keras_mnist.predict(img3)
print("DeepLearning recognizes your number as " + str(p))
