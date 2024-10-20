# Explicación del Proceso de Entrenamiento del Modelo

## Contexto del Problema

En el contexto de un Marketplace en línea, es crucial poder predecir si un producto listado es **nuevo** o **usado** para mejorar la experiencia del usuario y optimizar las recomendaciones. Este proyecto se enfoca en el desarrollo de un modelo de machine learning que permita realizar dicha predicción utilizando el dataset `MLA_100k.jsonlines`.

---

## 1. Análisis Exploratorio de Datos (EDA)

### Carga y Limpieza de Datos

En el análisis exploratorio de datos (EDA), se realizaron las siguientes tareas clave:

- **Carga de datos**: El archivo `MLA_100k.jsonlines` fue cargado y transformado a un formato adecuado para el análisis.
- **Desempaquetado de columnas JSON**: Varias columnas que contenían listas o estructuras JSON.
- **Eliminación de columnas irrelevantes**: Se eliminaron columnas con más del 80% de valores nulos o con poca variabilidad, como `site_id`, `seller_id`, `id`, `currency_id`, entre otras.
- **Creación de nuevas características**: Se generaron nuevas columnas a partir de las ya existentes.

El conjunto de datos final fue guardado como `MLA_100k_cleaned.csv` para ser utilizado en el entrenamiento de los modelos.

### Análisis de Correlación

Un análisis de correlación mostró que algunas variables, como **`accepts_mercadopago`** y **`buying_mode`**, tenían una correlación negativa alta (-0.86), lo que sugiere que es posible que contengan información redundante. Por otro lado, la mayoría de las demás variables mostraron correlaciones moderadas o bajas, lo que las hace candidatas útiles para el modelo, al no estar altamente correlacionadas entre sí.

---

## 2. Proceso de Entrenamiento del Modelo

### Selección de Características

Para entrenar el modelo, se seleccionaron varias características clave del conjunto de datos limpio, tales como:

- `base_price`
- `price`
- `non_mercado_pago_payment_methods`
- `initial_quantity`
- `sold_quantity`
- `available_quantity`
- `seller_address_latitude`
- `seller_address_longitude`

La **variable objetivo** fue la columna **condition**, que fue transformada en una variable binaria, donde **1** representa productos **nuevos** y **0** representa productos **usados**.

### División de los Datos

El conjunto de datos fue dividido en un **80% para entrenamiento** y un **20% para prueba**, utilizando una semilla aleatoria (`random_state=42`) para asegurar la reproducibilidad. Esta partición nos permite evaluar el rendimiento del modelo en datos no utilizados durante el entrenamiento.

---

## 3. Modelos de Machine Learning Utilizados

En el notebook de modelado (**002_model_training.ipynb**), se entrenaron cinco modelos de clasificación para predecir si un producto es nuevo o usado:

1. **Regresión Logística** (`LogisticRegression`)
2. **MLP (Perceptrón Multicapa)** (`MLPClassifier`)
3. **Árbol de Decisión** (`DecisionTreeClassifier`)
4. **Random Forest** (`RandomForestClassifier`)
5. **XGBoost** (`XGBClassifier`)

### Evaluación y Métrica

Para evaluar el rendimiento de cada modelo, se utilizó la métrica de **exactitud (accuracy)**, que mide el porcentaje de predicciones correctas realizadas por el modelo sobre el conjunto de prueba.

---

## 4. Evaluación de Modelos y Resultados

Los resultados obtenidos tras evaluar los modelos en el conjunto de prueba fueron los siguientes:

- **Logistic Regression**: 71.50%
- **MLP**: 71.74%
- **Decision Tree**: 81.60%
- **Random Forest**: 82.27%
- **XGBoost**: 83.09%

### Mejor Modelo: XGBoost

El modelo **XGBoost** fue el que obtuvo el mejor rendimiento general, con una **precisión del 83.09%**, lo que indica que es el modelo más adecuado para este problema. XGBoost también mostró un buen balance entre precisión y capacidad de generalización.

---

## 5. Conclusiones Finales

El modelo **XGBoost** fue seleccionado como el modelo final debido a su mejor rendimiento en términos de exactitud. Este modelo puede ser implementado en un entorno de producción para predecir si un producto es nuevo o usado con alta precisión.

El modelo final fue guardado en un archivo **.pkl** para su uso posterior en el despliegue.

---

## 6. Archivos Adjuntos

- **001_EDA.ipynb**: Contiene el análisis exploratorio de datos y el preprocesamiento.
- **002_model_training.ipynb**: Incluye el entrenamiento, evaluación y selección del modelo.
- **model.pkl**: Archivo con el modelo final entrenado listo para ser implementado.

---

## Bash Script para consumir el archivo .pkl

A continuación se muestra un script en bash que permite cargar el archivo **.pkl** y realizar predicciones con el modelo entrenado utilizando Python y `pickle`:

```bash

# Script para cargar un modelo .pkl y realizar predicciones
# Asegúrate de tener instalado Python y las librerías necesarias (scikit-learn, pickle, numpy)

# Ruta del modelo
MODEL_PATH="model.pkl"

# Datos de prueba para realizar predicción (ejemplo)
TEST_DATA="[[1500, 1, 3, 200, 50, 10, -34.6118, -58.4173, 10, 2]]"  # Reemplazar por tus datos

# Script Python para cargar el modelo y realizar predicciones
import pickle
import numpy as np

# Cargar el modelo
model_path = "$MODEL_PATH"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Datos de prueba (cambiar según sea necesario)
X_test = np.array($TEST_DATA)

# Realizar la predicción
prediction = model.predict(X_test)

# Imprimir el resultado
print("Predicción:", prediction)
