import duckdb
from table_defs.application_tables import create_application_tables
from table_defs.grant_tables import create_grant_tables
from table_defs.report_tables import create_report_tables
from data_inserts.grant_inserts import grant_table_inserts

# Connect to a new DuckDB database
conn = duckdb.connect('grants.duckdb')

# Open connection and create `grants`, `applications`, and `reports` tables
tables_list = [
        'grants',
        'applications',
        'dagp_application_details',
        'fplagp_application_details',
        'rgp_application_details',
        'rppgp_application_details',
        'reports',
        'dagp_report_details',
        'fplagp_report_details',
        'rgp_report_details',
        'rppgp_report_details'
    ]
with duckdb.connect('grants.duckdb') as conn:
    # Make sure we start from a blank slate
    for table in tables_list:
        conn.sql(f"DROP TABLE IF EXISTS {table}")
    
    # Create the necessary tables
    create_grant_tables(conn)
    create_application_tables(conn)
    # create_report_tables(conn)

    # Generate grants, applications, and reports mock data
    grant_table_inserts(conn)


    conn.table("grants").show()
