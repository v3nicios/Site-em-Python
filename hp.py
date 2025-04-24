import streamlit as st
import requests
from funções_pequenas import *
from corpo import *

st.set_page_config(layout="wide")

Page_cliente = st.sidebar.selectbox(
    "Escolhas",
    ["Casas de Hogwarts", "Todos os personagens", "Todos os feitiços conhecidos"],
)

if Page_cliente == "Casas de Hogwarts":
    st.subheader("Casas de Hogwarts")
    Escolha_das_casas = st.selectbox(
        "", ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
    )
    if Escolha_das_casas == "Gryffindor":

        def fetch_data():
            url = "https://hp-api.onrender.com/api/characters/house/Gryffindor"
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()
            else:
                st.error("Erro ao buscar API")
                return []

        data = fetch_data()
        
        exibir_personagens(data)

        search_query = st.text_input("Pesquisar personagem:")

        
        

        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
        

    if Escolha_das_casas == "Ravenclaw":

        def fetch_data():
            url = "https://hp-api.onrender.com/api/characters/house/Ravenclaw"
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()
            else:
                st.error("Erro ao buscar API")
                return []

        
        data = fetch_data()
        exibir_personagens(data)

        search_query = st.text_input("Pesquisar personagem:")

        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
        

    if Escolha_das_casas == "Hufflepuff":

        def fetch_data():
            url = "https://hp-api.onrender.com/api/characters/house/Hufflepuff"
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()
            else:
                st.error("Erro ao buscar API")
                return []

        
        data = fetch_data()
        exibir_personagens(data)

        search_query = st.text_input("Pesquisar personagem:")

        
        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
        

    if Escolha_das_casas == "Slytherin":

        def fetch_data():
            url = "https://hp-api.onrender.com/api/characters/house/Slytherin"
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()
            else:
                st.error("Erro ao buscar API")
                return []

        
        data = fetch_data()
        
        exibir_personagens(data)

        search_query = st.text_input("Pesquisar personagem:")
        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
       
if Page_cliente == "Todos os personagens":

    def fetch_data():
        url = "https://hp-api.onrender.com/api/characters"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            st.error("Erro ao buscar API")
            return []
    
    data = fetch_data()
    exibir_personagens(data)

    search_query = st.text_input("Pesquisar personagem:")

    if search_query:
        data = [char for char in data if search_query.lower() in char["name"].lower()]


if Page_cliente == "Todos os feitiços conhecidos":
    def fetch_data():
        url = "https://api.potterdb.com/v1/spells"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()  
        else:
            st.error("Erro ao buscar API")
            return {}

    data = fetch_data()

    if isinstance(data, dict) and 'data' in data and isinstance(data['data'], list):
        for character in data['data']:  
            with st.container():
                spell_name = character['attributes']['name']  
                st.subheader(spell_name)
                
                col1, col2 = st.columns([1, 2])  
                with col1:
                    if character['attributes'].get('image'):
                        img_html = f"""
                        <img src="{character['attributes']['image']}" style="width: 170px; height: 150px; border-radius: 10%;">
                        """
                        st.markdown(img_html, unsafe_allow_html=True)

                with col2:
                    st.write(f"**Categoria:** {character['attributes'].get('category', 'Desconhecida')}")
                    st.write(f"**Efeito:** {character['attributes'].get('effect', 'Sem descrição')}")
                    st.write(f"**Encantamento:** {character['attributes'].get('incantation', 'Sem descrição')}")
                    st.write(f"**Luz:** {character['attributes'].get('light', 'Sem descrição')}")

                st.markdown("***")  
    else:
        st.error("Os dados não estão no formato esperado ou estão vazios.")


















