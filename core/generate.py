import duckdb

# Connect to a new DuckDB database
conn = duckdb.connect('grants.duckdb')

# Open connection and create `grants`, `applications`, and `reports` tables
tables_list = [
        'grants',
        'applications',
        'reports',
        'dagp_application_details',
        'fplagp_application_details',
        'rgp_application_details',
        'rppgp_application_details'
    ]
with duckdb.connect('grants.duckdb') as conn:
    for table in tables_list:
        conn.sql(f"DROP TABLE IF EXISTS {table}")
    conn.sql('''
        CREATE TABLE grants (
            grant_id INTEGER PRIMARY KEY,
            name VARCHAR
        )
    ''')
    conn.sql('''
        CREATE TABLE applications (
            application_id UUID PRIMARY KEY,
            grant_id UUID REFERENCES grants(grant_id),
            applicant_type VARCHAR,
            first_name VARCHAR,
            last_name VARCHAR,
            email VARCHAR,
            phone VARCHAR,
            application_date DATE,
            physical_address VARCHAR,
            physical_city VARCHAR,
            physical_state VARCHAR,
            physical_zip VARCHAR,
            mailing_address VARCHAR,
            mailing_city VARCHAR,
            mailing_state VARCHAR,
            mailing_zip VARCHAR,
            property_address VARCHAR,
            property_city VARCHAR,
            property_state VARCHAR,
            property_zip VARCHAR,
            property_county VARCHAR,
            property_acreage DECIMAL,
            amount_requested DECIMAL,
            source_of_information VARCHAR,
            has_signature BOOLEAN,
            application_preparer VARCHAR
        )
    ''')

    conn.sql('''
        CREATE TABLE reports (
            id INTEGER PRIMARY KEY,
            application_id INTEGER,
            report_date DATE,
            report_text VARCHAR,
            FOREIGN KEY (application_id) REFERENCES applications(id)
        )
    ''')

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
