import streamlit as st
from domain import calcula_notas
pesos = [1,2,3,4,5]

st.title("Minha Nota Sisu")

col1, col2 = st.columns(2)

with col1:
    st.session_state.nota_linguagens = st.number_input("Linguagens, Códigos e suas Tecnologias", max_value=1000.0, step=1.0)
    st.session_state.nota_humanas = st.number_input("Ciências Humanase suas Tecnologias", max_value=1000.0, step=1.0)
    st.session_state.nota_natureza = st.number_input("Ciências da Natureza e suas Tecnologias", max_value=1000.0, step=1.0)
    st.session_state.nota_matematica =  st.number_input("Matemática e suas Tecnologias", max_value=1000.0, step=1.0)
    st.session_state.nota_redacao = st.number_input("Redação", max_value=1000.0, step=1.0,)

with col2:  
    st.session_state.peso_linguagens = st.selectbox("Peso Linguagens", pesos)
    st.session_state.peso_humanas = st.selectbox("Peso Ciências Humanas", pesos)
    st.session_state.peso_natureza = st.selectbox("Peso Ciências da Natureza", pesos)
    st.session_state.peso_matematica = st.selectbox("Peso Matemática", pesos)
    st.session_state.peso_redacao = st.selectbox("Peso Redação", pesos)
    st.button('Calcular Nota', use_container_width=True , on_click=calcula_notas)

if 'media_ponderada' in st.session_state:
    st.header('Notas')
    st.write(f'Média Simples: {st.session_state.media:.2f}')
    st.write(f'Media Ponderada: {st.session_state.media_ponderada:.2f}')
