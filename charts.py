import streamlit as st
import pandas as pd
import numpy as np

def garage_chart(df, columns, coefficients):
    coeff = coefficients[columns.get_loc('GarageCars')]

    values = [coeff * x for x in range(int(df['GarageCars']['min'])+1, int(df['GarageCars']['max']+1))]

    chart_data = pd.DataFrame(
        {"Value Added by Number of Cars Garage Holds": 
            [x for x in range(
            int(df['GarageCars']['min']),
            int(df['GarageCars']['max']))],
        "Change in Price (USD)": values
        },
    )

    st.bar_chart(chart_data, x = "Value Added by Number of Cars Garage Holds")

def fireplace_chart(df, columns, coefficients):
    coeff = coefficients[columns.get_loc('Fireplaces')]
    values = [coeff * x for x in range(int(df['Fireplaces']['min'])+1, int(df['Fireplaces']['max']+1))]

    chart_data = pd.DataFrame(
        {"Value Added by Fireplaces": 
            [x for x in range(
            int(df['Fireplaces']['min']),
            int(df['Fireplaces']['max']))],
        "Change in Price (USD)": values
        },
    )

    st.bar_chart(chart_data, x="Value Added by Fireplaces")