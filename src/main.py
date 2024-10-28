import duckdb 
import os
from etl import DuckdbETL
from create_faker_data import Gerador
import pandas as pd
import glob


a = Gerador()
a.definir_tipo_campo()
a.generator_teste(10)
#a.output_csv_ovwewrite("last_position")


a.output_json_overwrite("teste_generator")

#etl = DuckdbETL()
#etl.read_parquet()
#etl.one_input_csv("last_position")
#etl.last_position_data("created_at","nome")
# # etl.all_input_json()
# # #etl.teste_all_input_json()
#query = f"SELECT count(*), nome FROM VW group by nome having count(*)>1 "
# # #etl.testando(query)
#etl.filter_select(query)
# #etl.remove_dados_duplicados()
#etl.select_table()
# #print(result_df)
#etl.save_parquet_table("last_position")
