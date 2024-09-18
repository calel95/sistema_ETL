import duckdb 
import os
from etl_json import DuckdbETL
from create_faker_data import Gerador
import re


a = Gerador()
a.generator_of_registers(5)
#a.output_json_overwrite("testando_json")
a.output_json_append("testando_json")

# etl = DuckdbETL()
# etl.json_input_one("tst")
# query = "SELECT * FROM VW WHERE Salary > 7000 "
# #etl.testando(query)
# result_df = etl.filter_select(query)
#print(result_df)
#df_all_jsons.filter_select("select * from ")