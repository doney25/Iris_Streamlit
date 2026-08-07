from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import streamlit as st

import numpy as np

iris=load_iris()
X=iris.data
y=iris.target
model=RandomForestClassifier()
model.fit(X,y)

st.title("Simple Iris species prediction app")

sepal_length=st.number_input("Sepal length", min_value=0.0, max_value=10.0, value=5.0)
sepal_width=st.number_input("Sepal width", min_value=0.0, max_value=10.0, value=3.0)
petal_length=st.number_input("Petal length", min_value=0.0, max_value=10.0, value=1.0)
petal_width=st.number_input("Petal width", min_value=0.0, max_value=10.0, value=0.2)
predict=st.button("Predict Species")

if predict:
    input_data=np.array([[sepal_length,sepal_width,petal_length,petal_width]])
    prediction=model.predict(input_data)[0]
    species=iris.target_names[prediction]
    st.success(f"The predicted species is: {species}")
    
st.markdown("----")
st.write("Adjust input values and click 'predict' to see the predicted species of the Iris flower based on the provided measurements.")