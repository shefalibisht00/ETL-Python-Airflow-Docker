import os


DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail_db',
            'DB_USER': 'root',
            'DB_PASS': 'root'
            # 'DB_USER': os.environ.get('SOURCE_DB_USER'),
            # 'DB_PASS': os.environ.get('SOURCE_DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail_db',
            'DB_USER': 'postgres',
            'DB_PASS': 'postgres'
            # 'DB_USER': os.environ.get('TARGET_DB_USER'),
            # 'DB_PASS': os.environ.get('TARGET_DB_PASS')
        }
    }
}

# set DB_NAME=retail_db
# set SOURCE_DB_USER=root
# set SOURCE_DB_PASS=root