import streamlit as st
import pandas as pd
import numpy as np

def garage_chart(df, columns, coefficients):
    coeff = coefficients[columns.get_loc('GarageCars')]

    values = [coeff * x for x in range(int(df['GarageCars']['min'])+1, int(df['GarageCars']['max']+1))]

    chart_data = pd.DataFrame(
        {"Number of Car Spaces in Garage": 
            [x for x in range(
            int(df['GarageCars']['min'])+1,
            int(df['GarageCars']['max'])+1)],
        "Change in Price (USD)": values
        },
    )

    st.bar_chart(chart_data, x = "Number of Car Spaces in Garage")

def fireplace_chart(df, columns, coefficients):
    coeff = coefficients[columns.get_loc('Fireplaces')]
    values = [coeff * x for x in range(int(df['Fireplaces']['min'])+1, int(df['Fireplaces']['max']+1))]
    print(values)

    chart_data = pd.DataFrame(
        {"Number of Fireplaces": 
            [x for x in range(
            int(df['Fireplaces']['min'])+1,
            int(df['Fireplaces']['max'])+1)],
        "Change in Price (USD)": values
        },
    )

    st.bar_chart(chart_data, x="Number of Fireplaces")