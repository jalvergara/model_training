# Predictive model training process.

## Exercise description.

El objetivo de este proyecto es desarrollar un **modelo de aprendizaje automático** capaz de predecir si un producto que aparece en un mercado es nuevo o usado, utilizando el conjunto de datos *MLA_100k.jsonlines*. Después de un análisis exhaustivo de las características, se implementaron varios modelos de aprendizaje automático, incluidos **Random Forest, Gradient Boosting, K-Nearest Neighbors, Logistic Regression y XGBoost**. Se evaluaron métricas de precisión para determinar el rendimiento de cada modelo. Este análisis busca optimizar la clasificación de la condición del producto, lo que afecta los precios y las estrategias de venta de los vendedores.

## Dataset Overview.

El conjunto de datos utilizado proviene de un archivo JSON Lines que contiene información del *producto* que figura en un mercado en línea.
Cada fila representa un producto con varias características, como:

* **Columnas numéricas:** representan características como base_price, sold_quantity, píxeles, etc.
* **Columnas categóricas:** incluyen características como buying_mode, status y shipping_mode.
* **Columnas booleanas:** Incluye columnas como, garantía, acepta_mercadopago y relista_automática.


## Data transformations.

Eliminamos columnas innecesarias y manejamos los valores faltantes.
El conjunto de datos original contenía aproximadamente *100 000 productos.* 
Algunas de las transformaciones que se realizaron fueron:

* Se eliminaron 35 columnas que no contribuían al modelo.
* La variable condition se transformó en un valor binario:
*1:* producto nuevo.
*0:* producto usado.
* convertimos las columnas de fecha a datetime y luego al formato YYYYMMDD.

Estas transformaciones mejoran la calidad del conjunto de datos, haciéndolo más adecuado para el análisis exploratorio y el modelado predictivo.

## Model evaluation.

La columna *Target* es **condition**, que indica si el producto es nuevo o usado.
Consideramos varios modelos de aprendizaje automático y los evaluamos con diferentes métricas:

* **Logistic Regression.**
* **Random Forest.**
* **XGBoost.**
* **Gradient Boosting.**
* **K-Nearest Neighbors (KNN).**

Lo que hice fue leer los datos limpios, verificar las columnas que estaban allí para entrenar cada modelo.
Luego definí el vector *X* (todas las columnas excepto la columna de condition) e y (condition).
Luego, el conjunto de datos se divide en *entrenamiento y prueba*, con el **80%** de los datos para entrenamiento y el **20%** para prueba (test_size=0.2).
En cada modelo, el entrenamiento, las predicciones y la evaluación del modelo se realizan con la métrica Acuracy.
Identifica el modelo con la mayor precisión y lo guarda mediante *joblib.*


## Model selection and results.

Los modelos lograron las siguientes precisiones:

* **Accuracy Logistic Regression:** 0.7095
* **Accuracy Random Forest:** 0.76685
* **Accuracy XGBoost:** *0.78515*
* **Accuracy Gradient Boosting:** 0.76995
* **Accuracy KNN:** 0.72995

El clasificador *XGBoost* logró la mayor precisión **(0,78515)**, lo que lo convierte en el modelo con mejor rendimiento.

## Conclusion.

El proceso de entrenamiento y evaluación del modelo permitió identificar al clasificador XGBoost con un accuracy de **0.78515**, como el modelo más adecuado para *predecir* si un artículo en el mercado es nuevo o usado.

Mejor modelo: el clasificador XGBoost mostró la mayor precisión **(0.78515)**.
Finalmente se guarda este modelo como *(modelo_xgboost.pkl)*.
