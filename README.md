[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Breast Cancer Classification using the Diagnostic Wisconsin Breast Cancer Database


## Problem Description
Breast cancer is a leading cause of death among women, and early diagnosis can be of great value in saving lives and alleviating suffering. An accurate model for classifying samples as benign or malignant can be of immense value.

## Data

The dataset is included in the repository.
The original dataset can also be obtained in 3 different ways:
1. It is included in scikit-learn - to access it from within Python, you can type
	 from sklearn.datasets import load_breast_cancer
	 df = pd. load_breast_cancer() 
2. From Kaggle:
	https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
3. From the original repository at UC Irvine ML Repository:
	https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic 

This dataset contains 569 samples, with 212 malignant cases (37%) and 357 benign cases (63%). It provides features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

Attribute Information:

1) ID number
2) Diagnosis (M = malignant, B = benign)
3-32)

Ten real-valued features are computed for each cell nucleus:

a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g) concavity (severity of concave portions of the contour)
h) concave points (number of concave portions of the contour)
i) symmetry
j) fractal dimension ("coastline approximation" - 1)

The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features. For instance, field 3 is Mean Radius, field
13 is Radius SE, field 23 is Worst Radius.

## Notebook
The notebook includes
	Data preparation and data cleaning
	EDA, feature importance analysis
	Model selection process and parameter tuning
 
## Script train.py
The script training.py can be used to:
	Train the final model
	Save it to a file using pickle

## Script predict.py 
The script predict.py can be used to:
	Load the model
	Serve it via a web service Flask 

You can execute predict.py and test.py to test the model on a single sample:

python predict.py
python test.py

The expected output is 

{'malignant': True, 'malignant_probability': 1.0} 

## Files with dependencies
	Pipenv and Pipenv.lock
	Dockerfile

## Setting up the virtual environment

Install pipenv, to create a virtual environment:

	pip install pipenv

Install dependencies using the requirements file:

	pipenv install -r requirements.txt

Activate the virtual environment:

	pipenv shell

Now run

	python train.py
to train and save the best model, and

	python predict.py
	python test.py

to test the saved model on 1 sample

## Dockerization

Build the Docker container:

	docker build -t breast_cancer_diagnostic

Run the Docker container:

	docker run -it -p 9696:9696 breast_cancer_diagnostic:latest

As before, to test that the prediction app is running properly via Docker, you can type

	python test.py

to test the saved model on 1 sample

and the expected output is

{'malignant': True, 'malignant_probability': 1.0}

## Deployment
	
Deployment was carried out using Google Cloud Run

To run the service, go to

https://console.cloud.google.com/run/detail/us-west2/breast-cancer-diagnostic/revisions?project=galvanic-smoke-404607

The URL is 

https://breast-cancer-diagnostic-e7c74nc6ea-wl.a.run.app/

which is specified in

	test_gcloud.py

and once the container is running via Google Cloud Run, you can run

	python test_gcloud.py

to test the saved model on 1 sample

and the expected output is (as before)

{'malignant': True, 'malignant_probability': 1.0}   

Here is a screenshot of the service created on Google Cloud Run:

<img src="https://github.com/Optimistix/Breast_Cancer_Classification_using_Wisconsin_Diagnostic_Data/blob/main/Google_Cloud_Run_Service_Screenshot.png" style="display:block;float:none;margin-left:auto;margin-right:auto;width:100%">
