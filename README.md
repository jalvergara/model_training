# **📦 Proyecto: Predicción de Condición de Productos en un Marketplace**

## **Descripción del Proyecto**

En el contexto de un Marketplace, se requiere un algoritmo de machine learning para predecir si un producto listado es **nuevo** o **usado**. Este proyecto abarca desde el análisis exploratorio de datos (EDA), la preparación del conjunto de datos, el entrenamiento de modelos hasta la selección del mejor modelo basado en diversas métricas de rendimiento.

El dataset utilizado en este proyecto se llama **MLA_100k.jsonlines**, el cual contiene información relevante sobre los productos listados en la plataforma. A lo largo de este proceso, se utilizaron diferentes modelos de machine learning para resolver este problema, seleccionando el que mejor se adapta a la tarea.

Puedes encontrar el dataset [aquí](https://drive.google.com/file/d/1mzk9g5StOsIvi8TBIVX5CObAsrAOWhcL/view?usp=drive_link).

---

## **Estructura del Proyecto**

El repositorio está organizado de la siguiente manera:

### **1. `artifacts/models/`**
   - **`model.pkl`**: Archivo que contiene el modelo final entrenado (XGBoost) listo para ser desplegado o utilizado en producción.

### **2. `data/`**
   - **`processed/`**: Carpeta que contiene el conjunto de datos limpio y procesado (**MLA_100k_cleaned.csv**).
   - **`raw/`**: Carpeta que contiene el conjunto de datos original en formato **JSON lines** proporcionado (**MLA_100k.jsonlines**).

### **3. `notebooks/`**
   - **`001_EDA.ipynb`**: Este notebook contiene todo el proceso de análisis exploratorio de datos (EDA), limpieza y preprocesamiento de las variables relevantes.
   - **`002_model_training.ipynb`**: En este notebook se realizó el entrenamiento de los modelos, su evaluación y la selección del mejor modelo basado en las métricas de rendimiento.

### **4. `src/utils/`**
   - **`analysis_functions.py`**: Módulo que contiene funciones auxiliares utilizadas para el análisis de los datos y la creación de resúmenes de columnas, entre otras tareas.

### **5. `test/`**
   - **Este directorio está reservado para futuras implementaciones de pruebas unitarias y de integración.**

### **6. Archivos Clave del Proyecto:**
   - **`.gitignore`**: Especifica los archivos y carpetas que deben ser ignorados por Git.
   - **`README.md`**: El archivo que estás leyendo ahora, que explica la estructura y el propósito del proyecto.
   - **`explanation.md`**: Este archivo contiene una explicación detallada sobre los criterios utilizados para entrenar el modelo y las métricas alcanzadas. [Haz clic aquí para leerlo](./explanation.md).
   - **`pyproject.toml` y `poetry.lock`**: Archivos relacionados con la configuración de dependencias del proyecto utilizando **Poetry**.

---

## **Instrucciones para Ejecutar el Proyecto**

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-repositorio/model_training.git
   ```
2. **Instalar dependencias:**
   Si estás utilizando **Poetry**:
   ```bash
   poetry install
   ```

3. **Ejecutar los notebooks:**
   - Puedes navegar a la carpeta `notebooks/` y ejecutar los archivos **001_EDA.ipynb** y **002_model_training.ipynb** para reproducir el análisis exploratorio y el entrenamiento del modelo.

4. **Cargar el modelo entrenado:**
   Para utilizar el modelo entrenado, puedes cargar el archivo `model.pkl` en tu código Python de la siguiente manera:
   ```python
   import pickle

   # Cargar el modelo
   with open('artifacts/models/model.pkl', 'rb') as f:
       model = pickle.load(f)

   # Realizar predicciones
   predictions = model.predict(X_test)
   ```

---

## **Documentación Adicional**

Para más detalles sobre el proceso de entrenamiento del modelo y las decisiones tomadas, consulta el archivo [**explanation.md**](./explanation.md) 📄.

---

## **Contacto**

Si tienes preguntas o sugerencias sobre este proyecto, no dudes en contactarme.
