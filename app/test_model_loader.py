import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.model_loader import (
    load_user_product_matrix,
    load_user_similarity_matrix
)

user_product_matrix = load_user_product_matrix()

print(
    "User Product Matrix:",
    user_product_matrix.shape
)

user_similarity_df = load_user_similarity_matrix()

print(
    "User Similarity:",
    user_similarity_df.shape
)