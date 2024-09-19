import duckdb 
import os
from etl_json import DuckdbETL
from create_faker_data import Gerador


a = Gerador()
a.generator_of_registers_list(5)
a.output_csv_ovwewrite("testando_json")
a.output_csv_append("testando_json")

# etl = DuckdbETL()
# etl.json_input_one("arquivo_teste1")
# query = "SELECT * FROM VW WHERE salario > 7000 "
# #etl.testando(query)
# etl.select_table()
# result_df = etl.filter_select(query)
# etl.select_table()
# print(result_df)
# etl.save_parquet_table("teste")
