import streamlit as st

st.set_page_config(
    page_title="FIFA 23 - Times",
    page_icon="⚽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
clube = st.sidebar.selectbox("Clubes", clubes)

clube_stats = df_data[(df_data["Club"] == clube)].set_index("Name")
st.image(clube_stats["Club Logo"].iloc[0])
st.markdown(f"## {clube}")

colunas = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(clube_stats[colunas],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=clube_stats["Wage(£)"].max()),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country", width="small"),
             })