# CS6242-GroupProject
CSE6242 / CX4242 Data and Visual Analytics Group project

DESCRIPTION

This project is a bird-identification application, which allows users to upload an image of a bird, and receive information on the top three most likely bird species, based on a 450 bird species dataset on Kaggle. It utilizes a Convolutional Neural Network to make the species predictions.

The CODE folder contains two sub-folders: Flask_Implementation and Model_Creation
Model_Creation contains the ipython notebooks that were used to train and test the model.
Flask_Implementation contains the final code, which uses the already-trained model.

INSTALLATION

The trained model can be downloaded by going to https://gatech.box.com/s/8hzdn1iwrlbob4tqo0ukexnymgzhbgdq. Once downloaded, move to the Flask_Implementation/model/variables folder.
If you want to train the model yourself, you need to run BIRD_train.ipynb, which requires a Kaggle API code.

The model reading requires the installation of certain python modules, like tensorflow/keras. Some users have reported issues with certain machines, but on our test computer (MacBook Air), it ran within a conda environment with the following modules/versions:

python = 3.8.5
werkzeug, flask = 2.2.2
keras, tensorflow = 2.10.0
numpy = 1.23.5
Pillow = 9.3.0

EXECUTION

To run the Flask environment, navigate to the Flask_Implementation directory and run

python3 app.py

from the command line. Then navigate to http://127.0.0.1:5000 in your browser to see the project. Click 'start', then upload the image you would like to identify and submit the image. You should be presented with the top three guesses. If you would like to upload another image, merely follow the button at the bottom of the page to return to the previous page.
