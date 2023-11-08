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


## Files with dependencies
	Pipenv and Pipenv.lock
	Dockerfile

## Deployment
	Deployment via cloud could not be completed before time ran out
