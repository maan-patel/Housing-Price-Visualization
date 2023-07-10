import streamlit as st

def intro():
    st.title('Housing Prices Visualization')
    st.write('''Understanding what factors affect the price of a house can be very
            valuable to a realtor and a new home buyer. A realtor’s objective is to
            help home buyers and sellers get the best deal possible. Realtors will
            benefit from the ML system by being able to assist their clients as a 
            result of a better understanding of the factors that influence house prices.
    ''')


def radio_for_bedrooms(coeff):
    totalRooms = st.slider('How many total rooms in the house do you want?'
                    , 2, 14, 6)
    st.write("On average, if a house has", totalRooms, "total rooms, the price of the house may be around $", coeff*totalRooms)
    
    st.session_state['PriceChange'] = st.session_state['Price'] - totalRooms
    st.session_state['Price'] = st.session_state['Price'] - totalRooms
    
