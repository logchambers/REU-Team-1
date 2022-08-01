from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers
from tensorflow.keras.models import Model
import tensorflow as tf
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.layers import Conv2D, AveragePooling2D, GlobalAveragePooling2D, BatchNormalization

MODE = "imagenet"
VERSION = "trainable"

def getModel():
    if MODE == "noweights":
        weights = None
    elif MODE == "imagenet":
        weights = "imagenet"

    base_model = InceptionV3(input_shape=(256,256,3), include_top=False, weights=weights)
    base_model = VGG16(
        include_top=False,
        weights=weights,
        input_shape=(256,256,3),
    )

    # for layer in base_model.layers:
    #  layer.trainable = False

    x = base_model.output
    x = Conv2D(40, (1, 1), strides = (1, 1), use_bias = False, activation = 'relu')(x) # v2
    x = layers.Flatten()(x)
    x = layers.Dense(512, activation='relu')(x) # v2
    x = layers.Dropout(0.2)(x)

    # Add a final layer with 1 node for classification output
    x = layers.Dense(1, activation='sigmoid')(x)        

    model = Model(base_model.input, x) 

    model.compile(
        optimizer = Adam(lr=0.000005),
        loss = tf.keras.losses.MeanSquaredError(),
    )
    return model

def evaluateModel(model, val, log_dir):
    pass

def getVersion():
    return MODE+"_"+VERSION

def getDataType():
    return "coords"
    # return "coords_small"