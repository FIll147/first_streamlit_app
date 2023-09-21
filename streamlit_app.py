import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('BreakFast Menu')
streamlit.text('🥣 Omega3 & Blueberry')
streamlit.text('🥗 Kale, Spinach & ROcket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list =pandas.read_cvs(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
