import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
from machine_learning_model import *
from streamlit_screen import *
import locale
locale.setlocale(locale.LC_ALL, '')

if __name__ == "__main__":

    intro()

    MLModel = regression()
    reg = MLModel['model']
    df = MLModel['df']
    data = MLModel['data']
    df_summary_numerical = summarize_df(data)[0]

    coefficients = reg.coef_
    columns = df.columns[1:-1]

    lin_reg = pd.DataFrame(zip(columns, coefficients))
    lin_reg
    totalRms = columns.get_loc('TotRmsAbvGrd')
    totalRmsCoeff = coefficients[totalRms]

    if 'Price' not in st.session_state:
        st.session_state['Price'] = df_summary_numerical['SalePrice']['mean']

    if 'PriceChange' not in st.session_state:
        st.session_state['PriceChange'] = 0

    radio_for_bedrooms(totalRmsCoeff)

    with st.sidebar:
        title = st.title(
            "Predicted Price of the house"
        )
        metric = st.metric(
            label="Dollars (in USD)", value=locale.currency(st.session_state["Price"], grouping=True), 
            delta=locale.currency(st.session_state["PriceChange"], grouping=True))
