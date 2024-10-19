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

5. **Resultados del Modelo: Random Forest**

El modelo de **Random Forest** fue evaluado utilizando diversas métricas de rendimiento, con los siguientes resultados:

- **Accuracy**: 0.8385
- **Precision**: 0.7933
- **Recall**: 0.8788
- **F1-Score**: 0.8339
- **ROC-AUC**: 0.9149

### Interpretación:
- El modelo tiene una **precisión** general del 83.85%, lo que significa que en promedio, clasifica correctamente el 83.85% de los casos.
- La **precisión** de 0.7933 indica que, de los artículos que el modelo predice como usados, el 79.33% son correctos.
- El **recall** de 0.8788 muestra que el modelo identifica correctamente el 87.88% de los artículos usados.
- El **F1-score** de 0.8339 indica un buen equilibrio entre precisión y recall.
- El **ROC-AUC** de 0.9149 sugiere que el modelo tiene una alta capacidad para distinguir entre clases (nuevo vs usado).

Estos resultados indican que el modelo es efectivo, aunque puede haber margen para mejorar la precisión sin sacrificar demasiado el recall.

## 6. Conclusión
El modelo de Random Forest tuvo un buen desempeño en la tarea de predecir si un artículo es nuevo o usado. El rendimiento del modelo, especialmente en términos de ROC-AUC, muestra que es efectivo para manejar la naturaleza desbalanceada del dataset. Las mejoras futuras podrían incluir probar otros algoritmos como Gradient Boosting o balancear el dataset utilizando técnicas como SMOTE.

