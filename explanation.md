# **📊 Explicación del Proceso de Entrenamiento del Modelo**

## **Contexto del Problema**

El objetivo de este proyecto es desarrollar un modelo de machine learning que permita predecir si un producto listado en un Marketplace es nuevo o usado. Para esto, se proporcionó un conjunto de datos llamado `MLA_100k.jsonlines`, que fue procesado y analizado en detalle para extraer las características relevantes. Este archivo resume las decisiones tomadas durante la construcción del modelo, las métricas evaluadas y los resultados finales obtenidos.

---

## **1. 🔍 Proceso de Análisis Exploratorio de Datos (EDA)**

### **Carga y Análisis de los Datos**
- Se cargaron los datos del archivo `MLA_100k.jsonlines` y se realizó una revisión inicial para identificar tipos de datos, columnas con valores nulos y la estructura general de la información.
- Se identificaron varias columnas que contenían datos en formato JSON, las cuales fueron desempacadas para obtener información adicional.
- Para algunas columnas que contenían arreglos, dado que era muy difícil de convertir en un formato estandar que se le pudiera entregar a un modelo, se optó por agregar la longitud de esas listas.  
- También se añadieron columnas calculadas, como el **tiempo de vida de la publicación** y la **última actualización**. Además, se agregaron columnas relacionadas al tamaño de las imágenes con base al contenido de la lista en la columna **pictures**.
- Se detectaron y eliminaron varias columnas con valores no informativos, como aquellas con un solo valor único o con más del 90% de valores nulos.
- Finalmente, se guardó el conjunto de datos procesado en `MLA_100k_cleaned.csv` ✅.

---

## **2. 🧠 Proceso de Entrenamiento del Modelo**

### **Selección de Variables**
Para entrenar el modelo, se eligieron las siguientes variables del conjunto de datos limpio:
- `base_price`
- `non_mercado_pago_payment_methods`
- `seller_id`
- `variations`
- `price`
- `attributes`
- `pictures`
- `initial_quantity`
- `sold_quantity`
- `available_quantity`
- `seller_address_longitude`
- `seller_address_id`
- `seller_address_latitude`
- `pixels`
- `max_pixels`
- `lifetime publication`
- `last_update`

La variable objetivo (**target**) es la columna `condition`, que indica si un producto es nuevo o usado. Esta se transformó en binaria, asignando **1** a los productos **nuevos** y **0** a los **usados**.

### **División de Datos**
Los datos se dividieron en un conjunto de entrenamiento y un conjunto de prueba utilizando un 70% de los datos para entrenar y un 30% para probar, con un estado aleatorio de 42 para asegurar la reproducibilidad.

---

## **3. ⚙️ Modelos Utilizados**

Se entrenaron y compararon cinco modelos diferentes:
- **🌲 Random Forest**
- **🌟 Gradient Boosting**
- **🔍 K-Nearest Neighbors**
- **🧮 Regresión Logística**
- **🚀 XGBoost**

Para cada modelo, se midieron las siguientes métricas:
- **Exactitud (Accuracy)**
- **AUC-ROC**
- **Precisión (Precision)**
- **Recall**
- **F1-Score** (para ambas clases: nueva y usada)

---

## **4. 📈 Evaluación de Modelos**

### **Comparación de Métricas**

- Se graficaron las métricas para una mejor comparación. En la primera gráfica, se compararon **Accuracy** y **AUC-ROC**. En la segunda gráfica, se compararon **Precisión, Recall y F1-Score** para las clases positiva (nuevo) y negativa (usado). Puedes indagar en los resultados visitando el notebook [002_model_training.ipynb](./notebooks/002_model_training.ipynb).

### **Mejor Modelo**
- **🚀 XGBoost** fue el modelo que obtuvo el mejor desempeño global, con la mayor **exactitud (0.8824)** y un **AUC-ROC de 0.9508**.
- También destacó en la predicción de la clase positiva (nuevos), obteniendo un **F1-Score de 0.7366** y un **Recall** alto, lo cual es crucial en problemas donde es más importante identificar correctamente los productos nuevos.
- Aunque **🌲 Random Forest** tuvo un rendimiento competitivo, **XGBoost** lo superó en la mayoría de las métricas.

---

## **5. 💾 Guardado del Modelo**

Finalmente, el mejor modelo, **XGBoost**, se guardó como un archivo **.pkl** para su posterior uso en producción. La ruta del archivo es:  
`artifacts/models/model.pkl`.

---

## **6. 🏆 Conclusiones Finales**

- **🚀 XGBoost** fue seleccionado como el mejor modelo, gracias a su balance entre exactitud, capacidad de discriminación de clases (AUC-ROC) y rendimiento en la predicción de la clase positiva.
- Este modelo está listo para ser usado en un entorno de producción y se espera que generalice bien en datos no vistos debido a su rendimiento en la validación cruzada.
  
---
