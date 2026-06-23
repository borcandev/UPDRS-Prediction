import pandas as pd
import streamlit as st

from common import load_data, top_features, train_model

st.title("Vorhersage")
st.write("Decision Tree Regressor – **total_UPDRS** aus den wichtigsten Features schätzen")
st.markdown("---")

with st.spinner("Modell trainieren..."):
    df = load_data()
    model, feature_names, _ = train_model(df)

st.subheader("Eingabe")
st.write("Die 6 stärksten Features lassen sich anpassen, der Rest nutzt Median-Werte.")

top = top_features(df)
defaults = {name: float(df[name].median()) for name in feature_names}
defaults["sex"] = int(df["sex"].mode()[0])
values = dict(defaults)


def feature_input(name):
    if name == "sex":
        return st.selectbox(
            "Geschlecht (0=männlich, 1=weiblich)",
            options=[0, 1],
            index=int(defaults[name]),
            key=f"feat_{name}",
        )
    col = df[name]
    return st.slider(
        name,
        min_value=float(col.min()),
        max_value=float(col.max()),
        value=float(defaults[name]),
        key=f"feat_{name}",
    )


cols = st.columns(2)
for i, name in enumerate(top):
    with cols[i % 2]:
        values[name] = feature_input(name)

if st.button("Vorhersage", type="primary"):
    x = pd.DataFrame([values], columns=feature_names)
    pred = model.predict(x)[0]
    st.metric("Geschätzter total_UPDRS", f"{pred:.1f}")
