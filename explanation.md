# Marketplace Item Condition Prediction

## Introduction

In the context of an online marketplace, accurately predicting whether a listed item is **new** or **used** is crucial for improving the user experience, facilitating search functionality, and optimizing product recommendations. The goal of this exercise is to develop a **machine learning model** capable of classifying the condition of an item based on a provided dataset.

The dataset, `MLA_100k.jsonlines`, contains information about various items listed on the marketplace, including features that may help differentiate between new and used items. The challenge is to use this data to design, train, and evaluate a machine learning model that can predict the item's condition as **new** or **used**.

## Problem Overview

The steps involved in solving this problem are as follows:

1. **Data Preprocessing:** Load and clean the dataset to ensure it is ready for model training. This includes handling missing values, encoding categorical variables, and normalizing or scaling features as necessary.
  
2. **Model Training:** Select and train a suitable machine learning algorithm to classify items as new or used. Various algorithms, such as decision trees, random forests, logistic regression, or gradient boosting, can be considered based on the nature of the data.

3. **Evaluation:** Choose an appropriate metric to evaluate model performance. Since this is a binary classification task, metrics such as accuracy, precision, recall, F1-score, or AUC-ROC can be used to assess the model's effectiveness on a held-out test dataset.

4. **Results Interpretation:** After training the model, analyze its performance using the chosen metric and document the findings.

## Deliverables

- **Notebook(s):** Containing the entire process of data preprocessing, model training, and evaluation.
- **Explanation.md:** A markdown file with a concise explanation of the criteria applied to train the model and the results obtained using the selected evaluation metric.

By the end of this task, the aim is to have a robust model that can predict whether an item is new or used, along with an understanding of its performance based on the selected metric.

