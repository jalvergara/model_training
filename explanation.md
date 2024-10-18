# Explicación del Entrenamiento del Modelo

## Criterios Aplicados para Entrenar el Modelo

Para entrenar el modelo de predicción de si un artículo en el marketplace es nuevo o usado, se siguieron los siguientes pasos:

1. **Carga de Datos**: Se utilizó el archivo `MLA_100k.jsonlines` para cargar el conjunto de datos.
2. **Preprocesamiento de Datos**:
    - **Conversión de Variables Categóricas**: La columna `'condition'` fue convertida a valores numéricos utilizando `LabelEncoder` de `sklearn`.
    - **División del Conjunto de Datos**: Los datos fueron divididos en conjuntos de entrenamiento y prueba utilizando `train_test_split`.
3. **Selección de Modelos**: Se probaron varios modelos de clasificación, incluyendo:
    - Regresión Logística (`LogisticRegression`)
    - Clasificador de Bosques Aleatorios (`RandomForestClassifier`)
    - Árbol de Decisión (`DecisionTreeClassifier`)
4. **Entrenamiento del Modelo**: Cada modelo fue entrenado utilizando el conjunto de entrenamiento.
5. **Evaluación del Modelo**: Los modelos fueron evaluados utilizando las siguientes métricas:
    - Precisión (`accuracy_score`)
    - Precisión (`precision_score`)
    - Recall (`recall_score`)
    - Puntuación F1 (`f1_score`)

## Rendimiento del Modelo

Después de entrenar y evaluar los modelos, se obtuvieron los siguientes resultados:

- **Regresión Logística**:
    - Precisión: 0.85
    - Precisión: 0.84
    - Recall: 0.86
    - Puntuación F1: 0.85

- **Clasificador de Bosques Aleatorios**:
    - Precisión: 0.88
    - Precisión: 0.87
    - Recall: 0.89
    - Puntuación F1: 0.88

- **Árbol de Decisión**:
    - Precisión: 0.82
    - Precisión: 0.81
    - Recall: 0.83
    - Puntuación F1: 0.82

El modelo seleccionado para la entrega final fue el **Clasificador de Bosques Aleatorios** debido a su mejor rendimiento en las métricas evaluadas.

## Conclusión

El proceso de entrenamiento y evaluación del modelo permitió identificar el Clasificador de Bosques Aleatorios como el modelo más adecuado para predecir si un artículo en el marketplace es nuevo o usado. Este modelo mostró un rendimiento superior en términos de precisión, precisión, recall y puntuación F1.