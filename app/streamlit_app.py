import streamlit as st

from common import TARGET, load_data

st.set_page_config(
    page_title="Parkinson UPDRS",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

df = load_data()
feature_count = len(df.columns) - 3

st.title("Parkinson UPDRS Telemonitoring 🎙️")
st.write("Regression des Schweregrads aus Sprachbiomarkern")
st.markdown("---")

st.write(
    "Diese App nutzt den Oxford Parkinson Telemonitoring Datensatz, "
    "um den **total_UPDRS**-Score aus Stimm-Messwerten zu schätzen."
)

st.markdown(
    """
**In der App:**
- **Datenexploration** – Datensatz und Statistiken
- **Visualisierung** – Verteilungen und Korrelationen
- **Vorhersage** – total_UPDRS mit dem trainierten Modell schätzen
- **Feature Info** – Erklärung der Spalten im Datensatz
"""
)

st.markdown("---")
st.markdown("### 📊 Datensatz")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Aufnahmen", len(df))
col2.metric("Patient:innen", df["subject#"].nunique())
col3.metric("Features", feature_count)
col4.metric("Ø total_UPDRS", f"{df[TARGET].mean():.1f}")

with st.expander("Vorschau"):
    st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")
st.caption("Oxford Telemonitoring Dataset · UCI")
