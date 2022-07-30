# Deploy pHs Machine Learning Model With Flask  
# Author: Mahmoud Basseem I. Mohamed
# affiliation: Chemistry Department, Faculty of Science, Al-Azhar University, Nasr City, Cairo, P.O.11884, Egypt
# Date: 15-07-2022
# Version: 0.1 
#-----------------------------------------------------------------------------------------------------------------------
# Importing the libraries
from tkinter import N
from flask import Flask, render_template, request, Response, jsonify, redirect, url_for, flash, session, abort, send_from_directory
import numpy as np  # Importing the numpy library
import pandas as pd  # Importing the pandas library
import pickle
import sklearn  # Importing the sklearn library
import cv2  # Importing the cv2 library
import os  # Importing the os library
import datetime, time    


# creating the flask app
app = Flask(__name__)

# loading the model
model = pickle.load(open('model/KNeighborsRegressor.pkl', 'rb'))
model_M = pickle.load(open('model/KNeighborsRegressor_M.pkl', 'rb'))
model_D = pickle.load(open('model/KNeighborsRegressor_D.pkl', 'rb'))

# camera object
cap = cv2.VideoCapture(0)

# creating the route for the home page
@app.route('/')
def index():
    return render_template('index.html', title='Home')

# creating the route for the upload page
@app.route('/upload')
def upload():
    return render_template('upload.html', title='Upload')

# creating the route for the predict page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # getting the image from the request
        image = request.files['image']
        # save the images to the local directory
        image.save('./static/images/image.png')
        # loading the image
        img = cv2.imread('./static/images/image.png')
        # extracting the features from the image RGB values at 25,25 axis
        b = img[25, 25, 0]
        g = img[25, 25, 1]
        r = img[25, 25, 2]
        # creating the feature vector
        X = np.array([r, g, b])
        # reshaping the feature vector
        X = X.reshape(-1, 3)
        # predicting the image getting the image from the request after selecting the models from the dropdown menu
        if request.form['model'] == 'model':
            prediction = model.predict(X)
            # returning the prediction to the user
            return render_template('predict.html', prediction_text='The pH value is: {}'.format(prediction), title='Predict')
        elif request.form['model'] == 'model_M':
            prediction = model_M.predict(X)
            # returning the prediction to the user
            return render_template('predict.html', prediction_text='The pH value is: {}'.format(prediction), title='Predict')
        elif request.form['model'] == 'model_D':
            prediction = model_D.predict(X)
            # returning the prediction to the user
            return render_template('predict.html', prediction_text='The pH value is: {}'.format(prediction), title='Predict')   
    else:
        return render_template('upload.html', title='Upload')
    
# creating the route for the camera capture page
@app.route('/camera', methods=['GET', 'POST'])
def camera():
    # if request is post    
    if request.method == 'POST' and request.form.get('click') == 'Capture':
        while True:
            global cap , capture    # capture the video frame
            # open the camera and read the frame
            success, frame = cap.read()
            # if the frame is not empty
            if success:
                # convert the frame to jpeg format
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                # send the jpeg frame to the client
                cv2.imwrite(r'./static/images/image.jpg', frame)
                # loading the image
                img = cv2.imread(r'./static/images/image.jpg')
                # extracting the features from the image RGB values at 25,25 axis
                b = img[25, 25, 0]
                g = img[25, 25, 1]
                r = img[25, 25, 2]
                # creating the feature vector
                X = np.array([r, g, b])
                # reshaping the feature vector
                X = X.reshape(-1, 3)
                # predicting the image
                if request.form['model'] == 'model':
                    prediction = model.predict(X)
                    # returning the prediction to the user
                    return render_template('camera.html', prediction_text='The pH value is: {}'.format(prediction), title='Camera')
                elif request.form['model'] == 'model_M':
                    prediction = model_M.predict(X)
                    # returning the prediction to the user
                    return render_template('camera.html', prediction_text='The pH value is: {}'.format(prediction), title='Camera')
                elif request.form['model'] == 'model_D':
                    prediction = model_D.predict(X)
                    # returning the prediction to the user
                    return render_template('camera.html', prediction_text='The pH value is: {}'.format(prediction), title='Camera')
            # if the frame is empty
            else:
                pass
    # if request is get 
    elif request.method == 'POST' and request.form.get('stop') == 'Stop':
        # close comera cv2 release all windows
        cap.release()
        cv2.destroyAllWindows()
        # return to the home page
        return render_template('index.html', title='Home')
    # I return to the Capture next time: activate the camera    
    else:
        cap = cv2.VideoCapture(0)
        return render_template('camera.html', title='Camera')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)    
        
#-----------------------------------------------------------------------------------------------------------------------


