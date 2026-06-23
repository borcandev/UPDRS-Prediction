import streamlit as st

from common import TARGET, get_feature_names, load_data

st.title("Datenexploration")
st.write("Datensatz inspizieren und Statistiken ansehen")
st.markdown("---")

df = load_data()
features = get_feature_names(df)

st.write(f"Daten geladen: **{len(df)}** Zeilen, **{len(df.columns)}** Spalten")

tab1, tab2 = st.tabs(["Übersicht", "Statistiken"])

with tab1:
    st.subheader("Übersicht")

    col1, col2 = st.columns(2)
    col1.write(f"**Shape:** {df.shape}")
    col2.write(f"**Zielvariable:** `{TARGET}`")

    rows = st.slider("Zeilen anzeigen", 5, 50, 10)
    st.dataframe(df.head(rows), use_container_width=True)

    st.markdown("#### Info")
    st.write(f"**Features für ML:** {len(features)}")
    st.write("**Spalten:**", ", ".join(df.columns))

with tab2:
    st.subheader("Beschreibende Statistiken")
    st.dataframe(df.describe().round(3), use_container_width=True)
