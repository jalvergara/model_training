# Explicación de la Selección del Modelo Random Forest

## 1. Análisis Exploratorio de Datos (EDA)

### 1.1. Limpieza de Datos y Selección de Características
- **Conjunto de Datos Inicial**: Comenzamos analizando el conjunto de datos proporcionado, que incluía varias características como `price`, `base_price`, `available_quantity` y `condition` (la variable objetivo).
- **Valores Faltantes**: Las características `original_price` y `catalog_product_id` contenían una cantidad significativa de datos faltantes y fueron eliminadas del análisis para mantener la robustez del modelo.
- **Variables Cualitativas vs Cuantitativas**: Nos centramos en variables cuantitativas como `price`, `base_price` y `available_quantity` para guiar el proceso de modelado. Las variables cualitativas fueron excluidas o transformadas (por ejemplo, `condition` fue transformada en una variable binaria donde `1 = Nuevo` y `0 = Usado`).

### 1.2. Análisis de Correlación
- **Matriz de Correlación**: Se generó una matriz de correlación para examinar las relaciones entre las características. Se encontraron correlaciones moderadas entre variables como `price`, `base_price` y `available_quantity` con la variable objetivo `condition`.
- **Decisión**: A partir de este análisis, se seleccionaron características clave como `price`, `base_price`, `available_quantity` y algunas otras variables relevantes para el proceso de modelado.

## 2. Proceso de Selección del Modelo

### 2.1. Prueba Inicial de Modelos
- **Modelo Base**: Comenzamos probando un modelo sencillo de **Regresión Logística** como línea base. Este modelo mostró un rendimiento bajo, particularmente al predecir la clase **Nuevo**, con una precisión de aproximadamente 0.65.
- **Problema Identificado**: El modelo de regresión logística mostró un sesgo hacia la predicción de más artículos "Usado", clasificando incorrectamente una gran cantidad de artículos "Nuevo".

### 2.2. Decisión de Probar Modelos Basados en Árboles
- Dado el bajo rendimiento del modelo de Regresión Logística, decidimos explorar modelos más complejos basados en árboles, comenzando con **Random Forest**, **XGBoost** y **Gradient Boosting**.
- Estos modelos fueron elegidos por su capacidad para manejar relaciones complejas entre características, así como su efectividad en el manejo de conjuntos de datos desbalanceados.

### 2.3. Comparación de Modelos y Métricas de Evaluación
- **Modelos Probados**:
  - **Random Forest**: Mostró el mejor equilibrio entre precisión y recall en ambas clases.
  - **XGBoost**: Desempeño similar, aunque ligeramente peor que Random Forest.
  - **Gradient Boosting**: Similar a XGBoost, pero también menos preciso que Random Forest.
  
- **Métricas de Evaluación**:
  - Evaluamos los modelos usando **precisión**, **F1-Score** y **matrices de confusión**. Random Forest obtuvo consistentemente el mayor F1-Score (0.79) y el menor número de clasificaciones incorrectas.

## 3. Ajuste de Hiperparámetros para Random Forest
- **Ajuste**: Se realizó un ajuste de hiperparámetros en el modelo Random Forest para optimizar parámetros clave como `n_estimators`, `max_depth` y `min_samples_split`.
- **Mejores Parámetros**: Después del ajuste, el mejor rendimiento se logró con `n_estimators = 300` y `max_depth = 7`.

## 4. Modelo Final: Random Forest

- **Precisión del Modelo**: 0.78625
- **Matriz de Confusión**:
  - [[8283, 1000], [3275, 7442]]
- **Reporte de Clasificación**:
  - **Precisión**: 0.72 para la clase 0 y 0.88 para la clase 1.
  - **Recall**: 0.89 para la clase 0 y 0.69 para la clase 1.
  - **F1-Score**: 0.79 para ambas clases.
  - **Accuracy**: 0.79.
  - **Macro avg**: 0.80 de precisión, 0.79 de recall y 0.79 de F1-Score.
  - **Weighted avg**: 0.81 de precisión, 0.79 de recall y 0.79 de F1-Score.

## 5. Conclusión
El modelo de **Random Forest** fue seleccionado como el modelo final debido a su rendimiento superior en todas las métricas comparado con la Regresión Logística, XGBoost y Gradient Boosting. Su capacidad para clasificar con precisión tanto artículos "Usado" como "Nuevo" con un alto nivel de precisión y recall lo convierte en la mejor opción para este problema de clasificación.
