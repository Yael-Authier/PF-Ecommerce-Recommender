# PF Ecommerce Recommender

Sistema de recomendación de productos para e-commerce desarrollado como Proyecto Final de Data Science.

El objetivo del proyecto es generar recomendaciones personalizadas a partir del historial de compras de los usuarios utilizando técnicas de Collaborative Filtering.

---

## Objetivo de negocio

Los comercios electrónicos suelen disponer de catálogos con miles de productos, dificultando que los usuarios descubran artículos relevantes.

Este proyecto busca mejorar la experiencia de compra mediante recomendaciones personalizadas basadas en patrones históricos de consumo.

Como caso de estudio se utilizó el dataset público **Instacart Market Basket Analysis**.

---

## Dataset

Instacart Market Basket Analysis

Características principales:

* 206.209 usuarios
* 49.688 productos
* 3.421.083 pedidos
* 32.434.489 interacciones

---

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Scikit-Learn
* FastAPI
* Uvicorn
* Jupyter Notebook
* Git
* GitHub

---

## Arquitectura del proyecto

```text
PF-Ecommerce-Recommender
│
├── app
│   ├── main.py
│   ├── test_recommender.py
│   └── test_model_loader.py
│
├── data
│   ├── raw
│   └── processed
│
├── docs
│   ├── 01_Project_Proposal.md
│   ├── 02_Technical_Report.md
│   └── 03_User_Manual.md
│
├── models
│
├── notebooks
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Data_Preprocessing.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Modeling.ipynb
│   └── 06_Model_Evaluation.ipynb
│
├── src
│
├── README.md
└── requirements.txt
```

---

## Metodología

### 1. Data Understanding

* Exploración de tablas.
* Comprensión del modelo de datos.
* Validación de claves primarias y relaciones.

### 2. EDA

* Análisis de usuarios.
* Distribución de productos.
* Long Tail.
* Recompra.
* Patrones temporales.

### 3. Data Preprocessing

* Tratamiento de valores faltantes.
* Validación de integridad.
* Consolidación de tablas.

### 4. Feature Engineering

* Variables de usuario.
* Variables de producto.
* Reducción de sparsity.

### 5. Modelado

Se implementaron dos enfoques:

#### Baseline

Recomendación basada en productos más populares.

#### Collaborative Filtering User-Based

Recomendación basada en similitud entre usuarios utilizando Cosine Similarity.

---

## Resultados

### Métrica utilizada

Hit Rate@10

### Comparación de modelos

| Modelo                             | Hit Rate@10 |
| ---------------------------------- | ----------- |
| Baseline                           | 4.6%        |
| Collaborative Filtering User-Based | 6.6%        |

### Mejora obtenida

El modelo colaborativo obtuvo una mejora aproximada del **43.5%** respecto al baseline.

---

## API REST

El proyecto incluye una API desarrollada con FastAPI.

### Ejecutar API

```bash
uvicorn app.main:app --reload
```

### Swagger

```text
http://127.0.0.1:8000/docs
```

### Endpoints

#### Home

```text
GET /
```

#### Productos populares

```text
GET /recommend/popular
```

#### Recomendaciones personalizadas

```text
GET /recommend/user/{user_id}
```

Ejemplo:

```text
GET /recommend/user/21
```

---

## Artefactos del modelo

Para optimizar los tiempos de respuesta de la API se almacenan:

* user_product_matrix.parquet
* user_similarity_df.parquet

Estos artefactos permiten desacoplar la etapa de entrenamiento de la etapa de inferencia.

---

## Aplicación futura

La arquitectura desarrollada puede adaptarse fácilmente a escenarios reales de retail.

Particularmente se proyecta su utilización para futuras iniciativas de recomendación de productos congelados de El Club de la Milanesa, combinando información transaccional y preferencias declaradas por los usuarios dentro del programa de fidelización.

---

## Autor

**Yael Authier**

Proyecto Final — Data Science
