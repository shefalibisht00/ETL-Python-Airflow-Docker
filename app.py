import sys
from util import get_tables_to_load, load_db_details
import mysql.connector as mc
from read_input_files import read_table
from write_output_files import load_into_db


def main():
    print(sys.argv)
    env = sys.argv[1]
    db_details = load_db_details(env)
    table_list = get_tables_to_load('table_list.txt')['table_name']
    
    print(f"Loading data for {len(table_list)} tables: [", ', '.join(table_list), "]")

    for table in table_list:
        data, column_names = read_table(db_details=db_details,table_name=table, limit=250)        
        # Load into Target PostGres
        load_into_db(db_details=db_details, table_name=table, column_list=column_names, table_data=data)


if __name__ == '__main__':
    main()
