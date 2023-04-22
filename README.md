# Deep-Learning
Note: The following cases were only run for 3 epochs because of the system's computational inadequacy
configuration:CNN-1 layer 128 kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.001 
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 226s 5ms/step - loss: 1.3475 - acc: 0.7031 - val_loss: 0.3847 - val_acc: 0.8932
Epoch 2/3
50000/50000 [==============================] - 225s 5ms/step - loss: 0.3487 - acc: 0.8988 - val_loss: 0.2668 - val_acc: 0.9226
Epoch 3/3
50000/50000 [==============================] - 226s 5ms/step - loss: 0.2738 - acc: 0.9184 - val_loss: 0.2263 - val_acc: 0.9346
Test loss: 0.2310860241264105
Test accuracy: 0.932
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configuration:CNN-1 layer 128kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.01 
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 226s 5ms/step - loss: 0.4748 - acc: 0.8665 - val_loss: 0.1754 - val_acc: 0.9485
Epoch 2/3
50000/50000 [==============================] - 226s 5ms/step - loss: 0.1440 - acc: 0.9556 - val_loss: 0.1168 - val_acc: 0.9652
Epoch 3/3
50000/50000 [==============================] - 226s 5ms/step - loss: 0.1013 - acc: 0.9686 - val_loss: 0.0928 - val_acc: 0.9725
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configuration:CNN-1 layer 128kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.05 
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 225s 5ms/step - loss: 0.3047 - acc: 0.9083 - val_loss: 0.0789 - val_acc: 0.9777
Epoch 2/3
50000/50000 [==============================] - 222s 4ms/step - loss: 0.0665 - acc: 0.9795 - val_loss: 0.0648 - val_acc: 0.9811
Epoch 3/3
50000/50000 [==============================] - 224s 4ms/step - loss: 0.0356 - acc: 0.9891 - val_loss: 0.0462 - val_acc: 0.9859
Test loss: 0.04253744101373013
Test accuracy: 0.9854
Test loss: 0.09429743888936937
Test accuracy: 0.9688
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configuration:CNN-1 layer 128kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.1 

x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 224s 4ms/step - loss: 0.4606 - acc: 0.8627 - val_loss: 0.0831 - val_acc: 0.9764
Epoch 2/3
50000/50000 [==============================] - 223s 4ms/step - loss: 0.0686 - acc: 0.9786 - val_loss: 0.0635 - val_acc: 0.9821
Epoch 3/3
50000/50000 [==============================] - 223s 4ms/step - loss: 0.0419 - acc: 0.9874 - val_loss: 0.0610 - val_acc: 0.9824
Test loss: 0.06021976371346973
Test accuracy: 0.9819
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configuration:CNN-1 layer 128kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.1, batch size=1
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 34110s 682ms/step - loss: 2.5342 - acc: 0.0998 - val_loss: 2.4954 - val_acc: 0.1030
Epoch 2/3
50000/50000 [==============================] - 7430s 149ms/step - loss: 2.5337 - acc: 0.1000 - val_loss: 2.4241 - val_acc: 0.1009
Epoch 3/3
50000/50000 [==============================] - 7442s 149ms/step - loss: 2.5316 - acc: 0.1022 - val_loss: 2.5071 - val_acc: 0.0983
Test loss: 2.500949384689331
Test accuracy: 0.0982
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configuration:CNN-1 layer 128kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.1, batch size=32
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 426s 9ms/step - loss: 0.2993 - acc: 0.9183 - val_loss: 0.1438 - val_acc: 0.9606
Epoch 2/3
50000/50000 [==============================] - 428s 9ms/step - loss: 0.1524 - acc: 0.9626 - val_loss: 0.1591 - val_acc: 0.9593
Epoch 3/3
50000/50000 [==============================] - 427s 9ms/step - loss: 0.1544 - acc: 0.9661 - val_loss: 0.2447 - val_acc: 0.9583
Test loss: 0.2440467735814814
Test accuracy: 0.956
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configuration:CNN-1 layer 128kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.1, batch size=128

x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 224s 4ms/step - loss: 0.4606 - acc: 0.8627 - val_loss: 0.0831 - val_acc: 0.9764
Epoch 2/3
50000/50000 [==============================] - 223s 4ms/step - loss: 0.0686 - acc: 0.9786 - val_loss: 0.0635 - val_acc: 0.9821
Epoch 3/3
50000/50000 [==============================] - 223s 4ms/step - loss: 0.0419 - acc: 0.9874 - val_loss: 0.0610 - val_acc: 0.9824
Test loss: 0.06021976371346973
Test accuracy: 0.9819
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
configuration:CNN-1 layer 128kernel
  followed by Feed Forward- 3 layer 512 unit  
              momentum=0.9, LR=0.1, batch size=1024

x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 50000 samples, validate on 10000 samples
Epoch 1/3
50000/50000 [==============================] - 190s 4ms/step - loss: 3.5711 - acc: 0.2732 - val_loss: 2.0078 - val_acc: 0.3183
Epoch 2/3
50000/50000 [==============================] - 171s 3ms/step - loss: 2.1455 - acc: 0.2442 - val_loss: 1.5281 - val_acc: 0.4706
Epoch 3/3
50000/50000 [==============================] - 172s 3ms/step - loss: 0.6446 - acc: 0.7912 - val_loss: 0.2614 - val_acc: 0.9259
Test loss: 0.2470146568208933
Test accuracy: 0.9272
