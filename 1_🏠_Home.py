import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="FIFA 23",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("Fifa 23 Players Data.csv", index_col=0)
    st.session_state["data"] = df_data


st.markdown("# FIFA 23 DATASET OFICIAL!") 
st.sidebar.markdown("Desenvolvido por [Lucas Requião](https://instagram.com/lucas.requiao)")

btn = st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/sanjeetsinghnaik/fifa-23-players-dataset/data")


