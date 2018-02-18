import keras
from keras.models import load_model
model = load_model('keras-mnist.h5')

def predict(ndarray):
    a = model.predict_classes(ndarray.reshape(1,-1), verbose=0)
    return a
