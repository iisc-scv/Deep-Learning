
from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv3D, MaxPooling3D
from keras import backend as K
from keras.optimizers import SGD

batch_size = 128
num_classes = 10
epochs = 15

# input image dimensions
img_rows, img_cols = 32, 32

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 3, img_rows, img_cols)
    x_train = x_train.reshape(-1, 32, 32, 3, 1)
    x_test = x_test.reshape(x_test.shape[0], 3, img_rows, img_cols)
    x_test = x_test.reshape(-1, 32, 32, 3, 3)
    input_shape = (3, 1 ,img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 3)
    print("x_train:{}".format(x_train.shape))
    x_train = x_train.reshape(-1, 32, 32, 3, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 3)
    x_test = x_test.reshape(-1, 32, 32, 3, 1)
    input_shape = (3, img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
print(y_train.shape)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv3D(32, kernel_size=(3, 3, 3), activation='relu', input_shape=(32,32,3,1)))
model.add(MaxPooling3D(pool_size=(2, 2, 1)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
print (model.summary())

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=SGD(lr=0.01,momentum=0.9),
              metrics=['accuracy'])

model.fit(x_train[0:42000], y_train[0:42000],
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_train[0:42000, :, :, :, :], y_train[0:42000:, :]))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

