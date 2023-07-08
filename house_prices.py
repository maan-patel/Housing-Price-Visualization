import streamlit as st
import pandas as pd
import numpy as np
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression

st.title('Insight on Factors that affect Housing Prices')

raw_data_train = pd.read_csv('https://raw.githubusercontent.com/jmpark0808/pl_mnist_example/main/train_hp_msci436.csv')
df = raw_data_train.select_dtypes(include = ['float64', 'int64']).fillna(0) 
X = df.values[:, 1:-1]
y = df.values[:, -1]
reg = LinearRegression().fit(X, y)
coefficients = reg.coef_

columns = df.columns[1:-1]

coefficients
columns




