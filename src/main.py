import duckdb 
import os
from etl_json import DuckdbETL
from create_faker_data import Gerador


# os.chdir('..')


# a = "json1.json"
# input_one_json = duckdb.read_json(f"data/json/{a}")
# duckdb.sql("select * from input_one_json").show()

# df_one_json = DuckdbETL()
# df_one_json.carrega_one_json("json1")
# df_one_json.select_table()

# df_all_jsons = DuckdbETL()
# df_all_jsons.carrega_all_jsons()
#df_all_jsons.select_table()

arquivo = Gerador()
arquivo.generator_of_registers(10000)
arquivo.output_csv("teste1")

# etl = DuckdbETL()
# etl.json_input_one("tst")
# query = "SELECT * FROM VW WHERE Salary > 7000 "
# #etl.testando(query)
# result_df = etl.filter_select(query)
#print(result_df)
#df_all_jsons.filter_select("select * from ")