import streamlit as st
import pandas as pd
import numpy as np

def garage_chart(df, columns, coefficients):
    coeff = coefficients[columns.get_loc('GarageCars')]

    values = [coeff * x for x in range(int(df['GarageCars']['min']), int(df['GarageCars']['max']))]

    chart_data = pd.DataFrame(
        {"Number of Garage Spaces": 
            [x for x in range(
            int(df['GarageCars']['min']),
            int(df['GarageCars']['max']))],
        "Change in Price (USD)": values
        },
    )

    st.bar_chart(chart_data, x = "Number of Garage Spaces")

def fireplace_chart(df, columns, coefficients):
    coeff = coefficients[columns.get_loc('Fireplaces')]
    values = [coeff * x for x in range(int(df['Fireplaces']['min']), int(df['Fireplaces']['max']))]

    chart_data = pd.DataFrame(
        {"Home Contains Fireplace": 
            [x for x in range(
            int(df['Fireplaces']['min']),
            int(df['Fireplaces']['max']))],
        "Change in Price (USD)": values
        },
    )

    st.bar_chart(chart_data, x="Home Contains Fireplace")