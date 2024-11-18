import sys
import os

# Adicionar o diretório src ao sistema de caminhos do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from src.etl_process.extract import Extract
from src.etl_process.transform import Transform
from src.etl_process.load import Load



st.title("Projeto ETL")

st.header("Carregar Dados")

file_type = st.selectbox("Escolha o tipo de arquivo:", ["CSV", "JSON"])

extractor = Extract()

if file_type == "CSV":
    csv_file = st.file_uploader("Carregar arquivo CSV", type=["csv"])
    if csv_file:
        df = extractor.one_input_csv(csv_file)
        st.write(df)

elif file_type == "JSON":
    json_file = st.file_uploader("Carregar arquivo JSON", type=["json"])
    if json_file:
        df = extractor.one_input_json(json_file)
        st.write(df)
