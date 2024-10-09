import duckdb 
import os
from etl import DuckdbETL
from create_faker_data import Gerador
import pandas as pd
import glob


# a = Gerador()
# a.generator_of_registers_list(10000)
# a.output_csv_append("objetos")


# #a.output_csv_append("testando_csv")

etl = DuckdbETL()
etl.one_input_json("json1")
# etl.all_input_json()
# #etl.teste_all_input_json()
query = f"SELECT count(*), name FROM VW group by name having count(*)>1 "
# #etl.testando(query)
etl.filter_select(query,True)
#etl.remove_dados_duplicados()
etl.select_table()
# #print(result_df)
#etl.save_parquet_table("salva_distinct_name")
