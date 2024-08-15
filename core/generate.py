import duckdb
from core.table_defs.application_tables import create_application_tables
from core.table_defs.grant_tables import create_grant_tables
from core.table_defs.report_tables import create_report_tables
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
    
    # Create the various tables necessary
    create_grant_tables(conn)
    create_application_tables(conn)
    create_report_tables(conn)



# Generate grants, applications, and reports mock data
    conn.sql(
    '''
        INSERT INTO grants VALUES
            (1, 'Conservation Reserve Enhancement Program (CREP)'),
            (2, 'Disaster Assistance Program (DAP)'),
            (3, 'Farmland Protection and Land Access (FPLA) Program'),
            (4, 'Forest Health and Community Wildfire Resiliency (CWR)'),
            (5, 'Irrigation Efficiencies Grant Program (IEGP)'),
            (6, 'Natural Resource Investments (NRI)'),
            (7, 'Riparian Grant Program (RGP)'),
            (8, 'Riparian Plant Propagation Program (RPPP)'),
            (9, 'Shellfish Program'),
            (10, 'Sustainable Farms & Fields'),
            (11, 'Sustainable Farms & Fields: Climate-Smart Livestock');
    '''
    )

    conn.table("grants").show()
