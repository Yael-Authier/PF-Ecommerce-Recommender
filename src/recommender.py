# Funciones principales del sistema de recomendación

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def build_popular_products(model_data: pd.DataFrame) -> pd.DataFrame:
    """
    Construye ranking de productos más populares.
    """
    popular_products = (
        model_data
        .groupby(["product_id", "product_name"])
        .size()
        .reset_index(name="purchase_count")
        .sort_values(by="purchase_count", ascending=False)
    )

    return popular_products


def recommend_popular_products(popular_products: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Recomienda los N productos más populares.
    """
    return popular_products[["product_id", "product_name", "purchase_count"]].head(n)


def build_user_product_matrix(data: pd.DataFrame) -> pd.DataFrame:
    """
    Construye matriz usuario-producto binaria.
    """
    data = data.copy()
    data["interaction"] = 1

    matrix = data.pivot_table(
        index="user_id",
        columns="product_id",
        values="interaction",
        fill_value=0
    )

    return matrix


def build_user_similarity_matrix(user_product_matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula similitud coseno entre usuarios.
    """
    user_similarity = cosine_similarity(user_product_matrix)

    user_similarity_df = pd.DataFrame(
        user_similarity,
        index=user_product_matrix.index,
        columns=user_product_matrix.index
    )

    return user_similarity_df


def recommend_user_based(
    user_id: int,
    user_product_matrix: pd.DataFrame,
    user_similarity_df: pd.DataFrame,
    product_catalog: pd.DataFrame,
    n_recommendations: int = 10,
    n_similar_users: int = 10
) -> pd.DataFrame:
    """
    Recomienda productos a un usuario según usuarios similares.
    """
    if user_id not in user_product_matrix.index:
        raise ValueError("El usuario no existe en la matriz usuario-producto.")

    similar_users = (
        user_similarity_df[user_id]
        .sort_values(ascending=False)
        .iloc[1:n_similar_users + 1]
        .index
    )

    user_products = set(
        user_product_matrix.loc[user_id][
            user_product_matrix.loc[user_id] > 0
        ].index
    )

    similar_users_products = user_product_matrix.loc[similar_users]

    product_scores = (
        similar_users_products
        .sum(axis=0)
        .sort_values(ascending=False)
    )

    recommendations = product_scores[
        ~product_scores.index.isin(user_products)
    ].head(n_recommendations)

    recommendations = (
        recommendations
        .reset_index()
        .rename(columns={0: "score"})
        .merge(
            product_catalog[["product_id", "product_name"]].drop_duplicates(),
            on="product_id",
            how="left"
        )
    )

    return recommendations[["product_id", "product_name", "score"]]