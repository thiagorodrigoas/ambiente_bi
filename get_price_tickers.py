from tinydb import TinyDB, Query
import pandas as pd
import yfinance as yf
from pathlib import Path
from desc_produtos import df_produtos
# Definindo a variável global para o banco de dados e os dados mensais

global_db = None


def init_db():
    global global_db
    dir_path = Path("database")
    db_file_path = dir_path / "database_price.json"
    
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)

    global_db = TinyDB(db_file_path,indent=2)
    global_db.truncate()

def store_in_db(data):
    init_db()
    
    global global_db

    if global_db is None:
        raise ValueError("O banco de dados ainda não foi inicializado. Chame init_db() primeiro.")

    global_db.insert_multiple(data)

def fetch_monthly_data(list_tickers, data_consulta):
    # Define o período de data_consulta até hoje
    end_date = pd.Timestamp.today()
    daily_data = yf.download(list_tickers, start=data_consulta, end=end_date)
    
    # Converte para frequência mensal
    daily_data = daily_data.resample('MS').mean()
    daily_data = daily_data['Close']
    daily_data = daily_data.apply(lambda row: row.fillna(row.mean()), axis=1)
    daily_data = daily_data.round(2)
    monthly_data_close =  daily_data.reset_index() 
    monthly_data_close['Date'] = monthly_data_close['Date'].dt.strftime('%Y-%m-%d')

    # Armazenando no banco de dados tinydb
    store_in_db(monthly_data_close.to_dict(orient='records'))
    return global_db
    

# # Inicialize o banco de dados antes de chamar a função fetch_monthly_data
# init_db()

# # Testando
# # Supondo que row e data_consulta são fornecidos, chame fetch_monthly_data
fetch_monthly_data(list(df_produtos['des_ticket_price']), '2018-01-01')