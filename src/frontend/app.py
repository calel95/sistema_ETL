import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from backend.extract import Extract
#from etl_process.transform import Transform
#from etl_process.load import Load


__all__ = ["Extract"]

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

# st.header("Transformar Dados")

# if 'df' in locals():  # Verifica se o DataFrame foi carregado
#     transform = Transform(df)

#     if st.button("Remover Duplicatas"):
#         df = transform.remove_data_duplicates()
#         st.write(df)

#     if st.button("Remover Nulos"):
#         columns_to_check = st.text_input("Colunas para verificar nulos (separadas por vírgula):")
#         if columns_to_check:
#             columns_list = [col.strip() for col in columns_to_check.split(",")]
#             df = transform.remove_data_nulls(columns_list)
#             st.write(df)

#     query = st.text_area("Consulta SQL para filtrar dados:")
#     if st.button("Filtrar Dados"):
#         df = transform.filter_select(query)
#         st.write(df)