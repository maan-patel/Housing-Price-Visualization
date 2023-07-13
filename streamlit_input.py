import streamlit as st

def radio_for_totalrooms(coeff, min, max):
    st.subheader("How many total Bedrooms in the house do you want?")
    totalRooms = st.slider('Slide to the desired number',
                           int(min), int(max), int((min+max)/2))
    # st.write("On average, if a house has", totalRooms, "total rooms, the price of the house may be around $", coeff*totalRooms)
    return totalRooms

def radio_for_fullbathrooms(coeff, min, max):
    st.subheader("How many total Full Bathrooms in the house do you want?")
    totalRooms = st.slider('Slide to the desired number',
                           int(min), int(max), int((min+max)/2))
    # st.write("On average, if a house has", totalRooms, "total rooms, the price of the house may be around $", coeff*totalRooms)
    return totalRooms

def radio_for_halfbathrooms(coeff, min, max):
    st.subheader("How many total Half Bathrooms in the house do you want?")
    totalRooms = st.slider('Slide to the desired number',
                           int(min), int(max), int((min+max)/2))
    # st.write("On average, if a house has", totalRooms, "total rooms, the price of the house may be around $", coeff*totalRooms)
    return totalRooms
    

def number_for_square_footage(coeff, min, max):
    st.subheader("How much total Lot Area do you want? (in Sq Ft)")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})', min_value=int(
        min), max_value=int(max), step=100)
    return number
    # st.write("On average, if a house has", number, "total rooms, the price of the house may be around $", coeff*number)

def number_of_garage_cars(coeff, min, max):
    st.subheader("How much total Car Garages do you want?")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})', min_value=int(
        min), max_value=int(max), step=1)
    return number
    # st.write("On average, if a house has", number, "total rooms, the price of the house may be around $", coeff*number)


def overall_condition(coeff, min, max):
    st.subheader(
        "What overall house condition do you want? (material and finish quality)")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})', min_value=int(
        min), max_value=int(max), step=1)
    return number
    # st.write("On average, if a house has", number, "total condition, the price of the house may be around $", coeff*number)


def overall_age(coeff, min, max):
    st.subheader("How old do you want your house?")
    old = st.slider('Slide to the desired number (in years)',
                    min_value=int(min), max_value=int(max))
    # st.write("On average, if a house has", number, "total condition, the price of the house may be around $", coeff*number)
    return old

# def overall_reno_age(coeff, min, max):
#     st.subheader("Whe you want your house?")
#     old = st.slider('Slide to the desired number (in years)',
#                     min_value=int(min), max_value=int(max))
#     # st.write("On average, if a house has", number, "total condition, the price of the house may be around $", coeff*number)
#     return old



def number_of_wodden_deck_area(coeff, min, max):
    st.subheader("How much Wodden Deck Area do you want? (in sq feet)")
    number = st.number_input(f'Insert a number (min: {min}, max: {max})', min_value=int(
        min), max_value=int(max), step =50)
    return number
    # st.write("On average, if a house has", number, "total rooms, the price of the house may be around $", coeff*number)

def do_you_want_pool(coeff, min, max):
    st.subheader("Do you want a Pool?")
    option = st.selectbox(
    'Please enter Yes/No',
    ('No', 'Yes'),key=2)
    
    if option == 'Yes':
        st.subheader("How much Pool Area Area do you want? (in sq feet)")
        number = st.number_input(f'Insert a number (min: {min}, max: {max})', min_value=int(
            min), max_value=int(max), step =50)
        return number
    else:
        return 0


def do_you_want_fireplace(coeff, min, max):
    st.subheader("Do you want a Fireplace?")
    option = st.selectbox(
    'Please enter Yes/No',
    ('No', 'Yes'),key=1)
    
    if option == 'Yes':
        st.subheader("How many Fireplaces do you want?")
        number = st.number_input(f'Insert a number (min: {min}, max: {max})', min_value=int(
            min), max_value=int(max), step =1)
        return number
    else:
        return 0