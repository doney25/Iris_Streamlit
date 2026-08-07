import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

st.title('Streamlit Basics Practice')
test="hello world"
st.write("lets learn Streamlit step by step")
st.badge("Success",color='red',icon=':material/check:')
st.write(test)

df = pd.DataFrame(
    rng(0).standard_normal((10, 20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df.style.highlight_max(axis=0))

st.json(
    
    {
        "foo": "bar",
        "baz": "boz",
        "stuff": [
            {"thing": "this"},
            {"thing": "that"},
            {"thing": [1, 2, 3]},
        ],
    }
)

from vega_datasets import data

source = data.barley()

st.bar_chart(source, x="year", y="yield", color="site", stack=False)

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.line_chart(df)