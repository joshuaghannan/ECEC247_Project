# -*- coding: utf-8 -*-
"""data_augmentation.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mspvRcDFXus4jLFjUgUPtgrzm95cMxb7
"""

import numpy as np
"""
We will put functions to augment data in here.
Functions in this file:
  window_data
"""

def window_data(X, y, window_size, stride):
  '''
  This function takes in X (a 3-d tensor) of size (#trials x #electrodes x #time 
  series) and y data of size (#trials) and outputs two options for using it. 
  X_new1: The first output stacks the windowed data in a new dimension, resulting 
    in a 4-d tensor of size (#trials x #electrodes x #windows x #window_size).
  X_new2: The second option makes the windows into new trails, resulting in a new
    X tensor of size (#trials*#windows x #electrodes x #window_size). To account 
    for the larger number of trials, we also need to augment the y data.
  y_new:  The augmented y vector of size (#trials*#windows) to match X_new2.
  Some code to visualize what's happening:
  #X_new_wind1, X_new_wind2, Y_new  = window_data(X_train_valid, y_train_valid, 200, 20)
  #print(X_new_wind1.shape)
  #print(X_new_wind2.shape)
  #print(Y_new.shape)
  '''
  num_sub_trials = int((X.shape[2]-window_size)/stride)
  X_new1 = np.empty([X.shape[0],X.shape[1],num_sub_trials,window_size])
  X_new2 = np.empty([X.shape[0]*num_sub_trials,X.shape[1],window_size])
  y_new = np.empty([X.shape[0]*num_sub_trials])
  for i in range(X.shape[0]):
    for j in range(X.shape[1]):
      for k in range(num_sub_trials):
        X_new1[i,j,k:k+window_size]    = X[i,j,k*stride:k*stride+window_size]
        X_new2[i*num_sub_trials+k,j,:] = X[i,j,k*stride:k*stride+window_size]
        y_new[i*num_sub_trials+k] = y[i]
  return X_new1, X_new2, y_new

