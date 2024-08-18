def create_application_tables(conn):
    conn.sql('''
            CREATE TABLE applications (
                application_id INTEGER PRIMARY KEY,
                grant_id INTEGER REFERENCES grants(grant_id),
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
                application_preparer VARCHAR,
                status VARCHAR
            )
        ''')
    conn.sql('''
        CREATE TABLE dagp_application_details (
            application_id INTEGER PRIMARY KEY REFERENCES applications(application_id),
            farm_ranch_name VARCHAR,
            property_tax_id VARCHAR,
            latitude_longitude VARCHAR,
            operation_type VARCHAR,
            property_owners TEXT,
            farm_type TEXT,
            acres_impacted DECIMAL,
            damage_description TEXT,
            fund_usage TEXT,
            expense_documentation TEXT,
            proof_of_damage TEXT,
            proof_of_payment TEXT,
            leased_property_letter TEXT,
            is_limited_resource BOOLEAN,
            is_socially_disadvantaged BOOLEAN
        )
    ''')
    conn.sql('''
        CREATE TABLE fplagp_application_details (
            application_id INTEGER PRIMARY KEY REFERENCES applications(application_id),
            property_tax_parcel_ids VARCHAR,
            property_zoning VARCHAR,
            project_description TEXT,
            site_viability_description TEXT,
            site_infrastructure_description TEXT,
            threat_of_conversion TEXT,
            project_timeline TEXT,
            match_funding_source VARCHAR,
            match_funding_status VARCHAR,
            future_farmer_identified BOOLEAN,
            future_farmer_characteristics TEXT,
            natural_resource_investment_opportunity TEXT,
            eligibility_conservation_easements BOOLEAN,
            secured_loan_through_farmPAI BOOLEAN
        )
    ''')
    conn.sql('''
        CREATE TABLE rgp_application_details (
            application_id INTEGER PRIMARY KEY REFERENCES applications(application_id),
            cca_requirements_completed BOOLEAN,
            project_types_requested TEXT,
            riparian_outreach_funds_requested DECIMAL,
            riparian_outreach_activities TEXT,
            technical_assistance_funds_requested DECIMAL,
            technical_assistance_activities TEXT,
            landowner_cost_share_funds_requested DECIMAL,
            landowner_cost_share_activities TEXT,
            district_implemented_funds_requested DECIMAL,
            district_implemented_activities TEXT,
            maintenance_funds_requested DECIMAL,
            maintenance_activities TEXT,
            permanent_protection_funds_requested DECIMAL,
            permanent_protection_activities TEXT,
            prioritized_projects TEXT,
            water_quality_impairment BOOLEAN,
            nature_of_impairment TEXT,
            sti_plan BOOLEAN,
            sti_plan_intersection TEXT,
            adjacent_project BOOLEAN,
            adjacent_project_description TEXT,
            leverages_other_resources BOOLEAN,
            resource_leverage_description TEXT,
            continuous_project BOOLEAN,
            environmental_justice BOOLEAN,
            environmental_justice_description TEXT,
            tribal_notification_letter TEXT,
            cpds_acknowledgment BOOLEAN,
            voucher_acknowledgment BOOLEAN
        )
    ''')
    conn.sql('''
        CREATE TABLE rppgp_application_details (
            application_id INTEGER PRIMARY KEY REFERENCES applications(application_id),
            funding_category TEXT,
            cultivation_experience TEXT,
            partnerships BOOLEAN,
            community_engagement TEXT,
            budget_justification TEXT,
            additional_budget_documents BOOLEAN
        )
    ''')