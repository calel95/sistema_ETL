import duckdb 
import os
import pandas as pd

class Extract:
    def __init__(self) -> None:
        #self.file_path = file_path
        self.df = None
        os.chdir('..')

    def one_input_json(self, arquive_name: str):
        '''apenas o nome do arquivo json'''
        #os.chdir('..')
        file_path = f"data/json/{arquive_name}.json"
        self.df = duckdb.read_json(f"data/json/{arquive_name}.json")
        size = os.path.getsize(file_path)
        print(f"Size do arquivo '{arquive_name}': {size} bytes")
        return self.df
    
    def one_input_csv(self, arquive_name: str):
        '''apenas o nome do arquivo csv'''
        #os.chdir('..')
        file_path = f"data/csv/{arquive_name}.csv"
        self.df = duckdb.read_csv(f"data/csv/{arquive_name}.csv")
        size = os.path.getsize(file_path)
        print(f"Size do arquivo '{arquive_name}': {size} bytes")
        return self.df
    
    def all_input_csv(self):
        self.df = duckdb.read_csv("data/csv/*.csv")
        return self.df
    
    def all_input_json(self):
        self.df = duckdb.read_json("data/json/*.json")
        return self.df