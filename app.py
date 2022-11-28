import streamlit as st
import pandas as pd


def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


if navigation() == "home":
    st.title('Home')
    st.write('This is the home page.')

elif navigation() == "results":
    st.title('Results List')
    for item in range(25):
        st.write(f'Results {item}')

elif navigation() == "analysis":
    st.title('Analysis')
    x, y = st.number_input('Input X'), st.number_input('Input Y')
    st.write('Result: ' + str(x+y))

elif navigation() == "examples":
    st.title('Examples Menu')
    st.write('Select an example.')


elif navigation() == "logs":
    st.title('View all of the logs')
    st.write('Here you may view all of the logs.')


elif navigation() == "verify":
    st.title('Data verification is started...')
    st.write('Please stand by....')


elif navigation() == "config":
    st.title('Configuration of the app.')
    st.write('Here you can configure the application')



st.title("Data Mining")

dataset = pd.read_csv("https://raw.githubusercontent.com/RagilSalsabil/datamining/gh-pages/drug200.csv")
st.dataframe(dataset)

st.subheader("inputan")
na_to_k = st.text_input("Na_to_K")
sex = st.radio(
    "Sex",
    ('F', 'M'))

bp = st.selectbox(
    'BP',
    ('Low', 'Normal', 'High'))

cholestrol = st.selectbox(
    'Cholestrol',
    ('Low', 'Normal', 'High'))

drug = st.selectbox(
    'Drug',
    ('DrugA', 'DrugB', 'DrugC','DrugY','DrugX'))

submit = st.button("submit")
