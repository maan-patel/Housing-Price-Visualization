import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
from machine_learning_model import *
from streamlit_screen import *
import locale
import charts as c
locale.setlocale(locale.LC_ALL, '')

if __name__ == "__main__":

    intro()

    MLModel = regression()
    reg = MLModel['model']
    df = MLModel['df']
    data = MLModel['data']
    df_summary_numerical = summarize_df(data)[0]

    intercept = reg.intercept_
    coefficients = reg.coef_
    columns = df.columns[1:-1]
    lin_reg = pd.DataFrame(zip(columns, coefficients))

    get_all_input(df_summary_numerical,columns,coefficients,intercept)

    display_charts(df_summary_numerical, columns, coefficients)

    with st.sidebar:
        title = st.title(
            "Predicted Price of the house"
        )
        metric = st.metric(
            label="Dollars (in USD)", value="{:,.2f}".format(st.session_state["Price"]), 
            delta="{:,.2f}".format(st.session_state["PriceChange"]))

