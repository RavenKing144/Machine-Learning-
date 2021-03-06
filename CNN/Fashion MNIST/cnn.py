# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G0hN0BrIOsIH7fxSghKraKDkR7ekdfM0
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import cv2 as cv
import os
from PIL import Image
from keras.models import Sequential
from keras.layers import Input,Convolution2D,MaxPool2D,Flatten,Dense,Dropout
from keras.utils import np_utils
import tensorflow

"""Data Preparation"""

x = pd.read_csv("fashion-mnist_test.csv")
X = np.array(x)
X = X[:,1:]
X = X/255
y = X[:,0]
print(X.shape)
print(y.shape)

np.unique(y, return_counts=True)

X_train = X.reshape((-1,28,28,1))
Y_train = np_utils.to_categorical(y)
print(X_train.shape,Y_train.shape)

for i in range(10):
  plt.imshow(X_train[i].reshape(28,28),cmap = 'gray')
  plt.show()

"""CNN Model"""

model = Sequential()
model.add(Convolution2D(32,(3,3),activation = 'relu', input_shape=(28,28,1)))
model.add(Convolution2D(64,(3,3),activation = 'relu',))
model.add(Dropout(0.25))
model.add(MaxPool2D(2,2))
model.add(Convolution2D(32,(5,5),activation = 'relu',))
model.add(Convolution2D(8,(5,5),activation = 'relu',))
model.add(MaxPool2D(2,2))
model.add(Flatten())
model.add(Dense(2,activation='softmax'))
model.summary()

model.compile(loss="sparse_categorical_crossentropy",optimizer='adam',metrics=['accuracy'])

hist = model.fit(X_train, Y_train,epochs=20,shuffle=True,batch_size=250,validation_split=0.20)

plt.figure(0)
plt.plot(hist.history['loss'],'g')
plt.plot(hist.history['val_loss'],'b')
plt.plot(hist.history['acc'],'r')
plt.plot(hist.history['val_acc'],'black')
plt.show()