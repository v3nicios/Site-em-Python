import streamlit as st

from funções_pequenas import *

def exibir_personagens(data):
    if data:
        for character in data:
            with st.container():
                col1, col2, col3 = st.columns([1, 2, 3])

                with col1:
                    if "image" in character and character["image"]:
                        img_html = f"""
                        <img src="{character['image']}" style="width: 300px; height: 300px; object-fit: fill; border-radius: 12%; box-sizing: border-box;">
                        """
                        st.markdown(img_html, unsafe_allow_html=True)
                    else:
                        st.write("🖼️ Sem imagem disponível")

                with col2:
                    st.subheader(character["name"])
                    st.write(f" **Nomes alternativos:** {', '.join(character['alternate_names'])}")
                    st.write(f" **Ator:** {character['actor']}")
                    st.write(f" **Casa de Hogwarts:** {character['house']}")
                    st.write(f" **Data de nascimento:** {character['dateOfBirth'].replace('-', '/') if character['dateOfBirth'] else 'N/A'}")
                    st.write(f" **Ancestrais:** {character['ancestry']}")
                    st.write(f" **Patronus:** {character['patronus']}")
                    st.write(f" **Bruxo/Trouxa?:** {E_bruxo(character['wizard'])}")
                    st.write(f" **Estudante de Hogwarts?:** {estuda_em_hog(character['hogwartsStudent'])}")
                    st.write(f" **Funcionário de Hogwarts?:** {Membrohog(character['hogwartsStaff'])}")
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
