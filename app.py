import streamlit as st

st.write("Simple illustration of finding max of three numbers")

st.header("User Inputs numbers")

def user_input_number():
  number1 = st.number_input("number_1")
  number2 = st.number_input("number_2")
  number3 = st.number_input("number_3")

  if number1 > number2 and number1 > number3:
    result = number1
  elif number2 > number1 and number2 > number3:
    result = number2
  elif number3 > number1 and number3 > number2:
    result = number3
  elif number1 == number2 and number2 == number3:
    result = "All number are equal"
  
  return result

result = user_input_number()

st.subheader('Here is the max of 3 number')
st.wirte(result)
