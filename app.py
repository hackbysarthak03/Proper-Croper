from flask import Flask, render_template, request
import requests
import pickle
from datetime import datetime
import pandas as pd
import os

# Libraries needed for Image Classification
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

# API Key
API_KEY = 'https://api.thingspeak.com/channels/2598198/feeds.json?api_key=7P0YO4ZEQRR3GIT1&results=2'

# Crop Prediction Model ( .pkl )
file_path = "Crop-Predict.pkl"
model = pickle.load(open(file_path, 'rb'))

# ===================================================================
@app.route('/')
def hello_world():
    return render_template('index.html')


# ===================================================================
@app.route('/predict-crop')
def predict():
    r = requests.get(API_KEY)
    r = r.json()

    lst = []
    values = {
        'temperature' : 22.87,
        'humidity' : 68,
        'n_value' : 84,
        'p_value' : 57,
        'k_value' : 25,
        'ph_value' : 6.5,
        'rainfall' : 64,
        'utc': datetime.strptime('2024-07-17T08:23:35Z', '%Y-%m-%dT%H:%M:%SZ')
    }

    lst.append([values['n_value'], values['p_value'], values['k_value'], values['temperature'], values['humidity'], values['ph_value'], values['rainfall']])
    predicted = model.predict(lst)[0][0]
    data = {
        'value':values,
        'predict':predicted
    }
    return render_template('prediction.html', data = data)


# ==============================================================================================
@app.route('/npk-compare')
def npk():
    r = requests.get(API_KEY)
    r = r.json()

    lst = []
    values = {
        'temperature' : 22.87,
        'humidity' : 68,
        'n_value' : 84,
        'p_value' : 57,
        'k_value' : 25,
        'ph_value' : 6.5,
        'rainfall' : 64,
        'utc': datetime.strptime('2024-07-17T08:23:35Z', '%Y-%m-%dT%H:%M:%SZ')
    }
    lst.append([values['n_value'], values['p_value'], values['k_value'], values['temperature'], values['humidity'], values['ph_value'], values['rainfall']])
    predicted = model.predict(lst)[0][0]

    

    return 'This is NPK Comparison Page'

@app.route('/submit', methods = ['POST'])
def submit():
    r = requests.get(API_KEY)
    r = r.json()

    lst = []
    values = {
        'n_value' : 84,
        'p_value' : 57,
        'k_value' : 25,
        'utc': datetime.strptime('2024-07-17T08:23:35Z', '%Y-%m-%dT%H:%M:%SZ')
    }

    lst.append([values['n_value'], values['p_value'], values['k_value']])
    crop = request.form['crop']
    dataset = pd.read_csv('static\Crop_recommendation.csv')
    var = dataset.groupby('label').get_group(crop)

    data = {
        'value' : values,
        'crop' : crop,
        'extremes' : {
            'max_n':var['N'].max(),
            'min_n':var['N'].min(),
            'max_p':var['P'].max(),
            'min_p':var['P'].min(),
            'max_k':var['K'].max(),
            'min_k':var['K'].min(),
        }
    }
    return render_template('npk.html', data = data)



# ========================================================================================


# Image Prediction Model ( .h5 )
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Load image and resize to 224x224
    img_array = image.img_to_array(img)  # Convert image to numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension
    return img_array

def predict_image_class(image_model, img):
    img = preprocess_image(img)
    result = image_model.predict(img)
    predicted_class = np.argmax(result, axis=1)
    return predicted_class[0]

@app.route('/predict', methods=['POST'])
def upload():
    image_model = load_model('disease_model.h5')
    # Get the file from post request
    f = request.files['file']

    # Save the file to ./uploads
    filename = f.filename
    file_path = os.path.join('static','Images','uploads', filename)
    f.save(file_path)

    # Make prediction
    # image_path = 'static\Images\PotatoHealthy1.JPG'
    predicted_class = predict_image_class(image_model, file_path)
    lst = ['Apple_Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy Apple', 'Corn_(maize)    ___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___healthy',   'Corn_(maize)___Northern_Leaf_Blight', 'Potato___Early_blight', 'Potato___healthy',   'Potato___Late_blight', 'Tomato___Bacterial_spot', 'Tomato___healthy',    'Tomato___Tomato_mosaic_virus']

    data = {
        'value': lst[predicted_class],
        'image_path' : file_path
    }
        
    return render_template('disease.html', data = data)
    
from app import app

if __name__ == "__main__":
    app.run(debug=True, port=5000)

