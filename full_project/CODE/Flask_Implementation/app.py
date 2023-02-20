from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import keras
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
import os
import csv

def classify(img_path, model, label_map, top_n=3):
  img = image.load_img(img_path, grayscale=False, target_size=(224, 224))
  input_arr = image.img_to_array(img)
  input_arr = np.expand_dims(input_arr, axis=0)
  input_arr = preprocess_input(input_arr) # preprocess function specific to ResNet50

  predictions = model.predict(input_arr)

  top_n_indices = np.argpartition(predictions[0], -top_n)[-top_n:] # gets top_n prediction indices
  top_n_indices = top_n_indices[np.argsort(predictions[0][top_n_indices])] # sorts by prediction confidence
  top_n_indices = top_n_indices[::-1] # reverses array so that sorted most to least confident

  classes = []
  for index in top_n_indices:
    classes.append([label_map[index], f"{predictions[0][index]*100:.3f}"])
  return classes

model_path = "model"
model = keras.models.load_model(model_path)

# map label with index
lmap_path = "model/label_map.txt"
if not os.path.exists(lmap_path):
	# If this doesn't exist, you need to download the training data from Kaggle and put in content folder
	test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
	test_generator = test_datagen.flow_from_directory('content/train',
	                                                  target_size=(224, 224),
	                                                  batch_size=32,
	                                                  class_mode='categorical')

	label_map = (test_generator.class_indices) # maps index in predict array to species name
	with open(lmap_path, "w") as f:
		for k, v in label_map.items():
			f.write(f"{v},{k}\n")
	label_map = {v: k for k, v in label_map.items()}
else:
	label_map = {}
	for line in open(lmap_path, "r"):
		line = line.split(',')
		label_map[int(line[0])] = line[1][:-1]


def class_csv():
	csv_path = "content/wiki_info.csv"
	class_info = {}
	with open(csv_path, newline='') as csvfile:
		for row in csv.reader(csvfile):
			class_info[row[0].upper()] = [row[1], row[2], row[3]]

	return class_info


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploaded/image'

@app.route('/')
def homepage():
	return render_template('index.html')


@app.route('/uploader', methods = ['GET','POST'])
def upload():
	return render_template('frame-2.html')

@app.route('/result', methods = ['GET','POST'])
def result():
	if request.method == 'POST':
		f = request.files['file']
		if not os.path.exists(app.config['UPLOAD_FOLDER']):
			os.mkdir(app.config['UPLOAD_FOLDER'])
		img_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
		print(img_path)
		rtn = f.save(img_path)
		print(rtn)
		pred = classify(img_path, model, label_map, top_n=3)
		[name1, conf1] = pred[0]
		[name2, conf2] = pred[1]
		[name3, conf3] = pred[2]
		class_info = class_csv()

		return render_template('frame-3.html', 
				name1=name1, conf1=conf1, desc1=class_info[name1][0], img1=class_info[name1][1], wiki1=class_info[name1][2],
				name2=name2, conf2=conf2, desc2=class_info[name2][0], img2=class_info[name2][1], wiki2=class_info[name2][2],
				name3=name3, conf3=conf3, desc3=class_info[name3][0], img3=class_info[name3][1], wiki3=class_info[name3][2],)


if __name__ == '__main__':
	app.run(debug = True)





