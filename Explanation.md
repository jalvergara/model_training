# Explanation.md

## Análisis Exploratorio de Datos (EDA)

El análisis exploratorio de datos (EDA) fue la primera fase del proyecto, donde se realizó la limpieza y transformación del dataset. Las acciones principales fueron:

- **Tratamiento de datos faltantes:** Se identificaron columnas con valores nulos y se aplicaron estrategias para manejarlas, como eliminación o imputación según correspondiera.
- **Transformaciones de variables:** Se aplicaron transformaciones logarítmicas a variables numéricas para normalizar la distribución y facilitar su uso en los modelos.
- **Análisis de variables categóricas:** Se analizaron las frecuencias de las categorías presentes en las variables relevantes como la condición del producto, el modo de compra y el modo de envío.
- **Creación de visualizaciones:** Se generaron gráficos de barras y diagramas de frecuencia para explorar la relación entre las variables categóricas y la condición del producto.

Al final del EDA, se obtuvo un dataset limpio y listo para ser utilizado en la fase de modelado.

## Preparación de los Datos para el Modelado

Antes de entrenar los modelos, se realizaron algunos pasos de preparación:

- **Conversión de variables booleanas:** Las variables categóricas con valores booleanos fueron convertidas a enteros (1/0) para que los modelos pudieran procesarlas correctamente.
- **Estandarización de variables numéricas:** Se estandarizaron las variables numéricas para garantizar que todas estuvieran en la misma escala, lo que es importante para algunos clasificadores.
- **División del dataset:** El dataset fue dividido en un conjunto de entrenamiento (70%) y un conjunto de prueba (30%) para evaluar el rendimiento de los modelos.

## Entrenamiento y Evaluación de Modelos

Se entrenaron y evaluaron diferentes modelos de clasificación utilizando un pipeline. Los modelos considerados fueron:

- Regresión Logística
- Random Forest
- Árbol de Decisión
- k-Nearest Neighbors (kNN)
- Gradient Boosting
- Naive Bayes
- XGBoost

Cada modelo fue evaluado usando las métricas de precisión, recall y F1-score, y se seleccionó el modelo con mejor desempeño. La precisión fue la métrica principal utilizada para la comparación.

## Resultados

El modelo que presentó el mejor rendimiento fue **XGBoost**, con una precisión de aproximadamente 80%. Se guardó este modelo para uso futuro.

Además, se utilizó una **matriz de confusión** para analizar el rendimiento del mejor modelo, proporcionando una visión clara sobre las predicciones correctas e incorrectas en ambas clases (nuevos y usados).