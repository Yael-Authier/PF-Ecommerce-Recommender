# User Manual

## PF Ecommerce Recommender

### Autor

Yael Authier

---

# 1. Introducción

PF Ecommerce Recommender es una aplicación desarrollada para generar recomendaciones de productos utilizando técnicas de Machine Learning y Collaborative Filtering.

La solución permite obtener:

* Productos más populares del catálogo.
* Recomendaciones personalizadas para usuarios específicos.

---

# 2. Requisitos

Antes de ejecutar el proyecto se debe contar con:

* Python 3.10 o superior.
* Git.
* Dependencias instaladas mediante requirements.txt.

---

# 3. Instalación

Clonar repositorio:

```bash
git clone https://github.com/Yael-Authier/PF-Ecommerce-Recommender.git
```

Ingresar al proyecto:

```bash
cd PF-Ecommerce-Recommender
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# 4. Estructura del proyecto

```text
PF-Ecommerce-Recommender
│
├── app
├── data
├── docs
├── models
├── notebooks
├── src
├── README.md
└── requirements.txt
```

---

# 5. Ejecución de la API

Desde la raíz del proyecto ejecutar:

```bash
uvicorn app.main:app --reload
```

La API quedará disponible en:

```text
http://127.0.0.1:8000
```

---

# 6. Documentación interactiva

FastAPI genera automáticamente una interfaz Swagger.

Acceder mediante:

```text
http://127.0.0.1:8000/docs
```

Desde allí es posible probar todos los endpoints disponibles.

---

# 7. Endpoints disponibles

## Home

Endpoint:

```text
GET /
```

Respuesta:

```json
{
    "message": "PF Ecommerce Recommender API"
}
```

---

## Productos populares

Endpoint:

```text
GET /recommend/popular
```

Descripción:

Devuelve los productos más populares del catálogo según cantidad de compras históricas.

---

## Recomendaciones personalizadas

Endpoint:

```text
GET /recommend/user/{user_id}
```

Ejemplo:

```text
GET /recommend/user/21
```

Descripción:

Genera recomendaciones utilizando Collaborative Filtering basado en similitud entre usuarios.

Ejemplo de respuesta:

```json
{
    "user_id": 21,
    "recommendations": [
        {
            "product_id": 36865,
            "product_name": "Non Fat Raspberry Yogurt",
            "score": 6
        }
    ]
}
```

---

# 8. Artefactos del modelo

La aplicación utiliza artefactos previamente generados durante la etapa de modelado:

* user_product_matrix.parquet
* user_similarity_df.parquet

Estos archivos permiten acelerar la generación de recomendaciones evitando recalcular matrices durante la ejecución de la API.

---

# 9. Solución de problemas

### Error: ModuleNotFoundError

Verificar que el proyecto se ejecute desde la raíz del repositorio.

### Error: Archivo parquet no encontrado

Verificar que existan los archivos:

```text
models/user_product_matrix.parquet
models/user_similarity_df.parquet
```

### Error: Usuario inexistente

Verificar que el user_id consultado exista dentro de la matriz usuario-producto utilizada por el sistema.

---

# 10. Próximas mejoras

* Dashboard interactivo con Streamlit.
* Despliegue en la nube.
* Sistema de recomendación Item-Based.
* Adaptación a datos reales de El Club de la Milanesa.
