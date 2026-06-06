# API principal del proyecto

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from fastapi import FastAPI

from src.data_loader import load_model_data
from src.recommender import (
    build_popular_products,
    recommend_popular_products
)

app = FastAPI(
    title="PF Ecommerce Recommender",
    version="1.0"
)

# Cargar datos al iniciar

model_data = load_model_data()

popular_products = build_popular_products(
    model_data
)


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