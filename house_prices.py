import streamlit as st
import pandas as pd
import numpy as np
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from machine_learning_model import regression
from streamlit_screen import *
import time

if __name__ == "__main__":

    intro()

    MLModel = regression()
    reg = MLModel['model']
    df = MLModel['df']

    coefficients = reg.coef_
    columns = df.columns[1:-1]

    lin_reg = pd.DataFrame(zip(columns, coefficients))
    lin_reg
    totalRms = columns.get_loc('TotRmsAbvGrd')
    totalRmsCoeff = coefficients[totalRms]

    if 'Price' not in st.session_state:
        st.session_state['Price'] = 1000000

    if 'PriceChange' not in st.session_state:
        st.session_state['PriceChange'] = 0

    radio_for_bedrooms(totalRmsCoeff)

    with st.sidebar:
        title = st.title(
            "Predicted Price of the house"
        )
        metric = st.metric(
            label="Price", value=st.session_state['Price'], delta=st.session_state['PriceChange'])
