# Synthetic Data Generation and Churn Prediction on Game Data

In this repository, you can find my work to predict **churn** in gaming data using **synthetic datasets**. The primary objective of this project is to predict **player churn** in a gaming environment, specifically focusing on **World of Warcraft**. To make the task more challenging and to create a more realistic dataset, I decided to generate **synthetic data** rather than use an existing one.

## Player Churn Prediction

### Project Overview

This repository contains my project for predicting **player churn** using **synthetic data**. The goal is to build a **machine learning model** that can accurately predict whether a player will churn (stop playing) based on various features. The project includes **data exploration**, **feature engineering**, **model selection**, and **hyperparameter tuning**, all aimed at improving the prediction accuracy.

In this project, I use a combination of data science techniques such as data cleaning, feature engineering, model comparison, and fine-tuning to develop an effective churn prediction model. The final model is a **Gradient Boosting Classifier**, which showed optimal performance in predicting churn.

### Contents

- **Data Exploration**: A detailed analysis of the dataset, including outlier detection, correlation analysis, and feature distribution analysis.
- **Feature Engineering**: The creation of new features, as well as handling outliers using **binning** techniques.
- **Model Selection & Evaluation**: A thorough comparison of multiple machine learning models with cross-validation and hyperparameter tuning to select the best-performing model.
- **Final Model**: **Gradient Boosting Classifier**, selected for its optimal performance after model evaluation.
- **Pipeline**: A reusable pipeline that allows for seamless deployment and future predictions, avoiding the need to retrain the model from scratch.

### Key Steps

The project follows several key steps to ensure the model is well-prepared and optimized for deployment:

1. **Exploratory Data Analysis (EDA)**: 
   - Understanding the dataset and its structure.
   - Detecting trends and relationships between features.
   - Analyzing feature distributions and identifying correlations with churn.

2. **Feature Engineering**:
   - Handling missing data through imputation and interpolation.
   - Creating new features based on domain knowledge.
   - **Handling Outliers**: Outliers were handled using **binning techniques**, ensuring they didn't distort the churn prediction model.

3. **Model Training & Evaluation**:
   - Using various classification algorithms and selecting the best one based on cross-validation scores.
   - Implementing hyperparameter tuning using **GridSearchCV** to fine-tune the **Gradient Boosting Classifier**.

4. **Deployment Pipeline**:
   - Creating a pipeline for easy deployment.
   - Allowing for easy predictions on new data without the need to retrain the model.

## Data Generation

Initially, I referred to the project by **Pelin Ercan**, titled "DETECTION OF CHURNERS IN INTERNET GAMES USING CRM APPROACH: A CASE STUDY ON PISHTI PLUS," advised by **Prof. Dr. Ferda Nur Alpaslan**. Based on this, I started generating data using the **random** and **faker** libraries.

However, I realized this dataset wouldn’t accurately reflect reality. So, I decided to generate **synthetic data** based on a real project whose data I could access. I learned that **synthetic data** can be produced by identifying relationships between different data types even with a small amount of data, and big companies often use such data from smaller-scale firms for their analysis.

## Synthetic Data Generation on World of Warcraft

For this task, I focused on the **World of Warcraft** game and used the **SDV (Synthetic Data Vault)** library. From a dataset of 37,000 rows, I created **20,000 rows** using **GaussianCopulaSynthesizer** with an accuracy rate of **85.48%**. Additionally, I generated another **20,000 rows** using **GAN** with an accuracy rate of **86.60%**.

I found that it was easier to measure accuracy with **SDV** compared to other synthetic data generation libraries. Therefore, I decided to continue using this method for generating synthetic data.

## Files in this Repository

This project contains the following main files:

1. **WoW.jynb**: 
    - A Jupyter Notebook file that contains the code for **data generation**, **data exploration**, **feature engineering**, and **model training**. It provides a step-by-step approach to building and training the churn prediction model.
   
2. **churn.csv**: 
    - The synthetic dataset used for the churn prediction task. This file contains the features related to the player's activities, such as **total_timestamps**, **unique_days**, **max_level**, etc.

3. **model.pkl**: 
    - The **saved model** of the churn prediction task, specifically the **Gradient Boosting Classifier**. This file can be used for future predictions without retraining the model.

## Features in the Dataset

The synthetic data contains the following features:

- **guild**: The community (guild) the player belongs to within the game.
- **total_timestamps**: The total number of timestamps recorded for the player's activities in the game.
- **unique_days**: The number of unique days the player was active.
- **max_level**: The highest level the player has reached.
- **min_month**: The earliest month the player was active in the game.
- **max_month**: The most recent month the player was active in the game.
- **Average_Hour**: The average hour the player plays the game.
- **Average_Playing_density**: The density of the player's gaming activities during specific time periods.

## Dataset Exploration and Preprocessing

### Outliers and Data Cleaning

The dataset did not have any missing values. For outliers, I used **binning techniques** to handle them, ensuring that the churn prediction model remained robust and accurate. The binning method grouped values into discrete ranges, which helped to minimize the impact of outliers on the model's performance.

### Correlation Analysis

I performed correlation analysis to understand the relationships between various features and churn prediction. I found a significant positive correlation between **max_level**, **unique_days**, **total_timestamps**, and **guild** with churn rate.

## Model Selection and Training

### Churn Prediction

After performing feature engineering and preprocessing, I selected classification models to predict player churn. The best model selected was **Gradient Boosting Classifier**, which showed high performance in predicting churn.

To confirm the model's validity, I used **cross-validation** to ensure the model’s performance wasn't due to overfitting. Following this, I applied **GridSearchCV** for hyperparameter tuning to enhance the model's performance further.

### Model Deployment

Once the model was trained, I saved the final model into the **model.pkl** file. This saved model can be loaded and used for future predictions on new data without the need to retrain it.
