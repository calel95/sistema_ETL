import duckdb 
import pandas as pd

class Transform:
    # def __init__(self,df=None):
    #     #self.file_path = file_path
    #     self.df = df

    @staticmethod
    def select_table(df):
        """Exibe o DataFrame atual."""
        print(df)
    
    @staticmethod
    def filter_select(df,query):
        """Filtra o DataFrame com uma consulta SQL, considerar o nome da tabela como VW.       
        Args:
            query (str): A consulta SQL.
            save_df (bool): Se True, salva o resultado no DataFrame original.       
        Returns:
            Retorna o dataframe original antes da edicao ou depois da edicao dependendo do parametro save_df.
        """
        duckdb.register('VW', df)
        result = duckdb.query(query).df()
        df = duckdb.df(result)
        return df

    @staticmethod    
    def remove_data_duplicates(df):
        """Remove todos os registros duplicados."""
        duckdb.register('VW', df)
        query = "select distinct * from VW"
        result = duckdb.query(query).df()
        df = duckdb.df(result)
        return df
    
    @staticmethod
    def remove_data_nulls(df,columns: list):
        """Remove todos os registros nulos de uma ou varias colunas.       
        Args:
            save_df (bool): Se True, salva o resultado no DataFrame original. 
            columns (list): Rece uma lista das colunas que devem ser verificadas se existe registros null      
        Returns:
            Retorna o dataframe original antes da edicao ou depois da edicao dependendo do parametro save_df.
        """
        duckdb.register('VW', df)
        if not isinstance(columns, list):
            columns = [columns]
        
        where_clause = " AND ".join([f"{column} IS NOT NULL" for column in columns])
        where_clause_drop_registers = " OR ".join([f"{column} IS NULL" for column in columns])
        
        query = f"SELECT * FROM VW WHERE {where_clause}"
        query_drop_registers = f"SELECT * FROM VW WHERE {where_clause_drop_registers}"

        print("=========================REGISTROS DROPADOS COM REGISTROS NULLS NOS CAMPOS ESPECIFICADOS=========================")
        result2 = duckdb.query(query_drop_registers).df()
        result = duckdb.query(query).df()
        print(duckdb.df(result2))
        df = duckdb.df(result)
        return df
    
    @staticmethod
    def last_position_data(self,column_order_by,column_partition_by,save_df = False, column_filter = '1=1'):
        duckdb.register('VW', self.df)
        query = f"SELECT * EXCLUDE(rn) from (select *, ROW_NUMBER() OVER(PARTITION BY {column_partition_by} order by {column_order_by} desc)as rn from VW) where rn = 1 AND {column_filter}"
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            print(duckdb.df(result))
            return self.df
    
    @staticmethod
    def first_position_data(self,column_order_by,column_partition_by,save_df = False,column_filter = '1=1'):
        duckdb.register('VW', self.df)
        query = f"SELECT * EXCLUDE(rn) from (select *, ROW_NUMBER() OVER(PARTITION BY {column_partition_by} order by {column_order_by} asc)as rn from VW) where rn = 1 AND {column_filter}"
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            print(duckdb.df(result))
            return self.df
        
    @staticmethod
    def apply_transformations(self, options):
        if 'remove_duplicates' in options:
            self.df = self.remove_data_duplicates(self.df)
        if 'remove_nulls' in options:
            self.df = self.remove_data_nulls(self.df, options['null_columns'])
        if 'last_position' in options:
            self.df = self.last_position_data(self.df, options['order_by'], options['partition_by'])
        # Adicione mais transformações conforme necessário
        return self.df