import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("st.write")

st.write("Hello *World* :sunglasses:")

st.write(1234*5671)

df = pd.DataFrame(
    np.random.randn(203,3),
    columns=["a","b","c"]
)

st.write(df)

c = alt.Chart(df).mark_circle().encode(
    x="a", y="b", size="c", color="c",
).properties(title="Chart")
st.write(c)



