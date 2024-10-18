# Model Training Explanation

## Dataset Overview
The dataset used for this project contains 100,000 entries and 66 columns. The target variable is `condition_dummy`, a binary variable representing whether an item is new (`1`) or used (`0`). We aim to build a predictive model using various machine learning algorithms to classify items based on their condition.

## Data Preprocessing
For this analysis, we selected the following features to train our models:
- `price`: The current price of the item.
- `base_price`: The base price of the item.
- `sold_quantity`: The quantity of items sold.
- `available_quantity`: The quantity of items available.
- `accepts_mercadopago`: Whether MercadoPago is accepted as a payment method.
- `local_pick_up`: Whether local pickup is available.
- `free_shipping`: Whether the item offers free shipping.

All features were checked for missing values, and no missing data was found in the selected columns. The dataset was split into 80% training data and 20% test data.

## Models Used
We tested three machine learning models:
1. **Logistic Regression**: A simple linear model used for binary classification.
2. **Random Forest**: A powerful ensemble learning method that builds multiple decision trees.
3. **K-Nearest Neighbors (KNN)**: A model based on the idea that similar points exist close to one another in feature space.

## Model Results

| Model               | Accuracy  |
|---------------------|-----------|
| Logistic Regression | 71.16%    |
| Random Forest       | 79.61%    |
| KNN                 | 77.92%    |

### Logistic Regression
- **Accuracy**: 71.16%
- The logistic regression model performed relatively well, achieving an accuracy of 71.16%. This is a reasonable baseline model given the simplicity of the algorithm, but more complex models are expected to perform better given the nature of the data.

### Random Forest
- **Accuracy**: 79.61%
- Random Forest was the best performing model, with an accuracy of 79.61%. This is likely due to the ability of ensemble models to capture non-linear relationships and interactions between the features. Random Forest is a robust choice when handling a mix of categorical and numerical data.

### K-Nearest Neighbors (KNN)
- **Accuracy**: 77.92%
- The KNN model achieved an accuracy of 77.92%. Although slightly lower than Random Forest, it still performed better than logistic regression. However, KNN may not be the best choice for large datasets due to its high computational cost.

## Conclusions

From the results, we can conclude that Random Forest is the most suitable model for predicting the condition of an item (new vs. used) based on the available features. The following key insights were gained from the analysis:
- **Feature Importance**: Price-related features such as `price` and `base_price` are likely to have the most significant impact on the model's performance. The `sold_quantity` and `available_quantity` features also provide important information about the state of the product.
- **Model Performance**: While all models provided reasonable results, the Random Forest model outperformed both Logistic Regression and KNN, indicating its strength in handling complex relationships between features.
- **Next Steps**: Future work could include feature engineering to extract more information from existing columns, tuning the hyperparameters of the Random Forest model to improve performance further, and evaluating additional models like Gradient Boosting.

Overall, the predictive accuracy achieved by Random Forest shows promise for classifying items based on their condition in the marketplace.

