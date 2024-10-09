import duckdb 
import os
import pandas as pd
from openpyxl.workbook import Workbook


class DuckdbETL:
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
    
    def teste_all_input_json(self):
        con = duckdb.connect()
        self.df = con.execute("SELECT * FROM read_json_auto('data/json/*.json')").df()
        return self.df
    
    def all_input_json(self):
        self.df = duckdb.read_json("data/json/*.json")
        return self.df
    
    def select_table(self):
        print(self.df)
    
    def filter_select(self,query,save_df = False):
        """Considerar o nome da tabela de VW.
            Se deseja salvar o resultado no DF setar o parametro save_df como True"""
        duckdb.register('VW', self.df)
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            return self.df
    
    def save_parquet_table(self,file_name: str):
        output_path = f"data/parquet/{file_name}.parquet"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_parquet(output_path)
        print(f"DataFrame salvo como Parquet em: {output_path}")

    def save_csv_table(self,file_name: str):
        output_path = f"data/excel/{file_name}.xlsx"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path)
        print(f"DataFrame salvo como csv em: {output_path}")

    def remove_dados_duplicados(self):
        duckdb.register('VW', self.df)
        query = "select distinct * from VW"
        result = duckdb.query(query).df()
        self.df = duckdb.df(result)
        return self.df