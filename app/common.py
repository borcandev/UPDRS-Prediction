from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeRegressor

APP_DIR = Path(__file__).parent
DATA_PATH = APP_DIR.parent / "data" / "parkinsons.data"
TARGET = "total_UPDRS"
RANDOM_STATE = 42
TOP_N = 6

PARAM_GRID = {
    "max_depth": [4, 8, 12, 16, None],
    "min_samples_leaf": [1, 2, 5, 50],
    "ccp_alpha": [0.0, 0.01],
}


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


def get_feature_names(df):
    return [
        c for c in df.columns if c not in ["subject#", "motor_UPDRS", "total_UPDRS"]
    ]


def top_features(df, n=TOP_N):
    feature_cols = get_feature_names(df)
    corr = df[feature_cols + [TARGET]].corr()[TARGET].drop(TARGET).abs()
    return list(corr.sort_values(ascending=False).head(n).index)


@st.cache_data
def train_model(df):
    features = get_feature_names(df)
    X = df[features]
    y = df[TARGET]
    train_idx, _ = train_test_split(
        np.arange(len(df)), test_size=0.2, random_state=RANDOM_STATE
    )
    grid_search = GridSearchCV(
        DecisionTreeRegressor(random_state=RANDOM_STATE),
        PARAM_GRID,
        cv=5,
        scoring="r2",
        n_jobs=-1,
    )
    grid_search.fit(X.iloc[train_idx], y.iloc[train_idx])
    return grid_search.best_estimator_, features, grid_search.best_params_
