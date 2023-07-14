import streamlit as st
from streamlit_input import *


def intro():
    st.title('Housing Prices Visualization')
    st.write('''Understanding what factors affect the price of a house can be very
            valuable to a realtor and a new home buyer. A realtor’s objective is to
            help home buyers and sellers get the best deal possible. Realtors will
            benefit from the ML system by being able to assist their clients as a 
            result of a better understanding of the factors that influence house prices.
    ''')


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
    cars = number_of_garage_cars(coefficients[columns.get_loc(
        'GarageCars')], df['GarageCars']['min'], df['GarageCars']['max'])
    old = overall_age(coefficients[columns.get_loc(
        'YearBuilt')], 2011-int(df['YearBuilt']['min']), 2011-int(df['YearBuilt']['max']))
    renovated = overall_reno_age(coefficients[columns.get_loc(
        'YearRemodAdd')], 2011-int(df['YearRemodAdd']['min']), 2011-int(df['YearRemodAdd']['max']))
    # pool_area = do_you_want_pool(coefficients[columns.get_loc(
    #     'PoolArea')], df['PoolArea']['min'], df['PoolArea']['max'])
    fireplaces = do_you_want_fireplace(coefficients[columns.get_loc(
        'Fireplaces')], df['Fireplaces']['min'], df['Fireplaces']['max'])
    externalCondition = evaluate_external_condition()
    heating_condition = evaluate_heating_condition()
    centralAir = air_condition()

    linear_regression_for_new_price = calculate_new_price(
        intercept, columns, coefficients, rooms, 'TotRmsAbvGrd', footage, 'LotArea', condition,
        'OverallQual', old, 'YearBuilt', fireplaces, 'Fireplaces', renovated, 'YearRemodAdd',
        fullbath_rooms, 'FullBath', halfbath_rooms, 'HalfBath', cars, 'GarageCars', centralAir, '',
        externalCondition, '', heating_condition, '')
    
    if 'PriceChange' not in st.session_state:
        st.session_state['PriceChange'] = 0
    else:
        st.session_state['PriceChange'] = st.session_state["Price"] - \
            linear_regression_for_new_price
            
    if 'Price' not in st.session_state:
        st.session_state['Price'] = intercept
    else:
        st.session_state['Price'] = linear_regression_for_new_price


def calculate_new_price(intercept, columns, coefficients, *args):
    price = intercept
    for i in range(0, len(args), 2):
        if args[i+1] == '':
            price += args[i]
        else:
            price += coefficients[columns.get_loc(args[i+1])] * args[i]
    return price
