# Technical Report

## 1. Introducción

El presente proyecto desarrolla un sistema de recomendación de productos para entornos de comercio electrónico utilizando técnicas de análisis de datos y Machine Learning.

El objetivo es recomendar productos relevantes a cada usuario a partir de su historial de compras, mejorando la experiencia de navegación y aumentando las probabilidades de conversión y recompra.

Para el desarrollo se utilizó el dataset público Instacart Market Basket Analysis.

---

## 2. Comprensión del negocio

### Problema

Los comercios electrónicos suelen disponer de catálogos con miles de productos.

Esta situación genera dificultades para que los usuarios descubran productos relevantes de manera eficiente.

Un sistema de recomendación permite personalizar la experiencia de compra utilizando información histórica de comportamiento.

### Objetivo

Desarrollar un recomendador capaz de sugerir productos relevantes para cada usuario en función de sus patrones de consumo.

---

## 3. Comprensión de los datos

Se analizaron las siguientes tablas:

| Tabla       | Descripción                          |
| ----------- | ------------------------------------ |
| orders      | Pedidos realizados por los usuarios  |
| products    | Catálogo de productos                |
| prior       | Productos comprados históricamente   |
| train       | Productos utilizados para evaluación |
| aisles      | Subcategorías de productos           |
| departments | Categorías principales               |

### Volumen de datos

* Usuarios: 206.209
* Productos: 49.688
* Pedidos: 3.421.083
* Interacciones: 32.434.489

---

## 4. Análisis exploratorio de datos (EDA)

Durante la exploración se identificaron los siguientes hallazgos:

### Comportamiento de usuarios

* Promedio de pedidos por usuario: 16,59
* Mediana de pedidos por usuario: 10
* Algunos usuarios alcanzan hasta 100 pedidos históricos.

### Distribución de productos

Se observó una fuerte distribución Long Tail.

La mayoría de los productos presentan pocas compras, mientras que un grupo reducido concentra gran parte de las interacciones.

### Patrones temporales

Se analizaron:

* Pedidos por día de la semana.
* Pedidos por hora del día.
* Tasas de recompra.

### Recompra

El 58,97% de las interacciones correspondieron a productos previamente comprados por el usuario.

Este resultado indica una fuerte recurrencia en los patrones de consumo.

---

## 5. Preprocesamiento de datos

Se realizaron las siguientes tareas:

* Verificación de valores faltantes.
* Identificación de registros duplicados.
* Validación de claves primarias.
* Validación de integridad referencial.
* Integración de tablas mediante joins.

Posteriormente se construyó una tabla consolidada para el modelado.

---

## 6. Feature Engineering

Se generaron variables descriptivas para usuarios y productos.

### Variables de usuario

* total_interactions
* unique_products
* reorder_rate

### Variables de producto

* total_purchases
* unique_users
* reorder_rate

### Reducción del problema

Para disminuir la sparsity se aplicaron filtros:

* Productos con al menos 20 interacciones.
* Usuarios con al menos 100 interacciones.

Esto permitió reducir el tamaño del espacio de recomendación manteniendo información relevante.

---

## 7. Modelado

### Modelo Baseline

Se implementó un recomendador basado en popularidad.

El modelo recomienda los productos más comprados históricamente.

Ventajas:

* Simplicidad.
* Bajo costo computacional.
* Fácil interpretación.

Limitaciones:

* Ausencia de personalización.

---

### Collaborative Filtering User-Based

Se implementó un sistema basado en similitud entre usuarios.

El procedimiento fue:

1. Construcción de matriz usuario-producto.
2. Cálculo de similitud mediante Cosine Similarity.
3. Identificación de usuarios similares.
4. Generación de recomendaciones personalizadas.

### Matriz usuario-producto

* Usuarios: 10.000
* Productos: 32.566
* Sparsity: 99,74%

La elevada sparsity es consistente con sistemas de recomendación reales.

---

## 8. Evaluación

### Métrica utilizada

Hit Rate@10

La métrica evalúa si el producto ocultado durante la validación aparece dentro de las 10 recomendaciones generadas por el modelo.

### Resultados

| Modelo                             | Hit Rate@10 |
| ---------------------------------- | ----------- |
| Baseline                           | 4,6%        |
| Collaborative Filtering User-Based | 6,6%        |

### Mejora obtenida

El modelo colaborativo obtuvo una mejora aproximada del 43,5% respecto al baseline.

---

## 9. Conclusiones

Los resultados muestran que el filtrado colaborativo basado en usuarios supera al modelo basado únicamente en popularidad.

La utilización de patrones de consumo compartidos permite generar recomendaciones más relevantes y personalizadas.

Por este motivo se selecciona Collaborative Filtering User-Based como modelo principal del sistema de recomendación.

---

## 10. Trabajo futuro

Las próximas etapas del proyecto incluyen:

* Desarrollo de API de recomendaciones.
* Dashboard interactivo.
* Despliegue de la solución.
* Adaptación del modelo a datos reales de El Club de la Milanesa para su futura unidad de negocio de productos congelados retail.
