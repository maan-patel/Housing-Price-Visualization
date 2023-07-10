import pandas as pd
import numpy as np
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
import streamlit as st

@st.cache_data
def regression():
    raw_data_train = pd.read_csv('https://raw.githubusercontent.com/jmpark0808/pl_mnist_example/main/train_hp_msci436.csv')
    df = raw_data_train.select_dtypes(include = ['float64', 'int64']).fillna(0) 
    X = df.values[:, 1:-1]
    y = df.values[:, -1]
    return {'model':LinearRegression().fit(X, y), 'df': df, 'data': raw_data_train}

@st.cache_data
def summarize_df(df):
    numeric_summary = pd.DataFrame()
    categorical_summary = pd.DataFrame()

    for col in df.columns:
        if df[col].dtypes in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']:
            stats = {
                'min': df[col].min(),
                'max': df[col].max(),
                'mean': df[col].mean(),
                'std_dev': df[col].std(),
                'variance': df[col].var(),
                'skewness': df[col].skew(),
            }
            numeric_summary[col] = pd.Series(stats)
        elif df[col].dtypes == 'object':
            stats = {
                'na_count': df[col].isna().sum(),
                'unique_values': df[col].nunique(),
            }
            categorical_summary[col] = pd.Series(stats)

    return numeric_summary, categorical_summary


def create_column_intervals(df, column_name, num_intervals,name_of_category):
    # Compute equal interval width
    interval_width = (df[column_name].max() - df[column_name].min()) / num_intervals

    # Create the intervals and corresponding labels
    intervals = [round(df[column_name].min() + i * interval_width, -int(np.floor(np.log10(abs(interval_width)))) + 1)
                 for i in range(num_intervals + 1)]
    labels = [f"${intervals[i]:,.0f}-{intervals[i+1]:,.0f}" for i in range(num_intervals)]

    # Assign categories based on the intervals
    df[name_of_category] = pd.cut(df[column_name], bins=intervals, labels=labels, include_lowest=True)

    return df

# create_price_intervals(raw_data_train, "", 8, '')
# raw_data_train.to_csv("out1_cat_price.csv")
    
