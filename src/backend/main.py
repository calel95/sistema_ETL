import duckdb 
import os
from extract import Extract
from transform import Transform
from load import Load
from create_data.create_faker_data import Gerador
import pandas as pd
import glob


a = Gerador()
a.definir_tipo_campo()
a.generator_teste(100,"Dict")
a.output_csv_ovwewrite("cc")


#a.output_csv_ovwewrite("teste_generator")

#etl = DuckdbETL()
#etl.read_parquet()
#etl.one_input_csv("teste1")
#etl.last_position_data("created_at","nome")
# # etl.all_input_json()
# # #etl.teste_all_input_json()
#query = f"SELECT * from VW where salary > 6000 "
# # #etl.testando(query)
#etl.filter_select(query)
# #etl.remove_dados_duplicados()
#etl.select_table()
# #print(result_df)
#etl.save_parquet_table("last_position")

#extract = Extract()
#df = extract.one_input_csv("arquivo_teste")
#print(type(extract))

#transform = Transform(df)
#query = "select * from VW where name = 'Katelyn Hull'"
#transform.select_table()
#transform.remove_data_nulls(['name','salary'])
#df = transform.filter_select(query,True)

#load = Load(df)
#load.save_parquet_table("teste3")