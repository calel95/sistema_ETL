import sys
import os
import pandas as pd
import streamlit as st

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.backend.extract import Extract
from src.backend.transform import Transform
from src.backend.load import Load

st.title("Projeto ETL")

if "df" not in st.session_state:
    st.session_state.df = None
if "df_origem" not in st.session_state:
    st.session_state.df_origem = None

st.header("Carregar Dados")

file_type = st.selectbox("Escolha o tipo de arquivo:", ["CSV", "JSON"])

extractor = Extract()

if file_type == "CSV":
    csv_file = st.file_uploader("Carregar arquivo CSV", type=["csv"])
    if csv_file:
        df = extractor.web_one_input_csv(csv_file)
        st.session_state.df_origem = df
        st.write("DataFrame Original:")
        st.write(df)

elif file_type == "JSON":
    json_file = st.file_uploader("Carregar arquivo JSON", type=["json"])
    if json_file:
        df = extractor.web_one_input_json(json_file)
        st.session_state.df_origem = df
        st.write("DataFrame Original:")
        st.write(df)

st.header("Transformar Dados")

if st.button("defini DF"):  
    st.session_state.df = st.session_state.df_origem


if st.button("Remover Duplicatas"):    
    st.session_state.df = Transform.remove_data_duplicates(st.session_state.df)
    st.success(f"dados duplicados removidos com sucesso!")

columns_to_check = st.text_input("Colunas para deletar nulos (separadas por vírgula):")
if st.button("Remover Nulos"):
    if columns_to_check:
        columns_list = columns_to_check.split(",") 
        st.session_state.df = Transform.remove_data_nulls(st.session_state.df, columns_list)
        st.success(f"dados nulos removidos com sucesso!")
    else:
        st.warning("Por favor, insira colunas válidas.")

query = st.text_area("Consulta SQL para filtrar dados:")
if st.button("Filtrar query"):
    if query:
        st.session_state.df = Transform.filter_select(st.session_state.df, query)
        st.success("Filtro aplicado com sucesso!")
    else:
        st.warning("Por favor, insira uma consulta SQL válida.")


if st.button("Reverter para Dataframe original"):    
    st.session_state.df = st.session_state.df_origem
    st.success(f"Dataframe Original!")

loader = Load()

st.header("Salvar Dados")

# Adicione um campo para o usuário digitar o caminho de destino
save_path = st.text_input("Caminho para salvar o arquivo Parquet:")

if st.button("Salvar Parquet"):
        if save_path:
            success = loader.save_teste(st.session_state.df, save_path)
            if success:
                st.success(f"Arquivo Parquet salvo em {save_path}")
            else:
                st.error("Falha ao salvar o arquivo")

st.write("DataFrame Transformado:")
st.write(st.session_state.df)