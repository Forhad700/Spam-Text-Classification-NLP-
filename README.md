# Spam Text Classification

## Overview
This project implemented a **Spam Detection System** focuses on text classification using **Natural Language Processing (NLP)** and **Machine Learning (ML)**. The goal is to classify text messages as either "spam" or "non-spam (ham)".

## Features
- **Spam Classification**: Predicts whether a given text message is spam or non-spam (ham).
- **Web Interface**: Interactive Streamlit app where users can input messages and get instant predictions.
- **Text Preprocessing**: The model includes preprocessing steps such as handling missing values and balancing the dataset.
- **Visualizations**: Data visualizations to explore message length and punctuation distributions for spam vs. ham messages.

### Key Steps:
 * **Data Preprocessing**: The dataset is cleaned and preprocessed to handle missing values, and the data is balanced between spam and non-spam messages.
  **Feature Extraction**: Text data is transformed into numerical features using the **TF-IDF** (Term Frequency-Inverse Document Frequency) technique.
  **Model Training**: A **Random Forest Classifier** is used to train the model to classify the messages based on their features.
  **Model Evaluation**: The model's performance is evaluated on a test set using accuracy, precision, recall, and F1-score.
  **Deployment**: A simple **Streamlit** web application is built to allow users to input messages and get predictions (Spam or Ham).

## Tech Stack

- **Python**: Programming Language.
- **Streamlit**: A framework for building the interactive web app for real-time spam prediction.
- **scikit-learn**: Used for machine learning model training (Random Forest Classifier) and feature extraction (TF-IDF).
- **Pandas**: For data manipulation and handling the dataset.
- **NumPy**: For numerical operations and processing data.
- **Matplotlib**: For creating visualizations to explore the dataset.
- **Pickle**: For saving and loading the trained machine learning model.
