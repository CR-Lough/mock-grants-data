def generate_grant_mock_data(conn):
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
    print("Grant details data inserted successfully.")