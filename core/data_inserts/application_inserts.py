import random
from faker import Faker

faker = Faker()
faker.seed_instance(42)
mock_data_row_count = 50

def generate_application_mock_data(conn):
    def insert_applications_data(conn):
        def generate_dummy_data(mock_data_row_count):
            data = []
            for _ in range(mock_data_row_count):
                application = {
                    "application_id": faker.random_int(min=1, max=10000),
                    "grant_id": faker.random_int(min=1, max=11),  # Assuming you have 11 grants
                    "applicant_type": random.choice(["Farmer/Rancher", "Organization", "Conservation District"]),
                    "first_name": faker.first_name(),
                    "last_name": faker.last_name(),
                    "email": faker.email(),
                    "phone": faker.phone_number(),
                    "application_date": faker.date_this_year(),
                    "physical_address": faker.street_address(),
                    "physical_city": faker.city(),
                    "physical_state": faker.state_abbr(),
                    "physical_zip": faker.zipcode(),
                    "mailing_address": faker.street_address(),
                    "mailing_city": faker.city(),
                    "mailing_state": faker.state_abbr(),
                    "mailing_zip": faker.zipcode(),
                    "property_address": faker.street_address(),
                    "property_city": faker.city(),
                    "property_state": faker.state_abbr(),
                    "property_zip": faker.zipcode(),
                    "property_county": faker.word(),  # Using a random word to simulate a county name
                    "property_acreage": round(random.uniform(1, 500), 2),
                    "amount_requested": round(random.uniform(1000, 100000), 2),
                    "source_of_information": random.choice(["Internet", "Mail", "Word of Mouth", "Other"]),
                    "has_signature": random.choice([True, False]),
                    "application_preparer": faker.name()
                }
                data.append(application)
            return data
        dummy_data = generate_dummy_data(mock_data_row_count)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        application_ids = []
        for application in dummy_data:
            application_ids.append(application['application_id'])
            insert_statements.append(f"""
                ({application['application_id']}, {application['grant_id']}, '{application['applicant_type']}', 
                '{application['first_name']}', '{application['last_name']}', '{application['email']}', 
                '{application['phone']}', '{application['application_date']}', '{application['physical_address']}', 
                '{application['physical_city']}', '{application['physical_state']}', '{application['physical_zip']}', 
                '{application['mailing_address']}', '{application['mailing_city']}', '{application['mailing_state']}', 
                '{application['mailing_zip']}', '{application['property_address']}', '{application['property_city']}', 
                '{application['property_state']}', '{application['property_zip']}', '{application['property_county']}', 
                {application['property_acreage']}, {application['amount_requested']}, '{application['source_of_information']}', 
                {application['has_signature']}, '{application['application_preparer']}')
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO applications VALUES {', '.join(insert_statements)};
            """
        )
        return application_ids

    def insert_dagp_application_details_data(conn, application_ids):
        def generate_dummy_data(application_ids):
            data = []
            for app_id in application_ids:
                application_details = {
                    "application_id": app_id,  # Use the passed application_id
                    "farm_ranch_name": faker.company(),
                    "property_tax_id": faker.uuid4(),
                    "latitude_longitude": f"{round(random.uniform(-90, 90), 6)}, {round(random.uniform(-180, 180), 6)}",
                    "operation_type": random.choice(["Commercial", "Subsistence", "Hobby"]),
                    "property_owners": ', '.join(faker.name() for _ in range(random.randint(1, 3))),
                    "farm_type": random.choice(["Irrigated crop", "Non-irrigated crop", "Livestock", "Other"]),
                    "acres_impacted": round(random.uniform(1, 500), 2),
                    "damage_description": faker.text(max_nb_chars=200),
                    "fund_usage": faker.text(max_nb_chars=200),
                    "expense_documentation": faker.text(max_nb_chars=200),
                    "proof_of_damage": faker.text(max_nb_chars=200),
                    "proof_of_payment": faker.text(max_nb_chars=200),
                    "leased_property_letter": faker.text(max_nb_chars=200),
                    "is_limited_resource": random.choice([True, False]),
                    "is_socially_disadvantaged": random.choice([True, False])
                }
                data.append(application_details)
            return data
        
        dummy_data = generate_dummy_data(application_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['application_id']}, '{details['farm_ranch_name']}', '{details['property_tax_id']}', 
                '{details['latitude_longitude']}', '{details['operation_type']}', '{details['property_owners']}', 
                '{details['farm_type']}', {details['acres_impacted']}, '{details['damage_description']}', 
                '{details['fund_usage']}', '{details['expense_documentation']}', '{details['proof_of_damage']}', 
                '{details['proof_of_payment']}', '{details['leased_property_letter']}', 
                {details['is_limited_resource']}, {details['is_socially_disadvantaged']})
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO dagp_application_details VALUES {', '.join(insert_statements)};
            """
        )

    def insert_fplagp_application_details_data(conn, application_ids):
        def generate_dummy_data(application_ids):
            data = []
            for app_id in application_ids:
                application_details = {
                    "application_id": app_id,  # Use the passed application_id
                    "property_tax_parcel_ids": faker.uuid4(),
                    "property_zoning": random.choice(["Residential", "Commercial", "Agricultural", "Industrial"]),
                    "project_description": faker.text(max_nb_chars=200),
                    "site_viability_description": faker.text(max_nb_chars=200),
                    "site_infrastructure_description": faker.text(max_nb_chars=200),
                    "threat_of_conversion": faker.text(max_nb_chars=200),
                    "project_timeline": faker.text(max_nb_chars=100),
                    "match_funding_source": faker.company(),
                    "match_funding_status": random.choice(["Applied", "Awarded", "Under Agreement"]),
                    "future_farmer_identified": random.choice([True, False]),
                    "future_farmer_characteristics": faker.text(max_nb_chars=100),
                    "natural_resource_investment_opportunity": faker.text(max_nb_chars=200),
                    "eligibility_conservation_easements": random.choice([True, False]),
                    "secured_loan_through_farmPAI": random.choice([True, False])
                }
                data.append(application_details)
            return data
        
        dummy_data = generate_dummy_data(application_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['application_id']}, '{details['property_tax_parcel_ids']}', '{details['property_zoning']}', 
                '{details['project_description']}', '{details['site_viability_description']}', 
                '{details['site_infrastructure_description']}', '{details['threat_of_conversion']}', 
                '{details['project_timeline']}', '{details['match_funding_source']}', 
                '{details['match_funding_status']}', {details['future_farmer_identified']}, 
                '{details['future_farmer_characteristics']}', '{details['natural_resource_investment_opportunity']}', 
                {details['eligibility_conservation_easements']}, {details['secured_loan_through_farmPAI']})
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO fplagp_application_details VALUES {', '.join(insert_statements)};
            """
        )

    def insert_rgp_application_details_data(conn, application_ids):
        def generate_dummy_data(application_ids):
            data = []
            for app_id in application_ids:
                application_details = {
                    "application_id": app_id,  # Use the passed application_id
                    "cca_requirements_completed": random.choice([True, False]),
                    "project_types_requested": faker.text(max_nb_chars=100),
                    "riparian_outreach_funds_requested": round(random.uniform(1000, 50000), 2),
                    "riparian_outreach_activities": faker.text(max_nb_chars=200),
                    "technical_assistance_funds_requested": round(random.uniform(1000, 50000), 2),
                    "technical_assistance_activities": faker.text(max_nb_chars=200),
                    "landowner_cost_share_funds_requested": round(random.uniform(1000, 50000), 2),
                    "landowner_cost_share_activities": faker.text(max_nb_chars=200),
                    "district_implemented_funds_requested": round(random.uniform(1000, 50000), 2),
                    "district_implemented_activities": faker.text(max_nb_chars=200),
                    "maintenance_funds_requested": round(random.uniform(1000, 50000), 2),
                    "maintenance_activities": faker.text(max_nb_chars=200),
                    "permanent_protection_funds_requested": round(random.uniform(1000, 50000), 2),
                    "permanent_protection_activities": faker.text(max_nb_chars=200),
                    "prioritized_projects": faker.text(max_nb_chars=100),
                    "water_quality_impairment": random.choice([True, False]),
                    "nature_of_impairment": faker.text(max_nb_chars=100),
                    "sti_plan": random.choice([True, False]),
                    "sti_plan_intersection": faker.text(max_nb_chars=100),
                    "adjacent_project": random.choice([True, False]),
                    "adjacent_project_description": faker.text(max_nb_chars=200),
                    "leverages_other_resources": random.choice([True, False]),
                    "resource_leverage_description": faker.text(max_nb_chars=200),
                    "continuous_project": random.choice([True, False]),
                    "environmental_justice": random.choice([True, False]),
                    "environmental_justice_description": faker.text(max_nb_chars=200),
                    "tribal_notification_letter": faker.text(max_nb_chars=200),
                    "cpds_acknowledgment": random.choice([True, False]),
                    "voucher_acknowledgment": random.choice([True, False])
                }
                data.append(application_details)
            return data
        
        dummy_data = generate_dummy_data(application_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['application_id']}, {details['cca_requirements_completed']}, '{details['project_types_requested']}', 
                {details['riparian_outreach_funds_requested']}, '{details['riparian_outreach_activities']}', 
                {details['technical_assistance_funds_requested']}, '{details['technical_assistance_activities']}', 
                {details['landowner_cost_share_funds_requested']}, '{details['landowner_cost_share_activities']}', 
                {details['district_implemented_funds_requested']}, '{details['district_implemented_activities']}', 
                {details['maintenance_funds_requested']}, '{details['maintenance_activities']}', 
                {details['permanent_protection_funds_requested']}, '{details['permanent_protection_activities']}', 
                '{details['prioritized_projects']}', {details['water_quality_impairment']}, 
                '{details['nature_of_impairment']}', {details['sti_plan']}, '{details['sti_plan_intersection']}', 
                {details['adjacent_project']}, '{details['adjacent_project_description']}', 
                {details['leverages_other_resources']}, '{details['resource_leverage_description']}', 
                {details['continuous_project']}, {details['environmental_justice']}, 
                '{details['environmental_justice_description']}', '{details['tribal_notification_letter']}', 
                {details['cpds_acknowledgment']}, {details['voucher_acknowledgment']})
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO rgp_application_details VALUES {', '.join(insert_statements)};
            """
        )

    def insert_rppgp_application_details_data(conn, application_ids):
        def generate_dummy_data(application_ids):
            data = []
            for app_id in application_ids:
                application_details = {
                    "application_id": app_id,  # Use the passed application_id
                    "funding_category": random.choice([
                        "Purchasing native riparian trees and shrubs", 
                        "Maintenance of plants", 
                        "Creation or expansion of a holding site"
                    ]),
                    "cultivation_experience": faker.text(max_nb_chars=200),
                    "partnerships": random.choice([True, False]),
                    "community_engagement": faker.text(max_nb_chars=200),
                    "budget_justification": faker.text(max_nb_chars=200),
                    "additional_budget_documents": random.choice([True, False])
                }
                data.append(application_details)
            return data
        
        dummy_data = generate_dummy_data(application_ids)

        # Generate the SQL insert statement for the dummy data
        insert_statements = []
        for details in dummy_data:
            insert_statements.append(f"""
                ({details['application_id']}, '{details['funding_category']}', '{details['cultivation_experience']}', 
                {details['partnerships']}, '{details['community_engagement']}', '{details['budget_justification']}', 
                {details['additional_budget_documents']})
            """)

        # Combine all insert statements into a single SQL command
        conn.sql(
            f"""
                INSERT INTO rppgp_application_details VALUES {', '.join(insert_statements)};
            """
        )
    
    application_ids = insert_applications_data(conn)
    insert_dagp_application_details_data(conn, application_ids)
    insert_fplagp_application_details_data(conn, application_ids)
    insert_rgp_application_details_data(conn, application_ids)
    insert_rppgp_application_details_data(conn, application_ids)
    print("Application details data inserted successfully.")