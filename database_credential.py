import os

DATABASE_CREDENTIAL = {
    'host': os.environ.get('HOST', 'localhost'),
    'database': 'postgres',
    'user': 'postgres',
    'password': "ratestask"
}
