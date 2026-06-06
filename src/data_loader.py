# Funciones para cargar datos procesados del proyecto

import pandas as pd


def load_model_data(path: str = "data/processed/model_data.parquet") -> pd.DataFrame:
    """
    Carga el dataset procesado utilizado para modelado.
    """
    return pd.read_parquet(path)