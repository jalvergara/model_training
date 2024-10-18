# Explanation of the Modeling Process

## Introduction

The goal of this analysis is to classify the condition of items (either "new" or "used") based on various features provided in the dataset. We explored multiple machine learning models to identify the one that performs the best in terms of accuracy and other classification metrics.

## Dataset Overview

The dataset contains 94,247 entries and 25 columns, with a mix of numeric, boolean, and categorical data types:

- **Numeric columns**: Represent features such as `base_price`, `sold_quantity`, `pixeles`, etc.
- **Categorical columns**: Include features like `buying_mode`, `status`, and `shipping_mode`.
- **Boolean columns**: For example, `warranty`, `accepts_mercadopago`, and `automatic_relist`.


This was the case because, previously in the EDA, we performed several important transformations on the dataset to prepare it for analysis and modeling. Some of these included:

1. **Data Cleaning**: We removed unnecessary columns and handled missing values, filling them with appropriate substitutes (e.g., filling `original_price` with `price`).

2. **Feature Engineering**: We extracted and computed new features such as:
   - Calculating pixel dimensions for images (`pixeles` and `pixeles_max`).
   - Counting the number of non-Mercado Pago payment methods.
   - Calculating the number of days items were active and days since the last update.

3. **Data Type Conversion**: We converted certain columns to numeric types and coerced errors to NaN, ensuring proper handling of geographic coordinates and pixel dimensions.

4. **Boolean Transformations**: We transformed columns like `warranty`, `seller_contact`, `tags`, and `variations` into boolean values to simplify analysis.

5. **Status Normalization**: The `status` column was standardized to either "active" or "no_active" for clarity.

These transformations enhance the dataset's quality and usability, making it more suitable for exploratory analysis and predictive modeling.

## Data Preprocessing

### 1. Checking Data Types and Distribution

We started by using `df.info()` to inspect the data types and identify any missing values or inconsistencies. The dataset was complete, with no missing values.

### 2. Analyzing the `condition` Column

The `condition` column, which represents our target variable, contains categorical values: "new" and "used". We visualized the distribution of these values using a pie chart.

### 3. Mapping Categorical Values to Numeric

For easier modeling, we mapped the categorical values in the `condition` column to numeric values:
- "used" → 0
- "new" → 1

### 4. Splitting the Data

The dataset was split into features (`X`) and target variable (`y`):
- `X`: All columns except `condition`.
- `y`: The `condition` column.

We then split the data into training and testing sets, with 70% of the data for training and 30% for testing (`test_size=0.3`). We set the `random_state` to 42 for reproducibility.

### 5. Identifying Numeric and Categorical Features

To prepare for data transformation, we identified:
- **Numeric columns**: Integer and float types.
- **Categorical columns**: Object, category, string, and boolean types.

## Data Transformation

We used a `ColumnTransformer` to preprocess the features:
- **Numeric columns**: Standardized using `StandardScaler`.
- **Categorical columns**: One-hot encoded using `OneHotEncoder`.

## Model Selection and Evaluation

### 1. Models Evaluated

We considered various machine learning models to classify the item condition:
- **Logistic Regression**
- **Random Forest Classifier**
- **Decision Tree Classifier**
- **K-Nearest Neighbors**
- **Gradient Boosting Classifier**
- **Naive Bayes**
- **XGBoost Classifier**

### 2. Evaluation Methodology

We defined a function `evaluate_models()` that:
1. Trains each model on the training set.
2. Makes predictions on the testing set.
3. Calculates the accuracy for each model.
4. Displays a classification report showing precision, recall, f1-score, and support.
5. Identifies the model with the highest accuracy and saves it using `joblib`.

### 3. Results

The models achieved the following accuracies:
- **Logistic Regression**: 0.72
- **Random Forest**: 0.83
- **Decision Tree**: 0.77
- **K-Nearest Neighbors**: 0.74
- **Gradient Boosting**: 0.81
- **Naive Bayes**: 0.58
- **XGBoost**: 0.84

The XGBoost classifier achieved the highest accuracy (0.84), making it the best-performing model.

## Conclusion

- **Best Model**: The XGBoost Classifier showed the highest accuracy and was saved as the best model (`best_model_XGB Classifier.pkl`).
- **Worst Model**: The Naive Bayes classifier had the lowest accuracy (0.58), indicating it struggled to classify the instances effectively.


