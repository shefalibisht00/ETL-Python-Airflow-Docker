from util import get_connection
import os

# Every table has different column name. So we build a generic fn to build a query based on column names & table. Below is Query Template
# cur.execute("INSERT INTO employees (id, name, age) VALUES (%s, %s, %s)",
#             (employee_id, employee_name, employee_age))
def build_query(table_name, column_list):
    # Ex of column_list = ('department_id', 'department_name')
    column_names = str.replace(str(column_list),"'","")
    column_names_string = tuple(map(lambda x: x.replace(x,'%s'), column_list))
    column_names_string = str.replace(str(column_names_string),"'","")

    query = f'INSERT INTO {table_name} {column_names} VALUES {column_names_string}'
    print(query)
    return query



def insert_date(connection, cursor, query, table_data, batch_size=100):
    records,ctr=[],0
    for rec in table_data:
        records.append(rec)
        if ctr%batch_size==0:
            cursor.executemany(query,records)
            connection.commit()
            records=[]
        ctr+=1
    #Below is to inserts left over records
    cursor.executemany(query,records)     
    connection.commit()     

    
def load_into_db(db_details, table_name, column_list, table_data):
   
    TARGET_DB = db_details['TARGET_DB']
    # print(table_data)
    connection = get_connection(db_type=TARGET_DB['DB_TYPE'], db_host=TARGET_DB['DB_HOST'],db_name=TARGET_DB['DB_NAME'],db_user=TARGET_DB['DB_USER'],db_pass=TARGET_DB['DB_PASS'])
    cursor = connection.cursor()

    cursor.execute(f"TRUNCATE TABLE {table_name}")
    connection.commit()

    query = build_query(table_name, column_list)

    insert_date(connection, cursor, query, table_data)
    connection.close()


