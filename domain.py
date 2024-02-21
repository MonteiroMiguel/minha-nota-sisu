import streamlit as st

def calcula_peso_total():
    st.session_state.peso_total = st.session_state.peso_linguagens + st.session_state.peso_humanas  + st.session_state.peso_natureza + st.session_state.peso_matematica + st.session_state.peso_redacao
    

def calcula_media_simples():
    st.session_state.media = (st.session_state.nota_linguagens + st.session_state.nota_humanas + st.session_state.nota_natureza + st.session_state.nota_matematica + st.session_state.nota_redacao) / 5
    

def calcula_media_ponderada():
    st.session_state.media_ponderada = ((st.session_state.nota_linguagens * st.session_state.peso_linguagens) + (st.session_state.nota_humanas * st.session_state.peso_humanas) + (st.session_state.nota_natureza * st.session_state.peso_natureza) + (st.session_state.nota_matematica * st.session_state.peso_matematica ) + (st.session_state.nota_redacao * st.session_state.peso_redacao) ) / st.session_state.peso_total

def calcula_notas():
    calcula_peso_total()
    calcula_media_simples()
    calcula_media_ponderada()