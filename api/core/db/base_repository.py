from mysql import connector 
from mysql.connector import MySQLConnection
from mysql.connector.connection import CursorBase
from mysql.connector import errorcode as err_codes


class BaseRepository:
    def __init__(self, config):
        
        self.config = config

    def _init_connection(self) -> MySQLConnection:
        try:
            return connector.connect(**self.config)
        except connector.Error as err:
            if err.errno == err_codes.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == err_codes.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            raise err

    def create_cursor(self,connection:MySQLConnection, **config) -> CursorBase:
        
        return connection.cursor(**config)