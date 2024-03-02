import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '192.168.80.4',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('MYSQL_DB_USER'),
            'DB_PASS': os.environ.get('MYSQL_DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '192.168.80.3',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('POSTGRES_DB_USER'),
            'DB_PASS': os.environ.get('POSTGRES_DB_PASS')
        }
    }
}