
import yaml
from sqlalchemy import create_engine

conf = yaml.load(open('./vars.yaml', 'r'))

rs_username = conf['REDSHIFT_USER']
rs_password = conf['REDSHIFT_PASSWORD']
rs_db = conf['REDSHIFT_DB']
rs_host = conf['REDSHIFT_HOST']

def get_conf():
    return conf


def get_engine():
    
    engine = create_engine(f'redshift+psycopg2://{rs_username}:{rs_password}@{rs_host}:5439/{rs_db}')
    return engine
    