class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:asbsistemas@localhost:5432/pyalmacen"
    #SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://DESKTOP-AQ2ALR2/pyalmacen2?driver=ODBC Driver 17 for SQL Server"
    #SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://WIN-D776HKG3N67/pyalmacen?driver=ODBC Driver 17 for SQL Server"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://asbsistemas:asbsistemas@192.168.0.24:3306/pyalmacen"

class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'




'''
#SQlite
sqlite:///database.db
#MySQL
mysql+pymysql://user:password@ip:port/db_name
#Postgres
postgresql+psycopg2://user:password@ip:port/db_name
#MSSQL
mssql+pyodbc://server_name/database_name?driver=ODBC Driver 17 for SQL Server
#Oracle
oracle+cx_oracle://user:password@ip:port/db_name
'''

