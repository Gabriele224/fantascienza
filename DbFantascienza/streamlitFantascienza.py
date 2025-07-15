import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components
from PIL import Image
import base64 ,re

st.title("Universi da Leggere")

def encode_image_to_base64(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        ext = os.path.splitext(img_path)[1][1:]  # esempio: jpg, png
        return f"data:image/{ext};base64,{encoded_string}"

def embed_images_in_html(html_content, base_folder):
    matches = re.findall(r'<img\s+[^>]*src="([^"]+)"', html_content)
    for src in matches:
        img_path = os.path.join(base_folder, src)
        if os.path.exists(img_path):
            img_data_uri = encode_image_to_base64(img_path)
            html_content = html_content.replace(src, img_data_uri)
    return html_content

PATH_HTML_TRAMALIBRI="./DbFantascienza/TRAMA"

PATH_HTML_VITASCRITTORI="./DbFantascienza/VITASCRITTORI"

st.write("Trama dei Libri Fantascientifici")

html_pages_trama = [file for file in os.listdir(PATH_HTML_TRAMALIBRI) if file.endswith(".html")]

# Mostra nel menu solo il nome senza estensione
display_names = [os.path.splitext(f)[0] for f in html_pages_trama]

box_html_tramalibri= st.selectbox("Seleziona il Libro\n", display_names)

if st.button("Ricerca Libro", box_html_tramalibri):

    # Ricostruisci il nome completo del file
    selected_file = box_html_tramalibri + ".html"

    file_path= os.path.join(PATH_HTML_TRAMALIBRI,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()
    contenuto = embed_images_in_html(contenuto, PATH_HTML_TRAMALIBRI)
    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")


st.write("Vita Degli Scrittori")

html_pages_Scrittori = [file for file in os.listdir(PATH_HTML_VITASCRITTORI) if file.endswith(".html")]

# Mostra nel menu solo il nome senza estensione
display_names_scrittori = [os.path.splitext(f)[0] for f in html_pages_Scrittori]

box_html_scrittori= st.selectbox("Seleziona lo scrittore\n", display_names_scrittori)

if st.button("Ricerca Scrittore", box_html_scrittori):

    # Ricostruisci il nome completo del file
    selected_file = box_html_scrittori + ".html"

    file_path= os.path.join(PATH_HTML_VITASCRITTORI,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()
    contenuto = embed_images_in_html(contenuto, PATH_HTML_VITASCRITTORI)
    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")
