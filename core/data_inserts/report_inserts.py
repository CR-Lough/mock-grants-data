import random
from faker import Faker

faker = Faker()
faker.seed_instance(42)

def generate_report_mock_data(conn):
    def get_application_ids(conn):
        query = "SELECT application_id FROM applications"
        result = conn.execute(query).fetchall()
        application_ids = [row[0] for row in result]
        return application_ids

    def insert_reports_data(conn, application_ids):
        def generate_dummy_data(application_ids):
            data = []
            for app_id in application_ids:
                report = {
                    "report_id": faker.random_int(min=1, max=10000),
                    "application_id": app_id,
                    "report_date": faker.date_this_year(),
                    "report_summary": faker.text(max_nb_chars=200)
                }
                data.append(report)
            return data

        dummy_data = generate_dummy_data(application_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        report_ids = []
        for report in dummy_data:
            report_ids.append(report['report_id'])
            insert_statements.append(f"""
                ({report['report_id']}, {report['application_id']}, '{report['report_date']}', 
                '{report['report_summary']}')
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO reports VALUES {', '.join(insert_statements)};
            """
        )
        return report_ids

    def insert_dagp_report_details_data(conn, report_ids):
        def generate_dummy_data(report_ids):
            data = []
            for rep_id in report_ids:
                report_details = {
                    "report_id": rep_id,
                    "damages_assessed": faker.text(max_nb_chars=200),
                    "compensation_amount": round(random.uniform(1000, 100000), 2),
                    "corrective_measures": faker.text(max_nb_chars=200),
                    "report_status": random.choice(["Pending", "Completed", "In Progress"])
                }
                data.append(report_details)
            return data

        dummy_data = generate_dummy_data(report_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['report_id']}, '{details['damages_assessed']}', {details['compensation_amount']}, 
                '{details['corrective_measures']}', '{details['report_status']}')
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO dagp_report_details VALUES {', '.join(insert_statements)};
            """
        )

    def insert_fplagp_report_details_data(conn, report_ids):
        def generate_dummy_data(report_ids):
            data = []
            for rep_id in report_ids:
                report_details = {
                    "report_id": rep_id,
                    "land_assessment": faker.text(max_nb_chars=200),
                    "zoning_compliance": random.choice(["Yes", "No"]),
                    "environmental_impact": faker.text(max_nb_chars=200),
                    "future_recommendations": faker.text(max_nb_chars=200),
                    "report_status": random.choice(["Pending", "Completed", "In Progress"])
                }
                data.append(report_details)
            return data

        dummy_data = generate_dummy_data(report_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['report_id']}, '{details['land_assessment']}', '{details['zoning_compliance']}', 
                '{details['environmental_impact']}', '{details['future_recommendations']}', '{details['report_status']}')
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO fplagp_report_details VALUES {', '.join(insert_statements)};
            """
        )

    def insert_rgp_report_details_data(conn, report_ids):
        def generate_dummy_data(report_ids):
            data = []
            for rep_id in report_ids:
                report_details = {
                    "report_id": rep_id,
                    "outreach_success": faker.text(max_nb_chars=200),
                    "technical_assistance_evaluation": faker.text(max_nb_chars=200),
                    "cost_share_effectiveness": faker.text(max_nb_chars=200),
                    "maintenance_review": faker.text(max_nb_chars=200),
                    "permanent_protection_review": faker.text(max_nb_chars=200),
                    "report_status": random.choice(["Pending", "Completed", "In Progress"])
                }
                data.append(report_details)
            return data

        dummy_data = generate_dummy_data(report_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['report_id']}, '{details['outreach_success']}', '{details['technical_assistance_evaluation']}', 
                '{details['cost_share_effectiveness']}', '{details['maintenance_review']}', 
                '{details['permanent_protection_review']}', '{details['report_status']}')
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO rgp_report_details VALUES {', '.join(insert_statements)};
            """
        )

    def insert_rppgp_report_details_data(conn, report_ids):
        def generate_dummy_data(report_ids):
            data = []
            for rep_id in report_ids:
                report_details = {
                    "report_id": rep_id,
                    "cultivation_assessment": faker.text(max_nb_chars=200),
                    "community_engagement_review": faker.text(max_nb_chars=200),
                    "budget_justification_review": faker.text(max_nb_chars=200),
                    "partnerships_review": faker.text(max_nb_chars=200),
                    "report_status": random.choice(["Pending", "Completed", "In Progress"])
                }
                data.append(report_details)
            return data

        dummy_data = generate_dummy_data(report_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['report_id']}, '{details['cultivation_assessment']}', '{details['community_engagement_review']}', 
                '{details['budget_justification_review']}', '{details['partnerships_review']}', '{details['report_status']}')
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO rppgp_report_details VALUES {', '.join(insert_statements)};
            """
        )

    application_ids = get_application_ids(conn)
    report_ids = insert_reports_data(conn, application_ids)
    
    insert_dagp_report_details_data(conn, report_ids)
    insert_fplagp_report_details_data(conn, report_ids)
    insert_rgp_report_details_data(conn, report_ids)
    insert_rppgp_report_details_data(conn, report_ids)
    
    print("Report details data inserted successfully.")