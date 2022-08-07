<p align="center">
  <a href="#">
    <img src="https://www.pngall.com/wp-content/uploads/2017/11/Breast-Cancer-Ribbon-PNG-Image.png" alt="" width="200">
  </a>
</p>

<h1 align="center">Breast Cancer Prediction</h1>

## Table of Contents
- [About](#about-the-project)
- [Logistic Regression](#logistic-regression)
- [Why have I used logistic regression in this project?](#why-have-I-used-logistic-regression-in-this-project?)
- [Why I found Logistic Regression to be preferrable in this project?](#why-I-found-Logistic-Regression-to-be-preferrable-in-this-project?)
- [Dataset](#dataset)
- [Working of the Model](#working-of-the-model)
- [Libraries Used](#libraries-used)

## About the Project
In this repository, I have developed a Breast cancer Prediction System using Logistic Regression. I am using Logistic Regression to classify and predict breast cancer.

## Logistic Regression
Logistic regression estimates the probability of an event occurring, such as voted or didn't vote, based on a given dataset of independent variables. Since the outcome is a probability, the dependent variable is bounded between 0 and 1.
<br>
<p align="center"><img src="https://thumbs.gfycat.com/RaggedShorttermHalcyon-size_restricted.gif" width="400"></p>


## Why have I used logistic regression in this project?
Logistic Regression is used when the dependent variable(target) is categorical, such as to predict whether the tumor is malignant (1) or benign (0).

## Why I found Logistic Regression to be preferrable in this project?
Logistic regression analysis is valuable for predicting the likelihood of an event. It helps determine the probabilities between any two classes by analyzing or training on historical data.

## Dataset
I am importing the classified breast cancer wisconsin dataset.
The breast cancer dataset is a classic and very easy binary classification dataset.

    =================   ==============
    Classes                          2
    Samples per class*   212(M),357(B)
    Samples total                  569
    Dimensionality                  30
    Features            real, positive
    =================   ==============

The copy of UCI ML Breast Cancer Wisconsin (Diagnostic) dataset is downloaded from [here](https://goo.gl/U2Uwz2).

### ***Data Set Information***

Features are computed from a digitized image of a **Fine Needle Aspirate (FNA)** of a breast mass. They describe characteristics of the cell nuclei present in the image.

### ***Attribute Information:***

1) ID number
2) Diagnosis (M = malignant, B = benign)
3) Ten real-valued features are computed for each cell nucleus:
    - radius (mean of distances from center to points on the perimeter)
    - texture (standard deviation of gray-scale values)
    - perimeter
    - area
    - smoothness (local variation in radius lengths)
    - compactness (perimeter^2 / area - 1.0)
    - concavity (severity of concave portions of the contour)
    - concave points (number of concave portions of the contour)
    - symmetry
    - fractal dimension (coastline approximation - 1)

## Working of the Model
<p>The dataset is loaded and then the data and targets are separated out. The data consists of 569 instances and 30 features.</p>
<p>
The data is then split into training and testing data by using *train_test_split* funtion of Scikit Learn. There were now 426 training data and 143 testing data, but so many testing data were not required so the *test_size* was assigned as 0.1 that means the 10% of the whole data. Now there are 512 training and 57 testing data.</p>
<p>Then from the mean it was observed that the distribution of the data was not even. So the data was stratified. Now the data was equally distributed among the two targets Malignant[0] and Benign[1].</p>
<table>
<tr><th width="50%">Benign [1]</th><th width="50%">Malignant [0]</th>
</tr>
<tr><td width="50%">Benign refers to a condition, tumor, or growth that is not cancerous. This means that it does not spread to other parts of the body. It does not invade nearby tissue. Sometimes, a condition is called benign to suggest it is not dangerous or serious. In general, a benign tumor grows slowly and is not harmful.</td><td width="50%">Malignancy is the tendency of a medical condition to become progressively worse. Malignancy is most familiar as a characterization of cancer.</td>
</tr>
</table>
<p align="center"><img src="https://www.publichealthnotes.com/wp-content/uploads/2022/04/shutterstock_1493059916.jpg" width="100%"></p>
## Libraries Used
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit Learn" width="30%">

Scikit Learn is a Python module integrating classical machine
learning algorithms in the tightly-knit world of scientific Python
packages (numpy, scipy, matplotlib).

It aims to provide simple and efficient solutions to learning problems
that are accessible to everybody and reusable in various contexts:
machine-learning as a versatile tool for science and engineering.</p>
<hr>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" alt="Pandas" width="30%">

Pandas is a Python package providing fast, flexible, and expressive data
structures designed to make working with "relational" or "labeled" data both
easy and intuitive. It aims to be the fundamental high-level building block for
doing practical, **real world** data analysis in Python. Additionally, it has
the broader goal of becoming **the most powerful and flexible open source data
analysis / manipulation tool available in any language**. It is already well on
its way toward this goal.
</p>
<hr>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1200px-NumPy_logo_2020.svg.png" alt="NumPy" width="30%">

NumPy provides
  - An array object of arbitrary homogeneous items
  - Fast mathematical operations over arrays
  - Linear Algebra, Fourier Transforms, Random Number Generation
</p>
