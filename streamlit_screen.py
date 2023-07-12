import streamlit as st

def intro():
    st.title('Housing Prices Visualization')
    st.write('''Understanding what factors affect the price of a house can be very
            valuable to a realtor and a new home buyer. A realtor’s objective is to
            help home buyers and sellers get the best deal possible. Realtors will
            benefit from the ML system by being able to assist their clients as a 
            result of a better understanding of the factors that influence house prices.
    ''')

def get_all_input(df,columns,coefficients):
 
    radio_for_totalrooms(coefficients[columns.get_loc('TotRmsAbvGrd')], df['TotRmsAbvGrd']['min'],df['TotRmsAbvGrd']['max'])
    number_for_square_footage(coefficients[columns.get_loc('LotArea')], df['LotArea']['min'],df['LotArea']['max'])
    overall_condition(coefficients[columns.get_loc('OverallQual')], df['OverallQual']['min'],df['OverallQual']['max'])


def radio_for_totalrooms(coeff, min, max):
    st.subheader("How many total rooms in the house do you want?")
    totalRooms = st.slider('Slide to the desired number'
                    , int(min), int(max), int((min+max)/2))
    # st.write("On average, if a house has", totalRooms, "total rooms, the price of the house may be around $", coeff*totalRooms)
    
    # st.session_state['PriceChange'] = totalRooms
    # st.session_state['Price'] = st.session_state['Price'] - totalRooms
    
def number_for_square_footage(coeff, min, max):
    st.subheader("How much total Lot Area do you want? (in Sq Ft)")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})',min_value=int(min), max_value=int(max), step=100)
    # st.write("On average, if a house has", number, "total rooms, the price of the house may be around $", coeff*number)

def overall_condition(coeff, min, max):
    st.subheader("How much overall condition you want? (Overall material and finish quality)")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})',min_value=int(min), max_value=int(max), step=1)
    # st.write("On average, if a house has", number, "total condition, the price of the house may be around $", coeff*number)

def overall_condition(coeff, min, max):
    st.subheader("How much overall condition (material and finish quality) you want?")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})',min_value=int(min), max_value=int(max), step=1)
    # st.write("On average, if a house has", number, "total condition, the price of the house may be around $", coeff*number)

def overall_condition(coeff, min, max):
    st.subheader("How much overall condition (material and finish quality) you want?")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})',min_value=int(min), max_value=int(max), step=1)
    # st.write("On average, if a house has", number, "total condition, the price of the house may be around $", coeff*number)

