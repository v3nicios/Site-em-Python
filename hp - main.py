import streamlit as st
import requests

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

        search_query = st.text_input("Pesquisar personagem:")

        
        def eh_bruxo_para_string(eh_bruxo):
            return "BRUXO" if eh_bruxo else "TROUXA"

        def estuda_em_hog(estudante):
            return "Sim" if estudante else "Não"

        def Membrohog(membro):
            return "Sim" if membro else "Não"

        def Ta_vivo(tavivo):
            return "Sim" if tavivo else "Não"

        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
        if data:
            for character in data:
                with st.container():
                    col1, col2, col3 = st.columns(
                        [1, 2, 3]
                    )  

                    with col1:
                        if "image" in character and character["image"]:
                            
                            img_html = f"""
                            <img src="{character['image']}" style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%; box-sizing: border-box;">
                            """
                            st.markdown(img_html, unsafe_allow_html=True)
                        else:
                            st.write("🖼️ Sem imagem disponível")

                    with col2:

                        st.subheader(character["name"])

                        st.write(
                            f" **Nomes alternativos:** {', '.join(character['alternate_names'])}"
                        )

                        st.write(f" **Ator:** {character['actor']}")

                        st.write(f" **Casa de Hogwarts:** {character['house']}")

                        st.write(
                            f" **Data de nascimento:** {character['dateOfBirth'].replace('-', '/') if character['dateOfBirth'] else 'N/A'}"
                        )

                        st.write(f" **Ancestrais:** {character['ancestry']}")

                        st.write(f" **Patronus:** {character['patronus']}")

                        st.write(
                            f" **Bruxo/Trouxa?:** {eh_bruxo_para_string(character['wizard'])}"
                        )
                        st.write(
                            f" **Estudante de Hogwarts?:** {estuda_em_hog(character['hogwartsStudent'])}"
                        )
                        st.write(
                            f" **Funcionário de Hogwarts?:** {Membrohog(character['hogwartsStaff'])}"
                        )

                        st.write(f" **Vivo?:** {Ta_vivo(character['alive'])}")

                    with col3:

                        st.subheader("Características físicas")

                        st.write(f" **Cor dos olhos:** {character['eyeColour']}")

                        st.write(f" **Cor do cabelo:** {character['hairColour']}")

                        st.write(f" **Gênero:** {character['gender']}")

                        st.write(f" **Espécie:** {character['species']}")

                        st.subheader("Varinha")
                        st.write(f" **Feita de:** {character['wand']['wood']}")

                        st.write(f" **Núcleo:** {character['wand']['core']}")

                        st.write(f" **Tamanho:** {character['wand']['length']}")

                    
                    st.markdown("***")

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

        search_query = st.text_input("Pesquisar personagem:")

        
        def eh_bruxo_para_string(eh_bruxo):
            return "BRUXO" if eh_bruxo else "TROUXA"

        def estuda_em_hog(estudante):
            return "Sim" if estudante else "Não"

        def Membrohog(membro):
            return "Sim" if membro else "Não"

        def Ta_vivo(tavivo):
            return "Sim" if tavivo else "Não"

        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
        if data:
            for character in data:
                with st.container():
                    col1, col2, col3 = st.columns(
                        [1, 2, 3]
                    )  

                    with col1:
                        if "image" in character and character["image"]:
                            
                            img_html = f"""
                            <img src="{character['image']}" style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%; box-sizing: border-box;">
                            """
                            st.markdown(img_html, unsafe_allow_html=True)
                        else:
                            st.write("🖼️ Sem imagem disponível")

                    with col2:

                        st.subheader(character["name"])

                        st.write(
                            f" **Nomes alternativos:** {', '.join(character['alternate_names'])}"
                        )

                        st.write(f" **Ator:** {character['actor']}")

                        st.write(f" **Casa de Hogwarts:** {character['house']}")

                        st.write(
                            f" **Data de nascimento:** {character['dateOfBirth'].replace('-', '/') if character['dateOfBirth'] else 'N/A'}"
                        )

                        st.write(f" **Ancestrais:** {character['ancestry']}")

                        st.write(f" **Patronus:** {character['patronus']}")

                        st.write(
                            f" **Bruxo/Trouxa?:** {eh_bruxo_para_string(character['wizard'])}"
                        )
                        st.write(
                            f" **Estudante de Hogwarts?:** {estuda_em_hog(character['hogwartsStudent'])}"
                        )
                        st.write(
                            f" **Funcionário de Hogwarts?:** {Membrohog(character['hogwartsStaff'])}"
                        )
                        st.write(f" **Vivo?:** {Ta_vivo(character['alive'])}")

                    with col3:

                        st.subheader("Características físicas")

                        st.write(f" **Cor dos olhos:** {character['eyeColour']}")

                        st.write(f" **Cor do cabelo:** {character['hairColour']}")

                        st.write(f" **Gênero:** {character['gender']}")

                        st.write(f" **Espécie:** {character['species']}")

                        st.subheader("Varinha")
                        st.write(f" **Feita de:** {character['wand']['wood']}")

                        st.write(f" **Núcleo:** {character['wand']['core']}")

                        st.write(f" **Tamanho:** {character['wand']['length']}")

                    
                    st.markdown("***")

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

        search_query = st.text_input("Pesquisar personagem:")

        
        def eh_bruxo_para_string(eh_bruxo):
            return "BRUXO" if eh_bruxo else "TROUXA"

        def estuda_em_hog(estudante):
            return "Sim" if estudante else "Não"

        def Membrohog(membro):
            return "Sim" if membro else "Não"

        def Ta_vivo(tavivo):
            return "Sim" if tavivo else "Não"

        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
        if data:
            for character in data:
                with st.container():
                    col1, col2, col3 = st.columns(
                        [1, 2, 3]
                    )  

                    with col1:
                        if "image" in character and character["image"]:
                            
                            img_html = f"""
                            <img src="{character['image']}" style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%; box-sizing: border-box;">
                            """
                            st.markdown(img_html, unsafe_allow_html=True)
                        else:
                            st.write("🖼️ Sem imagem disponível")

                    with col2:

                        st.subheader(character["name"])

                        st.write(
                            f" **Nomes alternativos:** {', '.join(character['alternate_names'])}"
                        )

                        st.write(f" **Ator:** {character['actor']}")

                        st.write(f" **Casa de Hogwarts:** {character['house']}")

                        st.write(
                            f" **Data de nascimento:** {character['dateOfBirth'].replace('-', '/') if character['dateOfBirth'] else 'N/A'}"
                        )

                        st.write(f" **Ancestrais:** {character['ancestry']}")

                        st.write(f" **Patronus:** {character['patronus']}")

                        st.write(
                            f" **Bruxo/Trouxa?:** {eh_bruxo_para_string(character['wizard'])}"
                        )
                        st.write(
                            f" **Estudante de Hogwarts?:** {estuda_em_hog(character['hogwartsStudent'])}"
                        )
                        st.write(
                            f" **Funcionário de Hogwarts?:** {Membrohog(character['hogwartsStaff'])}"
                        )
                        st.write(f" **Vivo?:** {Ta_vivo(character['alive'])}")

                    with col3:

                        st.subheader("Características físicas")

                        st.write(f" **Cor dos olhos:** {character['eyeColour']}")

                        st.write(f" **Cor do cabelo:** {character['hairColour']}")

                        st.write(f" **Gênero:** {character['gender']}")

                        st.write(f" **Espécie:** {character['species']}")

                        st.subheader("Varinha")
                        st.write(f" **Feita de:** {character['wand']['wood']}")

                        st.write(f" **Núcleo:** {character['wand']['core']}")

                        st.write(f" **Tamanho:** {character['wand']['length']}")

                    
                    st.markdown("***")

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

        search_query = st.text_input("Pesquisar personagem:")

        
        def eh_bruxo_para_string(eh_bruxo):
            return "BRUXO" if eh_bruxo else "TROUXA"

        def estuda_em_hog(estudante):
            return "Sim" if estudante else "Não"

        def Membrohog(membro):
            return "Sim" if membro else "Não"

        def Ta_vivo(tavivo):
            return "Sim" if tavivo else "Não"

        if search_query:
            data = [
                char for char in data if search_query.lower() in char["name"].lower()
            ]

        
        if data:
            for character in data:
                with st.container():
                    col1, col2, col3 = st.columns(
                        [1, 2, 3]
                    )  

                    with col1:
                        if "image" in character and character["image"]:
                            
                            img_html = f"""
                            <img src="{character['image']}" style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%; box-sizing: border-box;">
                            """
                            st.markdown(img_html, unsafe_allow_html=True)
                        else:
                            st.write("🖼️ Sem imagem disponível")

                    with col2:

                        st.subheader(character["name"])

                        st.write(
                            f" **Nomes alternativos:** {', '.join(character['alternate_names'])}"
                        )

                        st.write(f" **Ator:** {character['actor']}")

                        st.write(f" **Casa de Hogwarts:** {character['house']}")

                        st.write(
                            f" **Data de nascimento:** {character['dateOfBirth'].replace('-', '/') if character['dateOfBirth'] else 'N/A'}"
                        )

                        st.write(f" **Ancestrais:** {character['ancestry']}")

                        st.write(f" **Patronus:** {character['patronus']}")

                        st.write(
                            f" **Bruxo/Trouxa?:** {eh_bruxo_para_string(character['wizard'])}"
                        )
                        st.write(
                            f" **Estudante de Hogwarts?:** {estuda_em_hog(character['hogwartsStudent'])}"
                        )
                        st.write(
                            f" **Funcionário de Hogwarts?:** {Membrohog(character['hogwartsStaff'])}"
                        )
                        st.write(f" **Vivo?:** {Ta_vivo(character['alive'])}")

                    with col3:

                        st.subheader("Características físicas")

                        st.write(f" **Cor dos olhos:** {character['eyeColour']}")

                        st.write(f" **Cor do cabelo:** {character['hairColour']}")

                        st.write(f" **Gênero:** {character['gender']}")

                        st.write(f" **Espécie:** {character['species']}")

                        st.subheader("Varinha")
                        st.write(f" **Feita de:** {character['wand']['wood']}")

                        st.write(f" **Núcleo:** {character['wand']['core']}")

                        st.write(f" **Tamanho:** {character['wand']['length']}")

                    
                    st.markdown("***")

if Page_cliente == "Todos os personagens":

    def fetch_data():
        url = "https://hp-api.onrender.com/api/characters/house/Slytherin"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            st.error("Erro ao buscar API")
            return []

    
    data = fetch_data()

    search_query = st.text_input("Pesquisar personagem:")

    
    def eh_bruxo_para_string(eh_bruxo):
        return "BRUXO" if eh_bruxo else "TROUXA"

    def estuda_em_hog(estudante):
        return "Sim" if estudante else "Não"

    def Membrohog(membro):
        return "Sim" if membro else "Não"

    def Ta_vivo(tavivo):
        return "Sim" if tavivo else "Não"

    if search_query:
        data = [char for char in data if search_query.lower() in char["name"].lower()]

    
    if data:
        for character in data:
            with st.container():
                col1, col2, col3 = st.columns(
                    [1, 2, 3]
                )  

                with col1:
                    if "image" in character and character["image"]:
                        
                        img_html = f"""
                        <img src="{character['image']}" style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%; box-sizing: border-box;">
                        """
                        st.markdown(img_html, unsafe_allow_html=True)
                    else:
                        st.write("🖼️ Sem imagem disponível")

                with col2:

                    st.subheader(character["name"])

                    st.write(
                        f" **Nomes alternativos:** {', '.join(character['alternate_names'])}"
                    )

                    st.write(f" **Ator:** {character['actor']}")

                    st.write(f" **Casa de Hogwarts:** {character['house']}")

                    st.write(
                        f" **Data de nascimento:** {character['dateOfBirth'].replace('-', '/') if character['dateOfBirth'] else 'N/A'}"
                    )

                    st.write(f" **Ancestrais:** {character['ancestry']}")

                    st.write(f" **Patronus:** {character['patronus']}")

                    st.write(
                        f" **Bruxo/Trouxa?:** {eh_bruxo_para_string(character['wizard'])}"
                    )
                    st.write(
                        f" **Estudante de Hogwarts?:** {estuda_em_hog(character['hogwartsStudent'])}"
                    )
                    st.write(
                        f" **Funcionário de Hogwarts?:** {Membrohog(character['hogwartsStaff'])}"
                    )
                    st.write(f" **Vivo?:** {Ta_vivo(character['alive'])}")

                with col3:

                    st.subheader("Características físicas")

                    st.write(f" **Cor dos olhos:** {character['eyeColour']}")

                    st.write(f" **Cor do cabelo:** {character['hairColour']}")

                    st.write(f" **Gênero:** {character['gender']}")

                    st.write(f" **Espécie:** {character['species']}")

                    st.subheader("Varinha")
                    st.write(f" **Feita de:** {character['wand']['wood']}")

                    st.write(f" **Núcleo:** {character['wand']['core']}")

                    st.write(f" **Tamanho:** {character['wand']['length']}")

                
                st.markdown("***")

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

                
                    st.write(f"**Categoria:** {character['attributes'].get('category', 'Desconhecida')}")
                    st.write(f"**Efeito:** {character['attributes'].get('effect', 'Sem descrição')}")

                
                    if character['attributes'].get('image'):
                        
                        
                        img_html = f"""
                        <img src="{character['attributes']['image']}" style="width: 700px; height: 500px; border-radius: 10%;">
                        """
                        st.markdown(img_html, unsafe_allow_html=True)

                    st.markdown("***")  
        else:
            st.error("Os dados não estão no formato esperado ou estão vazios.")


            


















