# PF - E-commerce Product Recommender

## Autor

Yael Authier

## Carrera

Data Science - Soy Henry

## Descripción del proyecto

El presente proyecto tiene como objetivo desarrollar un sistema de recomendación de productos para entornos de comercio electrónico.

Utilizando información histórica de compras de clientes, el sistema busca generar recomendaciones personalizadas que permitan incrementar la conversión, mejorar la experiencia del usuario y favorecer la recompra.

Como caso de estudio se utiliza el dataset público Instacart Market Basket Analysis, compuesto por millones de interacciones entre usuarios y productos.

## Problema de negocio

Las plataformas de e-commerce suelen disponer de catálogos con miles de productos.

Ante esta situación, resulta complejo para los usuarios descubrir productos relevantes de forma eficiente.

Un sistema de recomendación permite personalizar la experiencia de compra mostrando productos potencialmente interesantes para cada usuario según su comportamiento histórico.

## Objetivos

### Objetivo general

Desarrollar un sistema de recomendación capaz de sugerir productos relevantes a usuarios de una plataforma de comercio electrónico.

### Objetivos específicos

* Analizar y comprender el comportamiento de compra de los usuarios.
* Construir un pipeline reproducible de procesamiento de datos.
* Implementar distintos enfoques de recomendación.
* Comparar modelos mediante métricas objetivas.
* Desplegar una solución funcional para generar recomendaciones.

## Dataset

Instacart Market Basket Analysis.

Características principales:

* Más de 3 millones de pedidos.
* Más de 200 mil usuarios.
* Más de 49 mil productos.
* Más de 32 millones de interacciones.

## Modelos implementados

* Baseline basado en popularidad.
* Collaborative Filtering User-Based.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Jupyter Notebook
- Git & GitHub

## Métrica principal

Hit Rate@10

## Resultados obtenidos

| Modelo                  | Hit Rate@10 |
| ----------------------- | ----------: |
| Baseline                |        4.6% |
| Collaborative Filtering |        6.6% |

El modelo de Collaborative Filtering obtuvo una mejora aproximada del 43.5% respecto del modelo baseline.

## Aplicación futura

La arquitectura desarrollada en este proyecto puede adaptarse a entornos reales de e-commerce.

Particularmente, se proyecta su utilización para un sistema de recomendación de productos congelados de El Club de la Milanesa, combinando información de compras históricas y preferencias declaradas por los usuarios dentro del programa de fidelización.

Esto permitiría personalizar ofertas, aumentar la conversión y mejorar la recompra en el canal retail.