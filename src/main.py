import duckdb 
import os
from etl import DuckdbETL
from create_faker_data import Gerador
import pandas as pd
import glob


# a = Gerador()
# a.generator_of_registers_dict(10000)
# a.output_json_overwrite("json1")


# #a.output_csv_append("testando_csv")

etl = DuckdbETL()
# etl.all_input_json()
# #etl.teste_all_input_json()
# #query = "SELECT * FROM VW WHERE name like 'A%' "
# #etl.testando(query)
# etl.select_table()
# #etl.filter_select(query)
# # etl.select_table()
# #print(result_df)
# etl.save_parquet_table("json_all_1")

















# def read_all_json_files(directory: str):
#     # Usando glob para encontrar todos os arquivos JSON na pasta especificada
#     os.chdir('..')
#     all_files = glob.glob(f"{directory}/*.json")
    
#     # Lista para armazenar os DataFrames
#     df_list = []

#     # Lendo cada arquivo JSON e adicionando o DataFrame à lista
#     for file in all_files:
#         df = pd.read_json(file)
#         df_list.append(df)

#     # Concatenando todos os DataFrames em um único DataFrame
#     combined_df = pd.concat(df_list, ignore_index=True)
    
#     return combined_df

# # Exemplo de uso
# directory_path = 'data/json'  # Substitua pelo caminho da sua pasta
# df = read_all_json_files(directory_path)
# print(df.dtypes)
