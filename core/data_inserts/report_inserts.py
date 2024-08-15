def create_report_tables(conn):
    conn.sql('''
        CREATE TABLE reports (
            id INTEGER PRIMARY KEY,
            application_id INTEGER,
            report_date DATE,
            report_text VARCHAR,
            FOREIGN KEY (application_id) REFERENCES applications(id)
        )
    ''')