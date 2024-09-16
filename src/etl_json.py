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
        #os.chdir('..')
        file_path = f"data/json/{arquive_name}.json"
        self.df = duckdb.read_json(f"data/json/{arquive_name}.json")
        tamanho = os.path.getsize(file_path)
        print(f"Tamanho do arquivo '{arquive_name}': {tamanho} bytes")
        #return self.df
    
    def carrega_all_jsons(self):
        self.df = duckdb.read_json("data/json/*.json")
        return self.df
    
    def select_table(self):
        return self.df.show()
    
    def filter_select(self,query):
        duckdb.register('tabela', self.df)
        result = duckdb.query(query).df()
        print(duckdb.df(result))
        print(self.df)
        return duckdb.df(result)
    

    def testando(self,query):
        duckdb.register('tabela', self.df)
        resultado = duckdb.sql(query).df()
        print(resultado)
        return duckdb.df(resultado)
