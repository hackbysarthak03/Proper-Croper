
# Proper-Croper 🌿

### A Crop recommendation and Disease Predicting System
*IOT -> Machine Learning Algorithm -> Flask Based Web-Application*

## Introduction       
Proper-Croper is a Flask based Web- Application used as a Crop Recommendation and Disease Predicting System along with the IOT Sensors.    

***Required IOT Sensors :***
- Arduino UNO
- ESP8266 Wifi
- Soil Moisture Sensor
- DHT 11 Sensor
- NPK Sensor
- pH Sensor

The below 4 Sensors are connected to the Arduino UNO and further the data is sent by the ESP8266 WiFi to the Cloud API. The Flask based Web Application get live updates from the sensor data and Use our Machine Learning Model to predict the best crop. The Disease Predicting System requires the Leaf Image to determine the disease within the plant/crop processed by our Keras Model.

***Machine Learning Model*** 🤖   

The Crop Recommending System has the dataset consisting of Nitrogen, Phosphorus, Potassium, Soil pH, Rainfall of the Area, Soil Temperature and Moisture for the Humidity.    
The Dataset is cleaned using the *Pandas & Numpy* library of Python and further Multiclass Classification methods were experimented, and the best accuracy method for the dataset is used. 

- Random Forest Classification *( Accuracy : 99.81% )*
- Decision Tree Classification *( Accuracy : 98.72% )*
- KNN Classification *( Accuracy : 97.12% )*

Hence, For further prediction, **Crop-Predict.pkl** Model is developed based on Random Forest Classification Method predicting with an accuracy of 99.81%.

The Disease Predicting System is developed using the Dataset available for multiple leaves *(Source: Kaggle)* further Keras and Tensorflow is used to develop the Model and **disease_model.h5** is loaded and used in our Flask Web Application for further Image Processing of the Leaf Image.   








### *Home Screen*

![Home Screen](https://res.cloudinary.com/doy34nvkz/image/upload/v1722441326/Screenshot_2024-07-31_212257_csy8md.png)

### *Crop Recommendation System*

![Home Screen](https://res.cloudinary.com/doy34nvkz/image/upload/v1722441611/Screenshot_2024-07-31_212830_gwm1dx.png)

### *NPK Comparator*

![Home Screen](https://res.cloudinary.com/doy34nvkz/image/upload/v1722441608/Screenshot_2024-07-31_212850_wvpzpj.png)

### *Disease Predicting System*

![Home Screen](https://res.cloudinary.com/doy34nvkz/image/upload/v1722441610/Screenshot_2024-07-31_212944_cvgjeq.png)


## Run Locally

 - Make sure git is installed. 
 - Clone the project by running following command in cmd or terminal: `git clone https://github.com/hackbysarthak03/Proper-Croper.git` or you can simply download the entire repo as zip.
 - Install Anaconda or miniconda and create an environment with Python 3.11. Refer [this tutorial](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) on how to create an environment in conda.
 - Activate environment ` .\env\Scripts\activate.ps1`
 - Install required libraries by running following commands:
	- Scikit-Learn `pip install -U scikit-learn`.
	- NumPy `pip install numpy`.
	- Flask `pip install Flask`.
 - Open new anaconda prompt in project folder and run following command:
  `python app.py`
  - Now project will start running in the terminal. Copy the localhost URL provided in terminal and open it into a web browser to use the application. 

    
## Acknowledgements

The Above Project is a Team Work of Sarthak Vishwakarma ([🚀 Connect on Github](https://github.com/hackbysarthak03)) and Aditya Prajapati ( [🚀 Connect on Github](https://github.com/thesilverwarrior) ).    
Thankyou ECE dept. MMMUT for the resources, the Tech content writer of Docs and the visitors of the Github Project.   

Access the Project Presentation using the [link](https://www.canva.com/design/DAGLfPOP_tQ/0WMiUOnCmGRa38qUqK8kvw/edit?utm_content=DAGLfPOP_tQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) for better understanding.


