import pandas as pd
import streamlit as st
import webbrowser

st.set_page_config(
    page_title="FIFA 23",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("/Users/lucasmelo/Documents/Asimov/Criando Aplicativos Web com Streamlit/Projeto Streamlit FIFA/datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    st.session_state["data"] = df_data


st.markdown("# FIFA 23 DATASET OFICIAL!") 
st.sidebar.markdown("Desenvolvido por [Lucas Requião](https://instagram.com/lucas.requiao)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/sanjeetsinghnaik/fifa-23-players-dataset/data")

