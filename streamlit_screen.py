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
    st.session_state['Price'] = totalRooms
    

# def sidebar_price(price, metric, update=False): # down should either be 'up' or 'down'
    
#     if update:
#         # Using "with" notation
        
#         metric.update(label="Price", value=price, delta=price)
            
# def sidebar_price_update(new_price): # down should either be 'up' or 'down'

#     # Using "with" notation
#     with st.sidebar:
#         title = st.title(
#             "Predicted Price of the house"
#         )
#         st.metric.update(value =new_price, delta)

        
