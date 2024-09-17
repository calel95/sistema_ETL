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
        #return self.df
    
    def json_all_input(self):
        self.df = duckdb.read_json("data/json/*.json")
        return self.df
    
    def select_table(self):
        return self.df.show()
    
    def filter_select(self,query):
        """Considerar FROM na tabela vw"""
        duckdb.register('VW', self.df)
        result = duckdb.query(query).df()
        print(duckdb.df(result))
        return duckdb.df(result)
    

