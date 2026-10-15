# Machine Learning Exercise with Python

## Create Virtual Environment
- Navigate to the directory where you want to create your virtual environment:

  $ `cd /path/to/myproject`

- Once you are in the desired directory, run the following command to create a virtual environment. You can choose a name for your virtual environment, such as "myvenv", "env", or any other name you prefer:

  $ `python3 -m venv myvenv`

  After running the above command, a new directory named "myvenv" (or the name you specified) will be created in your current directory. This directory will contain the necessary files for your virtual environment.

- Activate the virtual environment based on your operating system:

  $`myvenv/Scripts/activate`

  Once activated, you will notice that the command prompt changes, indicating that you are now working within the virtual environment.

## Install Pandas

Pandas is a widely-used open-source Python library for data manipulation and analysis. It provides easy-to-use data structures and data analysis tools for handling structured data, such as tabular data and time series data. Pandas is built on top of the NumPy library and is a fundamental tool in the data science ecosystem.

- $ `pip install pandas`

## Create a Jupyter Notebook

A Jupyter Notebook is an open-source web application that allows you to create and share documents containing live code, visualizations, explanatory text, and more. It provides an interactive computing environment that supports various programming languages, including Python, R, Julia, and others.


- Add a file with `.ipynb` extension (e.g., "my_notebook.ipynb")

## Highlevel Steps
- Import Data
- Clean Data
- Split Data into Training and Test Sets
- Create a Model
- Train Model
- Make Predictions
- Evaluate and Improve

## Popular Libraries
- Numpy
- Pandas
- MatPlotLib
- Scikit-Learn

---
## Linear Regression

- `y = b1 * x1 + b2 * x2 + ... bk * xk + a`
  - y = depedent variable
  - b = regression coefficients
  - x = independent variable

## Logistic Regression

- In a __linear regression__, the dependent variable is a matric variable, e.g. __salary__ or __electricity consumption__.

- In a __logistic regression__, the dependent variable is a __dichotomous variable__.

  - __Dichotomous variables__ are variables with only __two vallues__.

  - For example: 
    - Whether a person __buys__ or does __not buy__ a particular product.
    - Whether a condition is __present__ or __not__.
    - It's like a `boolean`. 1: Yes/True, 0: No/False

- The goal of logistic regression is to estimate the __probability__ of occurance. The value range for the prediction should therefore be between __0__ and __1__.
---