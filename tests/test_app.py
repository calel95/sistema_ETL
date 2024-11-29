import sys
import os
import pandas as pd
import streamlit as st

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.backend.extract import Extract
from src.backend.transform import Transform
#from backend.load import Load

st.title("Projeto ETL")

if 'original_df' not in st.session_state:
    st.session_state['original_df'] = None
if 'transformed_df' not in st.session_state:
    st.session_state['transformed_df'] = None

st.header("Carregar Dados")

file_type = st.selectbox("Escolha o tipo de arquivo:", ["CSV", "JSON"])

extractor = Extract()

if file_type == "CSV":
    csv_file = st.file_uploader("Carregar arquivo CSV", type=["csv"])
    if csv_file:
        df = extractor.web_one_input_csv(csv_file)
        st.session_state['original_df'] = df
        st.session_state['transformed_df'] = df
        st.write("DataFrame Original:")
        st.write(df)
        #st.table(st.session_state['df'])

elif file_type == "JSON":
    json_file = st.file_uploader("Carregar arquivo JSON", type=["json"])
    if json_file:
        df = extractor.web_one_input_json(json_file)
        st.session_state['original_df'] = df
        st.session_state['transformed_df'] = df
        st.write("DataFrame Original:")
        st.write(df)

st.header("Transformar Dados")

if st.session_state['original_df'] is not None:
    # Usar o DataFrame atual transformado
    df = st.session_state['transformed_df']

    if st.button("Remover Duplicatas"):    
        st.session_state['transformed_df'] = Transform.remove_data_duplicates(st.session_state['transformed_df'])
        st.success(f"dados duplicados removidos com sucesso!")

    columns_to_check = st.text_input("Colunas para deletar nulos (separadas por vírgula):")
    if st.button("Remover Nulos"):
        if columns_to_check:
            columns_list = columns_to_check.split(",") 
            st.session_state['transformed_df'] = Transform.remove_data_nulls(st.session_state['transformed_df'], columns_list)
            st.success(f"dados nulos removidos com sucesso!")
        else:
            st.warning("Por favor, insira colunas válidas.")

    query = st.text_area("Consulta SQL para filtrar dados:")
    if st.button("Filtrar query"):
        if query:
            st.session_state['transformed_df'] = Transform.filter_select(st.session_state['transformed_df'], query)
            st.success("Filtro aplicado com sucesso!")
        else:
            st.warning("Por favor, insira uma consulta SQL válida.")

    if st.button("Reverter para o DataFrame Original"):
        st.session_state['transformed_df'] = st.session_state['original_df'].copy()
        st.success("DataFrame revertido para o estado original!")

    if st.button("Remove duplicado e dados null"):  
        transformed_df_temp = Transform.remove_data_duplicates(st.session_state['transformed_df'])
        columns_list = columns_to_check.split(",") 
        transformed_df_temp = Transform.remove_data_nulls(transformed_df_temp, columns_list)
        st.session_state['transformed_df'] = transformed_df_temp

    st.write("DataFrame Transformado:")
    st.write(st.session_state['transformed_df'])