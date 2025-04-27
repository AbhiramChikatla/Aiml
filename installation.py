# Aim: Identification and Installation of python environment towards the artificial intelligence and machine learning,
# installing python modules/Packages Import scikitlearn, keras etc.


# DESCRIPTION:
# Python is one of the most popular programming languages for Artificial Intelligence (AI) and Machine
# Learning (ML) due to its simplicity, readability, and a vast ecosystem of libraries. Installing a Python
# environment properly is crucial for developing AI/ML applications. The process involves installing Python,
# setting up a virtual environment, and installing necessary libraries like scikit-learn, TensorFlow, and Keras,
# which are essential for building and deploying machine learning models.
    

# CODE:
# Here is a sample script to automate the setup process after Python is installed:
# # Step 1: Install Python and ensure it's added to PATH
# # Step 2: Verify Python and pip installation


# python --version
# pip --version
# # Step 3: Create a Virtual Environment
# python -m venv ai_ml_env
# # Step 4: Activate the Virtual Environment
# # On Windows
# .\ai_ml_env\Scripts\activate
# # On MacOS/Linux
# # source ai_ml_env/bin/activate
# # Step 5: Upgrade pip
# pip install --upgrade pip
# # Step 6: Install Required Packages
# pip install scikit-learn keras tensorflow numpy pandas matplotlib seaborn
# # Step 7: Verify Installation
# python -c "import sklearn; import keras; import tensorflow; import numpy; import pandas; import matplotlib;
# import seaborn; print('All packages imported successfully!')"