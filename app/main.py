# API principal del proyecto

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from fastapi import FastAPI

from src.data_loader import load_model_data

from src.model_loader import (
    load_user_product_matrix,
    load_user_similarity_matrix
)

from src.recommender import (
    build_popular_products,
    recommend_popular_products,
    recommend_user_based
)

# --------------------------------------------------
# Inicialización API
# --------------------------------------------------

app = FastAPI(
    title="PF Ecommerce Recommender",
    version="1.0"
)

# --------------------------------------------------
# Carga de datos
# --------------------------------------------------

model_data = load_model_data()

popular_products = build_popular_products(
    model_data
)

# --------------------------------------------------
# Carga de artefactos del modelo colaborativo
# --------------------------------------------------

user_product_matrix = load_user_product_matrix()

user_similarity_df = load_user_similarity_matrix()

product_catalog = model_data[
    ["product_id", "product_name"]
].drop_duplicates()

# --------------------------------------------------
# Endpoints
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "PF Ecommerce Recommender API"
    }


@app.get("/recommend/popular")
def recommend_popular():

    recommendations = recommend_popular_products(
        popular_products,
        n=10
    )

    return recommendations.to_dict(
        orient="records"
    )


@app.get("/recommend/user/{user_id}")
def recommend_user(user_id: int):

    try:

        recommendations = recommend_user_based(
            user_id=user_id,
            user_product_matrix=user_product_matrix,
            user_similarity_df=user_similarity_df,
            product_catalog=product_catalog,
            n_recommendations=10,
            n_similar_users=10
        )

        return {
            "user_id": user_id,
            "recommendations": recommendations.to_dict(
                orient="records"
            )
        }

    except ValueError as error:

        return {
            "error": str(error)
        }