import flask
import werkzeug
import numpy
import scipy.misc

import os.path
import json
from flask import Flask, request, Response

import joblib
from PIL import Image
import random
from matplotlib.pyplot import imread, imshow, imsave
import numpy as np
import cv2
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from random import seed
from random import randint
import math
import statistics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



def detectCirces(im):
    img = cv2.imread(im,1)

    #----------  Detect Circles  -----------

    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(grey_img, (21,21),cv2.BORDER_DEFAULT)
    # Apply Hough transform on the blurred image.
    all_circles = cv2.HoughCircles(blurred_img, cv2.HOUGH_GRADIENT,0.9,120,param1=50,param2=30, minRadius = 60,maxRadius = 150)
    
    coinImages=[]  # array of individua coin images 
    if all_circles is not None:
        all_circles_rounded = np.uint16(np.around(all_circles))
#         print('Circes Detected = '+ str(all_circles_rounded.shape[1]))
        #----------  Draw detected circles  -----------
        for i  in all_circles_rounded[0,:]:
          cv2.circle(img,  ( i[0],i[1]), i[2] , (50,200,200), 5)
#         imshow(img,cmap='gray')

        #----------  Remove Background and create seperate images per coin  ------
        imgColored = imread(im)  # reag again, coloured image
        
        X, Y = np.ogrid[0:imgColored.shape[0], 0:imgColored.shape[1]]         #creates arrays of all x and y coordinates
        for i  in all_circles_rounded[0,:]:

          masked_img = imgColored.copy()
          x=i[0]
          y=i[1]
          rad=i[2]
          mask = (X - y) ** 2 + (Y - x) ** 2 < rad** 2

          masked_img[~mask]=(0,0,0)
    #       coinImages.append(masked_img)
        #----------  Crop Coin
          x=i[0]-i[2]   #  x -rad
          y=i[1]-i[2]    #  y -rad
          h=i[2]*2
          crop_img = masked_img[y:y+h, x:x+h]   #[y:y+h, x:x+w]
          coinImages.append(crop_img)
    return  coinImages
    

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image0']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    #----------------------------
    amount=0
    model = joblib.load('finalized_model.sav')
    # pth='./Android_Flask_0.jpg'
    coinImages = detectCirces(filename)
    for i in range(len(coinImages)):
      coinImages[i]=cv2.resize(coinImages[i],(64,64))
      input=coinImages[i].flatten().reshape(1, -1)
      label=model.predict(input)
      amount+=int(label)

    return str(amount)

app.run(host="0.0.0.0", port=5000, debug=True)
