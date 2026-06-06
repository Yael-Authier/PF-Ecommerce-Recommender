# Carga de artefactos del modelo

import pandas as pd


def load_user_product_matrix(
    path="models/user_product_matrix.parquet"
):
    return pd.read_parquet(path)


def load_user_similarity_matrix(
    path="models/user_similarity_df.parquet"
):
    return pd.read_parquet(path)