# IVR Retail & CC Survey NPS Analysis

This project processes messy survey data (~600k rows) from IVR Retail & CC systems, 
filters by **team** and **month**, and generates **Net Promoter Score (NPS) results** per agent.

## Features
- Validates if source Excel file exists.
- User chooses:
  - Team ( X  or Y )
  - Month (January–December)
- Cleans and filters survey data.
- Calculates:
  - Number of Surveys
  - Promoters
  - Detractors
  - Neutrals
  - Answered Surveys
  - Final NPS Score
- Saves results to `C-Sat Result.xlsx`.

## Requirements
pandas
openpyxl


