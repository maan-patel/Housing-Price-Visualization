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
    st.header("How do different features affect the price of housing?")


    st.subheader("Value Added by Exterior Quality")
    hist_data_ext_qual = [46765.50376, -11790.75027, -19896.26241, -15078.49108]
    hist_label_ext_qual = ["Excellent", "Good", "Average", "Fair"]
    ext_qual = pd.DataFrame({"Exterior Quality": hist_label_ext_qual, "$ (USD)": hist_data_ext_qual})
    ax = ext_qual.plot.bar(x="Exterior Quality", y="$ (USD)")
    st.bar_chart(ext_qual, x="Exterior Quality", y="$ (USD)")

    st.subheader("Value Added by Central Air")
    hist_data_central_air = [-2388.683262, 2388.683262]
    hist_label_central_air = ["Available", "Not Available"]
    central_air = pd.DataFrame({"Central Air": hist_label_central_air, "$ (USD)": hist_data_central_air})
    ax = central_air.plot.bar(x="Central Air", y="$ (USD)")
    st.bar_chart(central_air, x="Central Air", y="$ (USD)")
    
    
    st.subheader("Value Added by Heating Quality")
    hist_data_heat = [5181.41053, 514.522098, -756.287888, 3223.430193, -8163.074934]
    hist_label_heat = ["Excellent", "Good", "Average", "Fair", "Poor"]
    heat = pd.DataFrame({"Heating Quality": hist_label_heat, "$ (USD)": hist_data_heat})
    ax = heat.plot.bar(x="Heating Quality", y="$ (USD)")
    st.bar_chart(heat, x="Heating Quality", y="$ (USD)")

    st.subheader("Value Added by Number of Fireplaces")
    hist_data_fire = [10603.88432, 21207.76864, 31811.65296]
    hist_label_fire = [1,2,3]
    fire = pd.DataFrame({"Number of Fireplaces": hist_label_fire, "$ (USD)": hist_data_fire})
    ax = fire.plot.bar(x="Number of Fireplaces", y="$ (USD)")
    st.bar_chart(fire, x="Number of Fireplaces", y="$ (USD)")

    st.subheader("Value Added by Number of Garage Size")
    hist_data_garage = [13710.65123, 27421.30247, 41131.9537, 54842.60493]
    hist_label_garage = [1,2,3,4]
    fire = pd.DataFrame({"Number of Garage Bays": hist_label_garage, "$ (USD)": hist_data_garage})
    ax = fire.plot.bar(x="Number of Garage Bays", y="$ (USD)")
    st.bar_chart(fire, x="Number of Garage Bays", y="$ (USD)")

    #  this displays the price 

    with st.sidebar:
        title = st.title(
            "Predicted Price of the house"
        )
        metric = st.metric(
            label="Dollars (in USD)", value="{:,.2f}".format(st.session_state["Price"]), 
            delta="{:,.2f}".format(st.session_state["PriceChange"]))


        st.subheader("Affect on Price by Feature")
        labels = st.session_state["PriceBreakdown"].keys()
        sizes = st.session_state["PriceBreakdown"].values()
        fire = pd.DataFrame({"Price Composition": labels, "$ (USD)": sizes})
        ax = fire.plot.bar(x="Price Composition", y="$ (USD)")
        st.bar_chart(fire, x="Price Composition", y="$ (USD)")

  

