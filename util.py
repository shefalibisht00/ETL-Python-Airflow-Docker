import pandas as pd 
import os
from mysql import connector as mc
from mysql.connector import errorcode as ec
from config import DB_DETAILS
import psycopg2


def load_db_details(env):
    return DB_DETAILS[env]

def get_mySQL_conn(db_host,db_name,db_user,db_pass):
    connection = None
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                database=db_name
                                )
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid creds")
        else:
            print(error)
    return connection

def get_postSQL_conn(db_host,db_name,db_user,db_pass):
    #  get_connection(db_type=TARGET_DB['DB_TYPE'], db_host=TARGET_DB['DB_HOST'],db_name=TARGET_DB['DB_NAME'],db_user=TARGET_DB['DB_USER'],db_pass=TARGET_DB['DB_PASS'])
    connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)
    return connection


# Wrapper to abstract type of db
def get_connection(db_type, db_host,db_name,db_user,db_pass):
    connection = None
    if db_type=='mysql':
        connection = get_mySQL_conn(db_host,db_name,db_user,db_pass)
    elif db_type=='postgres':
        connection = get_postSQL_conn(db_host,db_name,db_user,db_pass)
    return connection


def get_tables_to_load(path):
    df = pd.read_csv(path, sep=":")
    return df.query("to_be_loaded=='yes' ")
