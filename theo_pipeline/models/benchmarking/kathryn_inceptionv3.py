# https://colab.research.google.com/drive/1zJlzB0Le6KNRMzjrTHoM6_TGvni_yNpH?usp=sharing

from tensorflow.keras import layers
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.models import Model
import tensorflow as tf
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.layers import Conv2D, AveragePooling2D, GlobalAveragePooling2D, BatchNormalization

from models.utils import IOU_metric
MODE = "imagenet"
VERSION = "0.02"


# def Hausdorff(y_true, y_pred):
#     return tf.maximum(
#         tf.maximum(

#         )
#     )
#     points = [(0,1), (0,3), (2,1), (2,3)]
#     M1, M2 = 0, 0
#     for p1 in points:
#         m1, m2 = 1e6, 1e6
#         for p2 in points:
#     true = []

def getModel():
    base_model = InceptionV3(input_shape=(256,256,3), include_top=False, weights="imagenet")

    for layer in base_model.layers[:164]:
        layer.trainable = False

    last_layer = base_model.get_layer('mixed6')
    last_output = last_layer.output

    x = layers.Flatten()(last_output)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dropout(0.3)(x) 
    x = layers.Dense(1, activation='sigmoid')(x)           

    model = Model(base_model.input, x) 

    model.compile(
        optimizer = keras.optimizers.Adam(), 
        loss = 'binary_crossentropy', 
        metrics = ['accuracy']
    )
    return model

def evaluateModel(model, val, log_dir):
    pass

def getVersion():
    return MODE+"_"+VERSION

def getDataType():
    return "coords"
    # return "coords_small"