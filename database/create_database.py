import pandas as pd
from sqlalchemy import create_engine, text
from src.log_config import logger

xlsx_file = 'a_backup_saft_file.xlsx'
sheet_name = 'Sheet1'  

# Change 'user', 'password', 'host', 'port' e 'dbname' for the real data.
user = 'user'        
password = 'password123'
host = '192.168.1.99'
port = '5432'
db_name = 'bd_saftonline'
table_name = 't_saftonline'

try:
    df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
    logger.info('Excel file read successfully.')
except Exception as e:
    logger.error('Error on read excel file:', e)
    exit(1)

try:
    connect_str = (
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'
    )
    engine = create_engine(connect_str)

    with engine.connect() as conn:
        result = conn.execute(text('SELECT 1'))
        logger.info('Return of the connection test:', result.fetchone())

    logger.info('PostgreSQL connection estabilishd successfully!')
except Exception as e:
    logger.error('Error to connect with PostgreSQL:', e)
    exit(1)

try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    logger.info(f"Table '{table_name}' created and data inserted!")
except Exception as e:
    logger.error('Error to create table or insert data:', e)
