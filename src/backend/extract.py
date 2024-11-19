import duckdb 
import os
import pandas as pd

class Extract:
    def __init__(self) -> None:
        #self.file_path = file_path
        self.df = None
        #os.chdir('..')

    # def one_input_json(self, arquive_name: str):
    #     '''apenas o nome do arquivo json'''
    #     #os.chdir('..')
    #     file_path = f"data/json/{arquive_name}.json"
    #     self.df = duckdb.read_json(f"data/json/{arquive_name}.json")
    #     size = os.path.getsize(file_path)
    #     print(f"Size do arquivo '{arquive_name}': {size} bytes")
    #     return self.df
    
    # def one_input_csv(self, arquive_name: str):
    #     '''apenas o nome do arquivo csv'''
    #     #os.chdir('..')
    #     #file_path = f"data/csv/{arquive_name}.csv"
    #     file_path = f"data/csv/{arquive_name}.csv"
    #     self.df = duckdb.read_csv(f"data/csv/{arquive_name}.csv")
    #     size = os.path.getsize(file_path)
    #     print(f"Size do arquivo '{arquive_name}': {size} bytes")
    #     return self.df
    
    # def all_input_csv(self):
    #     self.df = duckdb.read_csv("data/csv/*.csv")
    #     return self.df
    
    # def all_input_json(self):
    #     self.df = duckdb.read_json("data/json/*.json")
    #     return self.df


    def one_input_csv(self, file):
        '''Carrega dados de um arquivo CSV em memória'''
        # self.df = pd.read_csv(file)  # Usa pandas para ler diretamente do objeto de arquivo
        # size = file.size  # Obtem o tamanho do arquivo
        # print(f"Size do arquivo: {size} bytes")
        # return self.df
        self.df = duckdb.read_csv(file)
        return self.df


    def one_input_json(self, file):
        '''Carrega dados de um arquivo JSON em memória'''
        self.df = duckdb.read_csv(file)  # Usa pandas para ler diretamente do objeto de arquivo
        return self.df