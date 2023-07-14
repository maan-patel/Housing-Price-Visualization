import streamlit as st
import pandas as pd
import numpy as np

def garage_chart(df, columns, coefficients):
    garage_coeff = coefficients[columns.get_loc('GarageCars')]

    values = [garage_coeff * x for x in range(int(df['GarageCars']['min']), int(df['GarageCars']['max']))]

    print(values)


    chart_data = pd.DataFrame(
    {"Number of Garage Spaces": 
        [x for x in range(
        int(df['GarageCars']['min']),
        int(df['GarageCars']['max']))],
    "Change in Price (USD)": values
    },
    )

    st.bar_chart(chart_data, 
    x = "Number of Garage Spaces")