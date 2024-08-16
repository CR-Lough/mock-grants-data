# Grants, Applications, Reports: Dummy Data
## Usage
1. Activate the virtual environment with
```
poetry install
poetry shell
```
2. Generate the dummy data .duckdb
```
cd core
python3 generate.py
```

## General Shape of .duckdb
```mermaid
flowchart LR;
	a[grants] --> b[applications]
	b --> ba[dagp_application_details]
	b --> bb[fplagp_application_details]
	b --> bc[rgp_application_details]
	b --> bd[rppgp_application_details]
	b --> c[reports]
	c --> ca[dagp_report_details]
	c --> cb[fplagp_report_details]
	c --> cc[rgp_report_details]
	c --> cd[rppgp_report_details]
```

## Acronyms
- Conservation Reserve Enhancement Program (CREP)
- Disaster Assistance Program (DAP)
- Farmland Protection and Land Access (FPLA) Program
- Forest Health and Community Wildfire Resiliency (CWR)
- Irrigation Efficiencies Grant Program (IEGP)
- Natural Resource Investments (NRI)
- Riparian Grant Program (RGP)
- Riparian Plant Propagation Program (RPPP)
- Shellfish Program (SP)
- Sustainable Farms & Fields (SFF)
- Sustainable Farms & Fields: Climate-Smart Livestock (SFFCSL)