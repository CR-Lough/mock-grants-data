```mermaid
erDiagram
    GRANTS {
        INTEGER grant_id PK
        VARCHAR name
    }
    
    APPLICATIONS {
        INTEGER application_id PK
        INTEGER grant_id FK
        VARCHAR applicant_type
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR email
        VARCHAR phone
        DATE application_date
        VARCHAR physical_address
        VARCHAR physical_city
        VARCHAR physical_state
        VARCHAR physical_zip
        VARCHAR mailing_address
        VARCHAR mailing_city
        VARCHAR mailing_state
        VARCHAR mailing_zip
        VARCHAR property_address
        VARCHAR property_city
        VARCHAR property_state
        VARCHAR property_zip
        VARCHAR property_county
        DECIMAL property_acreage
        DECIMAL amount_requested
        VARCHAR source_of_information
        BOOLEAN has_signature
        VARCHAR application_preparer
        VARCHAR status
    }
    
    REPORTS {
        INTEGER report_id PK
        INTEGER application_id FK
        DATE report_date
        TEXT report_summary
    }

    DAGP_REPORT_DETAILS {
        INTEGER report_id PK FK
        TEXT damages_assessed
        DECIMAL compensation_amount
        TEXT corrective_measures
        VARCHAR report_status
    }

    FPLAGP_REPORT_DETAILS {
        INTEGER report_id PK FK
        TEXT land_assessment
        VARCHAR zoning_compliance
        TEXT environmental_impact
        TEXT future_recommendations
        VARCHAR report_status
    }

    RGP_REPORT_DETAILS {
        INTEGER report_id PK FK
        TEXT outreach_success
        TEXT technical_assistance_evaluation
        TEXT cost_share_effectiveness
        TEXT maintenance_review
        TEXT permanent_protection_review
        VARCHAR report_status
    }

    RPPGP_REPORT_DETAILS {
        INTEGER report_id PK FK
        TEXT cultivation_assessment
        TEXT community_engagement_review
        TEXT budget_justification_review
        TEXT partnerships_review
        VARCHAR report_status
    }

    DAGP_APPLICATION_DETAILS {
        INTEGER application_id PK FK
        VARCHAR farm_ranch_name
        VARCHAR property_tax_id
        VARCHAR latitude_longitude
        VARCHAR operation_type
        TEXT property_owners
        TEXT farm_type
        DECIMAL acres_impacted
        TEXT damage_description
        TEXT fund_usage
        TEXT expense_documentation
        TEXT proof_of_damage
        TEXT proof_of_payment
        TEXT leased_property_letter
        BOOLEAN is_limited_resource
        BOOLEAN is_socially_disadvantaged
    }

    FPLAGP_APPLICATION_DETAILS {
        INTEGER application_id PK FK
        VARCHAR property_tax_parcel_ids
        VARCHAR property_zoning
        TEXT project_description
        TEXT site_viability_description
        TEXT site_infrastructure_description
        TEXT threat_of_conversion
        TEXT project_timeline
        VARCHAR match_funding_source
        VARCHAR match_funding_status
        BOOLEAN future_farmer_identified
        TEXT future_farmer_characteristics
        TEXT natural_resource_investment_opportunity
        BOOLEAN eligibility_conservation_easements
        BOOLEAN secured_loan_through_farmPAI
    }

    RGP_APPLICATION_DETAILS {
        INTEGER application_id PK FK
        BOOLEAN cca_requirements_completed
        TEXT project_types_requested
        DECIMAL riparian_outreach_funds_requested
        TEXT riparian_outreach_activities
        DECIMAL technical_assistance_funds_requested
        TEXT technical_assistance_activities
        DECIMAL landowner_cost_share_funds_requested
        TEXT landowner_cost_share_activities
        DECIMAL district_implemented_funds_requested
        TEXT district_implemented_activities
        DECIMAL maintenance_funds_requested
        TEXT maintenance_activities
        DECIMAL permanent_protection_funds_requested
        TEXT permanent_protection_activities
        TEXT prioritized_projects
        BOOLEAN water_quality_impairment
        TEXT nature_of_impairment
        BOOLEAN sti_plan
        TEXT sti_plan_intersection
        BOOLEAN adjacent_project
        TEXT adjacent_project_description
        BOOLEAN leverages_other_resources
        TEXT resource_leverage_description
        BOOLEAN continuous_project
        BOOLEAN environmental_justice
        TEXT environmental_justice_description
        TEXT tribal_notification_letter
        BOOLEAN cpds_acknowledgment
        BOOLEAN voucher_acknowledgment
    }

    RPPGP_APPLICATION_DETAILS {
        INTEGER application_id PK FK
        TEXT funding_category
        TEXT cultivation_experience
        BOOLEAN partnerships
        TEXT community_engagement
        TEXT budget_justification
        BOOLEAN additional_budget_documents
    }
    
    GRANTS ||--o{ APPLICATIONS : "has"
    APPLICATIONS ||--o{ REPORTS : "creates"
    REPORTS ||--o{ DAGP_REPORT_DETAILS : "includes"
    REPORTS ||--o{ FPLAGP_REPORT_DETAILS : "includes"
    REPORTS ||--o{ RGP_REPORT_DETAILS : "includes"
    REPORTS ||--o{ RPPGP_REPORT_DETAILS : "includes"
    APPLICATIONS ||--o{ DAGP_APPLICATION_DETAILS : "has"
    APPLICATIONS ||--o{ FPLAGP_APPLICATION_DETAILS : "has"
    APPLICATIONS ||--o{ RGP_APPLICATION_DETAILS : "has"
    APPLICATIONS ||--o{ RPPGP_APPLICATION_DETAILS : "has"
```