import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from common import TARGET, get_feature_names, load_data

st.title("Visualisierung")
st.write("Verteilungen und Korrelationen im Datensatz")
st.markdown("---")

df = load_data()
features = get_feature_names(df)
plot_features = [TARGET] + features

tab1, tab2 = st.tabs(["Verteilungen", "Korrelationen"])

with tab1:
    st.subheader("Verteilungsanalyse")

    feature = st.selectbox("Feature auswählen:", plot_features)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x=feature, kde=True, ax=ax)
    ax.set_title(f"Verteilung: {feature}")
    plt.tight_layout()
    st.pyplot(fig)

    col1, col2, col3 = st.columns(3)
    col1.metric("Mittelwert", f"{df[feature].mean():.4f}")
    col2.metric("Min", f"{df[feature].min():.4f}")
    col3.metric("Max", f"{df[feature].max():.4f}")

with tab2:
    st.subheader("Korrelationsmatrix")

    corr_cols = [c for c in df.columns if c != "subject#"]
    fig, ax = plt.subplots(figsize=(14, 11))
    sns.heatmap(
        df[corr_cols].corr(),
        annot=True,
        cmap="bwr",
        ax=ax,
    )
    ax.set_title("Korrelationsmatrix")
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Einzelkorrelation mit der Zielvariable")
    st.write(f"Top 10 Features nach |r| mit `{TARGET}`")

    raw_corr = df[features + [TARGET]].corr()[TARGET].drop(TARGET)
    target_corr = raw_corr.reindex(raw_corr.abs().sort_values(ascending=False).index)
    top10 = target_corr.head(10).sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top10.index, top10, color="green")
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.set_xlabel("Pearson-Korrelation (r)")
    ax.set_title(f"Top 10 Features nach |r| mit {TARGET}")
    plt.tight_layout()
    st.pyplot(fig)
