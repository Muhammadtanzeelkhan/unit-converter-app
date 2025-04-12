import streamlit as st

st.title ("🌎Unit Converter")
st.markdown("Convert Lenght, Weight, and Time units")
st.write("Welcome! This is a simple unit converter app. You can convert between different units of length, weight, and time.")

catagory = st.selectbox("💠Select a category", ["Length", "Weight", "Time"])

def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "feet": 0.3048,
        "inches": 0.0254
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_time(value, from_unit, to_unit):
    time_units = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }
    return value * (time_units[to_unit] / time_units[from_unit])

if catagory == "Length":
    unit = st.selectbox("📏Select a unit", ["meters", "kilometers", "centimeters", "millimeters", "feet", "inches"])
elif catagory == "Weight":
    unit = st.selectbox("⚖️Select a unit", ["grams", "kilograms", "pounds", "ounces"])
elif catagory == "Time":
    unit = st.selectbox("⏳Select a unit", ["seconds", "minutes", "hours", "days"])

value = st.number_input("Enter the value to convert")   

if st.button ("Convert"):
    if catagory == "Length":
        from_unit = unit
        to_unit = st.selectbox("Select the unit to convert to", ["meters", "kilometers", "centimeters", "millimeters", "feet", "inches"])
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
    elif catagory == "Weight":
        from_unit = unit
        to_unit = st.selectbox("Select the unit to convert to", ["grams", "kilograms", "pounds", "ounces"])
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
    elif catagory == "Time":
        from_unit = unit
        to_unit = st.selectbox("Select the unit to convert to", ["seconds", "minutes", "hours", "days"])
        result = convert_time(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")


st.write("Thank you for using the unit converter!")
st.write("If you have any questions or feedback, please let us know.")
st.write("Happy converting!")
st.write("Made with ❤️ by MUHAMMAD TANZEEL")
st.write("This app is built using Streamlit, a powerful framework for building web apps in Python.")

