# Prueba de los módulos del proyecto

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.data_loader import load_model_data
from src.recommender import (
    build_popular_products,
    recommend_popular_products
)

model_data = load_model_data()

print(model_data.shape)

popular_products = build_popular_products(model_data)

print(
    recommend_popular_products(
        popular_products,
        n=10
    )
)