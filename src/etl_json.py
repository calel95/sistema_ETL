import duckdb 
import os
import pandas as pd

class DuckdbETL:
    def __init__(self) -> None:
        #self.file_path = file_path
        self.df = None
        os.chdir('..')
    
    def carrega_one_json(self, arquive_name):
        '''apenas o nome do arquivo json'''
        self.df = duckdb.read_json(f"data/json/{arquive_name}.json")
        return self.df
    
    def carrega_all_jsons(self):
        self.df = duckdb.read_json("data/json/*.json")
        return self.df
    
    def select_table(self):
        return self.df.show()
    
    def filter_select(self,query):
        #duckdb.from_df(self.df).create('temp_table')
        duckdb.register('temp_table', self.df)
        result = duckdb.query(query).fetchdf()
        #duckdb.query(query).fetchdf()
        return result