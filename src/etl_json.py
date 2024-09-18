import duckdb 
import os
import pandas as pd

class DuckdbETL:
    def __init__(self) -> None:
        #self.file_path = file_path
        self.df = None
        os.chdir('..')
    


    def json_input_one(self, arquive_name: str):
        '''apenas o nome do arquivo json'''
        #os.chdir('..')
        file_path = f"data/json/{arquive_name}.json"
        self.df = duckdb.read_json(f"data/json/{arquive_name}.json")
        size = os.path.getsize(file_path)
        print(f"Size do arquivo '{arquive_name}': {size} bytes")
        return self.df
    
    def json_all_input(self):
        self.df = duckdb.read_json("data/json/*.json")
        return self.df
    
    def select_table(self):
        print(self.df)
    
    def filter_select(self,query):
        """Considerar FROM na tabela vw"""
        duckdb.register('VW', self.df)
        result = duckdb.query(query).df()
        self.df = result
        return self.df
    
    def save_parquet_table(self,file_name: str):
        output_path = f"data/parquet/{file_name}.parquet"
        self.df.to_parquet(output_path)
        print(f"DataFrame salvo como Parquet em: {output_path}")
        

