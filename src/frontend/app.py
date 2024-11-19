import sys
import os
import pandas as pd
import streamlit as st
from backend.extract import Extract
from backend.transform import Transform
from backend.load import Load

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.title("Projeto ETL")

if "df" not in st.session_state:
    df = Transform(st.session_state["df"])

st.header("Carregar Dados")

file_type = st.selectbox("Escolha o tipo de arquivo:", ["CSV", "JSON"])

extractor = Extract()

if file_type == "CSV":
    csv_file = st.file_uploader("Carregar arquivo CSV", type=["csv"])
    if csv_file:
        df = extractor.web_one_input_csv(csv_file)
        st.write(df)

elif file_type == "JSON":
    json_file = st.file_uploader("Carregar arquivo JSON", type=["json"])
    if json_file:
        df = extractor.web_one_input_json(json_file)
        st.write(df)

st.header("Transformar Dados")

if 'df' in locals():  # Verifica se o DataFrame foi carregado
    transform = Transform(df)

    if st.button("Remover Duplicatas"):
        #transform = transform.remove_data_duplicates()
        st.write(transform.remove_data_duplicates())
        st.success(f"dados duplicados removidos com sucesso!")

    columns_to_check = st.text_input("Colunas para deletar nulos (separadas por vírgula):")
    if st.button("Remover Nulos"):
        if columns_to_check:
            columns_list = columns_to_check.split(",")
            #transform = transform.remove_data_nulls(columns_list)
            transform = st.write(transform.remove_data_nulls(columns_list))
            st.success(f"dados nulos removidos com sucesso!")
        else:
            st.write("DEU RUIM")

    query = st.text_area("Consulta SQL para filtrar dados:")
    if st.button("Filtrar query"):
        if query:
            #transform = Transform(transform)
            transform = transform.filter_select(query,True)
            st.write(transform)
            st.success("Filtro aplicado com sucesso!")
        else:
            st.warning("Por favor, insira uma consulta SQL válida.")

    
        