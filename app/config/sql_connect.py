from sqlalchemy import create_engine
from app.config.environments import ENVIRONMENTS

save_on_db=ENVIRONMENTS['save_on_db']
db_username=ENVIRONMENTS['db_username']
db_password=ENVIRONMENTS['db_password']
db_databa_name=ENVIRONMENTS['db_databa_name']
db_host=ENVIRONMENTS['db_host']
db_port=ENVIRONMENTS['db_port']
db_engine=ENVIRONMENTS['db_engine']

engine = None

if save_on_db:
    engine = create_engine(f"{db_engine}://{db_username}:{db_password}@{db_host}:{db_port}/{db_databa_name}")