import duckdb 
import os
import pandas as pd
#from openpyxl.workbook import Workbook


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
            print(duckdb.df(result))
            return self.df
            
    
    def save_parquet_table(self,file_name: str):
        output_path = f"data/parquet/{file_name}.parquet"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_parquet(output_path)
        print(f"DataFrame salvo como Parquet em: {output_path}")

    def save_xlsx_table(self,file_name: str):
        output_path = f"data/excel/{file_name}.xlsx"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path)
        print(f"DataFrame salvo como xlsx em: {output_path}")

    def remove_data_duplicates(self):
        duckdb.register('VW', self.df)
        query = "select distinct * from VW"
        result = duckdb.query(query).df()
        self.df = duckdb.df(result)
        return self.df
    
    def remove_data_nulls(self):
        pass
    
    def last_position_data(self,column_order_by,column_partition_by,save_df = False):
        duckdb.register('VW', self.df)
        query = f"SELECT * EXCLUDE(rn) from (select *, ROW_NUMBER() OVER(PARTITION BY {column_partition_by} order by {column_order_by} desc)as rn from VW) where rn = 1 and nome = 'Michael Johnson'"
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            print(duckdb.df(result))
            return self.df
    
    def first_position_data(self,column_order_by,column_partition_by,save_df = False):
        duckdb.register('VW', self.df)
        query = f"SELECT * EXCLUDE(rn) from (select *, ROW_NUMBER() OVER(PARTITION BY {column_partition_by} order by {column_order_by} asc)as rn from VW) where rn = 1 and nome = 'Michael Johnson'"
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            print(duckdb.df(result))
            return self.df

    
    # def read_parquet(self):
    #     self.df = duckdb.connect()
    #     self.df.execute("CREATE VIEW df as select * from read_parquet('/home/casa/Python/sistema_ETL/data/parquet/last_position.parquet')")
    #     self.df = self.df.execute("SELECT id,nome,salario,created_at from (select *, ROW_NUMBER() OVER(PARTITION BY nome order by created_at desc)as rn from df) where rn = 1 and nome = 'Michael Johnson'").df()
    #     #print(self.df.execute("SELECT * from df where nome = 'Michael Johnson'").df())
    #     print(duckdb.df(self.df))
    #     return self.df