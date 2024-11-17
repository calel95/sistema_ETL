import duckdb 
import pandas as pd

class Transform:
    def __init__(self,df) -> None:
        #self.file_path = file_path
        self.df = df


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