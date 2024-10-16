import streamlit as st

st.set_page_config(
    page_title="FIFA 23 - Jogadores",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="expanded"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
clube = st.sidebar.selectbox("Clubes", clubes)

df_jogadores = df_data[df_data["Club"] == clube]
jogadores = df_jogadores["Name"].unique()
jogador = st.sidebar.selectbox("Jogadores", jogadores)

jogador_stats = df_jogadores[df_jogadores["Name"] == jogador].iloc[0]
st.image(jogador_stats["Photo"])
st.title(jogador_stats["Name"])

st.markdown(f"**Clube:** {jogador_stats['Club']}")
st.markdown(f"**Posição:** {jogador_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"**Idade:** {jogador_stats['Age']}")
with col2:
    st.markdown(f"**Altura:** {jogador_stats['Height(cm.)']/100}")
with col3:
    st.markdown(f"**Peso:** {jogador_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"**Overall:** {jogador_stats['Overall']}")
st.progress(int(jogador_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Valor de Mercado", value=f"£ {jogador_stats['Value(£)']:,}")
with col2:
    st.metric(label="Remuneração Semanal", value=f"£ {jogador_stats['Wage(£)']:,}")
with col3:
    st.metric(label="Cláusula de Rescisão", value=f"£ {jogador_stats['Release Clause(£)']:,}")

