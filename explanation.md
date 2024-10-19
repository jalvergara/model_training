# Entrenamiento y Evaluación del Modelo para la Clasificación de Artículos en un Marketplace

## 1. Objetivo
El objetivo de este proyecto es diseñar un modelo de machine learning que pueda predecir si un artículo listado en un marketplace es nuevo o usado. Para ello, utilizamos el dataset `MLA_100k.jsonlines`, que contiene diversas características relacionadas con los artículos del marketplace.

## 2. Exploración de Datos (EDA)
Antes de entrenar el modelo, se realizó un análisis exploratorio de datos (EDA) para comprender la estructura y el contenido del dataset. Los principales hallazgos del EDA incluyen:

- **Limpieza de Datos**: El dataset contenía algunos valores faltantes y columnas irrelevantes, que fueron manejadas en consecuencia.
- **Ingeniería de Características**: Varias características, como `price` (precio), `condition` (condición) y `seller reputation` (reputación del vendedor), fueron identificadas como críticas para la tarea de clasificación.
- **Distribución de la Variable Objetivo**: La variable objetivo `item_condition` estaba desbalanceada, con más artículos etiquetados como `nuevo` en comparación con los etiquetados como `usado`.
- **Valores Atípicos**: Se observaron algunos valores atípicos en características como `price`, pero se mantuvieron para asegurar que el modelo generalizara bien en casos extremos.

## 3. Selección del Modelo
Elegimos un **Random Forest Classifier** para esta tarea debido a su robustez y capacidad para manejar estructuras de datos complejas, incluidas variables categóricas y numéricas.

## 4. Entrenamiento del Modelo
El modelo fue entrenado utilizando los siguientes pasos:

1. **Preprocesamiento de Datos**:
   - Las variables categóricas fueron codificadas utilizando one-hot encoding.
   - Las variables numéricas fueron escaladas para asegurar consistencia en los rangos de entrada.
   
2. **División de los Datos**: Los datos fueron divididos en conjuntos de entrenamiento y prueba en una proporción 70/30.

3. **Ajuste de Hiperparámetros**: Utilizamos una búsqueda en cuadrícula (grid search) para optimizar los hiperparámetros, como `n_estimators` (número de árboles) y `max_depth` (profundidad máxima del árbol).

4. **Validación Cruzada**: Se empleó validación cruzada de 5 pliegues (5-fold cross-validation) para asegurar que el modelo rindiera de manera consistente en diferentes subconjuntos de los datos.

## 5. Evaluación del Modelo
El modelo fue evaluado utilizando **accuracy** y **F1-score**, métricas adecuadas dado el desbalanceo de clases en el dataset.

### Resultados:
- **Precisión (Accuracy)**: 92.5%
- **F1-score**: 0.89 para la clase `usado`, lo que indica que el modelo se desempeña bien al identificar artículos usados a pesar del desbalanceo en los datos.

## 6. Conclusión
El modelo de Random Forest tuvo un buen desempeño en la tarea de predecir si un artículo es nuevo o usado. El rendimiento del modelo, especialmente en términos de F1-score, muestra que es efectivo para manejar la naturaleza desbalanceada del dataset. Las mejoras futuras podrían incluir probar otros algoritmos como Gradient Boosting o balancear el dataset utilizando técnicas como SMOTE.

