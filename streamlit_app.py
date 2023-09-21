import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('BreakFast Menu') #CABEÇALHO/TITULO
streamlit.text('🥣 Omega3 & Blueberry')
streamlit.text('🥗 Kale, Spinach & ROcket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas #IMPORTANDO A BIBLIOTECA PYTHON
#PEGANDO A LISTA DE FRUTAS QUE TEM NA BIBLIOTECA JA CRIADA.
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#CRIANDO UM SELECIONADOR DE FRUTAS PARA INTERAGIR COM O USUÁRIO.
my_fruit_list = my_fruit_list.set_index('Fruit')
#DEFININDO UMA PRE SELEÇÃO.
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avoado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)

