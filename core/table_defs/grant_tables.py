def create_grant_tables(conn):
    conn.sql('''
        CREATE TABLE grants (
            grant_id INTEGER PRIMARY KEY,
            name VARCHAR
        )
    ''')