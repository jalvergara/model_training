# Project: Product Condition Prediction in a Marketplace  

## Introduction  
In this project, we developed a machine learning model to predict whether a product listed in an online marketplace is *new or used*, based on several features. The goal is to help sellers identify the condition of their products, influencing pricing and sales strategies.  

---

## Dataset Overview  
The dataset used comes from a *JSON Lines* file containing product information listed on an online marketplace. Each row represents a product with various features, such as:  

- *warranty*: Warranty provided with the product.  
- *base_price*: Product's base price.  
- *price*: Current price.  
- *buying_mode*: Purchase mode (e.g., auction or direct purchase).  
- *sold_quantity*: Quantity of products sold.  
- *shipping_free*: Indicator of whether shipping is free.  

The target column is *condition*, which indicates whether the product is new or used.  

### Data Distribution  
The original dataset contained approximately *100,000 products*. During the data cleaning process:  
- Incomplete rows were removed.  
- The *condition* variable was transformed into a binary value:  
  - 1: *New* product.  
  - 0: *Used* product.  

---

## Data Preprocessing  
### Data Cleaning  
- *Missing values* were removed to avoid bias in the models.  
- *Categorical variables* (such as buying_mode, status, and shipping_mode) were transformed into numerical variables using *One-Hot Encoding*.  

### Data Splitting  
- *Training set*: 70%  
- *Test set*: 30%  

This split ensures model evaluation on unseen data during training.  

---

## Model Selection  
Several machine learning models were tested to predict whether a product is new or used. Below are the models explored:  

1. *Random Forest*  
   - A robust model capable of handling large datasets with many features.  

2. *Gradient Boosting*  
   - Effective for classification tasks by combining multiple weak models.  

3. *K-Nearest Neighbors (KNN)*  
   - Simple and effective for classification tasks.  

4. *Logistic Regression*  
   - Ideal for binary classification by interpreting probabilities.  

5. *XGBoost*  
   - A powerful model optimized for imbalanced data with high performance.  

Each model was evaluated using *accuracy, **AUC-ROC, and the **classification report*.  

---

## Model Evaluation  
### Results  

#### *Random Forest*  
- *Accuracy:* 81.95%  
- *AUC-ROC:* 0.8943  
- *Classification Report:*  
  - Good balance between precision and recall, with a slight tendency to better predict used products.  

#### *Gradient Boosting*  
- *Accuracy:* 81.60%  
- *AUC-ROC:* 0.8872  
- *Classification Report:*  
  - Similar performance to Random Forest, with better predictions for new products.  

#### *XGBoost*  
- *Accuracy:* 82.70%  
- *AUC-ROC:* 0.8997  
- *Classification Report:*  
  - The best overall performance, excelling in predicting new products.  

#### *Logistic Regression*  
- *Accuracy:* 80.50%  
- *AUC-ROC:* 0.8756  
- *Classification Report:*  
  - Comparable performance to Random Forest and Gradient Boosting.  

---

## Saving the XGBoost Model as a .pkl File
After training the models, the *XGBoost* model gave the best performance. We saved it for later use in a **.pkl file**.



## Conclusion  
The *XGBoost* model showed the *best performance*, with:  
- *Accuracy:* 82.70%  
- *AUC-ROC:* 0.8997  

This model is well-suited to predict whether a product is *new or used*, with strong discriminative power between the two classes.