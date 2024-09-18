import duckdb 
import os
from etl_json import DuckdbETL
from create_faker_data import Gerador
import re


a = Gerador()
a.generator_of_registers(1000)
a.output_csv("testando_csv")
a.output_json("testando_json")

# etl = DuckdbETL()
# etl.json_input_one("tst")
# query = "SELECT * FROM VW WHERE Salary > 7000 "
# #etl.testando(query)
# result_df = etl.filter_select(query)
#print(result_df)
#df_all_jsons.filter_select("select * from ")