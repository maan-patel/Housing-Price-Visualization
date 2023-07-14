import streamlit as st
from streamlit_input import *
import charts as c


def intro():
    st.title('Housing Prices Visualization')
    st.write('''Understanding what factors affect the price of a house can be very
            valuable to a realtor and a new home buyer. A realtor’s objective is to
            help home buyers and sellers get the best deal possible. Realtors will
            benefit from the ML system by being able to assist their clients as a 
            result of a better understanding of the factors that influence house prices.
    ''')

def display_charts(df, columns, coefficients):
    st.header("How do different features affect the price of housing?")

    st.subheader("Does the home contain a fireplace?")
    c.fireplace_chart(df, columns, coefficients)

    st.subheader("How many cars does the garage hold?")
    c.garage_chart(df, columns, coefficients)


def get_all_input(df, columns, coefficients, intercept):
    rooms = radio_for_totalrooms(coefficients[columns.get_loc(
        'BedroomAbvGr')], df['BedroomAbvGr']['min'], df['BedroomAbvGr']['max'])
    fullbath_rooms = radio_for_fullbathrooms(coefficients[columns.get_loc(
        'FullBath')], df['FullBath']['min'], df['FullBath']['max'])
    halfbath_rooms = radio_for_halfbathrooms(coefficients[columns.get_loc(
        'HalfBath')], df['HalfBath']['min'], df['HalfBath']['max'])
    footage = number_for_square_footage(coefficients[columns.get_loc(
        'LotArea')], df['LotArea']['min'], df['LotArea']['max'])
    condition = overall_condition(coefficients[columns.get_loc(
        'OverallQual')], df['OverallQual']['min'], df['OverallQual']['max'])

    cars = number_of_garage_cars(
    coefficients[columns.get_loc('GarageCars')],
    df['GarageCars']['min'],
    df['GarageCars']['max'])

    old = overall_age(coefficients[columns.get_loc(
        'YearBuilt')], 2011-int(df['YearBuilt']['min']), 2011-int(df['YearBuilt']['max']))
    # renovated = overall_reno_age(coefficients[columns.get_loc(
    #     'years_since_remod')], 2011-int(df['years_since_remod']['min']), 2011-int(df['years_since_remod']['max']))
    pool_area = do_you_want_pool(coefficients[columns.get_loc(
        'PoolArea')], df['PoolArea']['min'], df['PoolArea']['max'])
    fireplaces = do_you_want_fireplace(
        coefficients[columns.get_loc('Fireplaces')],
        df['Fireplaces']['min'],
        df['Fireplaces']['max'])

    linear_regression_for_new_price = calculate_new_price(
        intercept, columns, coefficients, rooms, 'TotRmsAbvGrd', footage, 'LotArea', condition,
        'OverallQual', old, 'YearBuilt', pool_area, 'PoolArea', fireplaces, 'Fireplaces',
        fullbath_rooms, 'FullBath', halfbath_rooms, 'HalfBath', cars, 'GarageCars')
    if 'PriceChange' not in st.session_state:
        st.session_state['PriceChange'] = 0
    else:
        st.session_state['PriceChange'] = st.session_state["Price"] - \
            linear_regression_for_new_price
    st.session_state['Price'] = linear_regression_for_new_price

def calculate_new_price(intercept, columns, coefficients, *args):
    price = intercept
    for i in range(0, len(args), 2):
        price += coefficients[columns.get_loc(args[i+1])] * args[i]
    return price
