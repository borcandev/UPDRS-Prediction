import streamlit as st

st.title("Feature Info")
st.write("Oxford Parkinson's Disease Telemonitoring Dataset · 5.875 Patienten")
st.markdown("---")

st.markdown(
    """
| Feature | Erklärung |
|---------|-----------|
| `subject#` | ID des Patienten |
| `age` | Alter des Patienten (36–85 Jahre in diesem Datensatz) |
| `sex` | 0 = männlich, 1 = weiblich |
| `test_time` | Zeit in Tagen seit Beginn der Studie |
| `motor_UPDRS` | Nur motorische Symptome: Zittern, Steifheit, Gleichgewicht |
| `total_UPDRS` | Alles zusammen – höher = schlimmer |
| `Jitter(%)` | Frequenzschwankung in % |
| `Jitter(Abs)` | Frequenzschwankung in Sekunden |
| `Jitter:RAP` | Durchschnitt über jeweils 3 aufeinanderfolgende Schwingungen |
| `Jitter:PPQ5` | Durchschnitt über jeweils 5 aufeinanderfolgende Schwingungen |
| `Jitter:DDP` | RAP × 3 (abgeleiteter Wert) |
| `Shimmer` | Relevante Amplitudenschwankung |
| `Shimmer(dB)` | Dasselbe in Dezibel |
| `Shimmer:APQ3` | Amplitude Perturbation Quotient über 3 Schwingungen |
| `Shimmer:APQ5` | Amplitude Perturbation Quotient über 5 Schwingungen |
| `Shimmer:APQ11` | Amplitude Perturbation Quotient über 11 Schwingungen |
| `Shimmer:DDA` | APQ3 × 3 |
| `NHR` | Wie viel Rauschen im Verhältnis zum reinen Ton – höher = mehr Rauschen = schlechtere Stimmqualität |
| `HNR` | Das Gegenteil von NHR |
| `RPDE` | Misst, wie regelmäßig sich Stimmperioden wiederholen – gesund = regelmäßig, ungesund = unregelmäßiger |
| `DFA` | Misst langfristige Korrelationen im Signal (Konstanz vs. Zufall) |
| `PPE` | Entropie der Tonhöhenschwankungen – höher = mehr Unvorhersehbarkeit |
"""
)

st.markdown(
    "**UPDRS** (Unified Parkinson's Disease Rating Scale) hat eine Skala von 0 bis 260. "
    "Sie setzt sich aus der Summe von 6 Diagnose-Bereichen zusammen: "
    "kognitives Verhalten, Selbsteinschätzung, motorische Untersuchung, "
    "Komplikationen der Therapie, Hoehn-und-Yahr-Einstufung und ADL-Skala. "
    "Es ist unklar, welche Diagnosen in diesem Datensatz verwendet wurden."
)
