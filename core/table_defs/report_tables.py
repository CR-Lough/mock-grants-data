def create_report_tables(conn):
    conn.sql('''
        CREATE TABLE reports (
            report_id INTEGER PRIMARY KEY,
            application_id INTEGER REFERENCES applications(application_id),
            report_date DATE,
            report_summary TEXT
        )
    ''')
    conn.sql('''
        CREATE TABLE dagp_report_details (
            report_id INTEGER PRIMARY KEY REFERENCES reports(report_id),
            damages_assessed TEXT,
            compensation_amount DECIMAL,
            corrective_measures TEXT,
            report_status VARCHAR
        )
    ''')
    conn.sql('''
        CREATE TABLE fplagp_report_details (
            report_id INTEGER PRIMARY KEY REFERENCES reports(report_id),
            land_assessment TEXT,
            zoning_compliance VARCHAR,
            environmental_impact TEXT,
            future_recommendations TEXT,
            report_status VARCHAR
        )
    ''')
    conn.sql('''
        CREATE TABLE rgp_report_details (
            report_id INTEGER PRIMARY KEY REFERENCES reports(report_id),
            outreach_success TEXT,
            technical_assistance_evaluation TEXT,
            cost_share_effectiveness TEXT,
            maintenance_review TEXT,
            permanent_protection_review TEXT,
            report_status VARCHAR
        )
    ''')
    conn.sql('''
        CREATE TABLE rppgp_report_details (
            report_id INTEGER PRIMARY KEY REFERENCES reports(report_id),
            cultivation_assessment TEXT,
            community_engagement_review TEXT,
            budget_justification_review TEXT,
            partnerships_review TEXT,
            report_status VARCHAR
        )
    ''')

