import streamlit as st
from forex_python.converter import CurrencyRates
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()
c = CurrencyRates()

def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude
    except Exception as e:
        return str(e)

def convert_currency(amount, from_currency, to_currency):
    try:
        rate = c.get_rate(from_currency, to_currency)
        return amount * rate
    except Exception as e:
        return str(e)

st.title("Universal Unit Converter")

# Sidebar for selection
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Currency", "Speed", "Time", "Volume", "Area"])

unit_options = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter"],
    "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter per second", "kilometer per hour", "mile per hour", "knot"],
    "Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "Volume": ["liter", "milliliter", "gallon", "cubic meter", "cubic foot"],
    "Area": ["square meter", "square kilometer", "square mile", "hectare", "acre"]
}

if conversion_type == "Currency":
    amount = st.number_input("Enter Amount", min_value=0.0, value=1.0)
    from_currency = st.text_input("From Currency (e.g., USD)", "USD").upper()
    to_currency = st.text_input("To Currency (e.g., EUR)", "EUR").upper()
    if st.button("Convert"):
        result = convert_currency(amount, from_currency, to_currency)
        st.success(f"Converted Amount: {result} {to_currency}")
else:
    value = st.number_input("Enter Value", min_value=0.0, value=1.0)
    from_unit = st.selectbox("From Unit", unit_options.get(conversion_type, ["Select a unit"]))
    to_unit = st.selectbox("To Unit", unit_options.get(conversion_type, ["Select a unit"]))
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")

st.write("Happy Converting..😊")