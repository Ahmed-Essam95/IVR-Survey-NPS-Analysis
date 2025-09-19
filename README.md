# Excel NPS Analyzer

A high-performance, robust Python tool designed to process massive Excel survey data, calculate Net Promoter Score (NPS), and generate detailed agent-level reports. Built to handle datasets exceeding one million rows across 46 columns efficiently.

🚀 Features
Massive Data Handling: Efficiently processes single Excel workbooks containing over 1 million rows and 46 columns.

Multi-Sheet Support: Automatically detects and concatenates data from all sheets within the master Excel file, even with varying column structures.

NPS Calculation: Computes accurate Net Promoter Scores (NPS) based on standard survey methodology (Promoters: 9-10, Passives: 7-8, Detractors: 0-6).

Team Filtering: Generates reports for specific teams ( team_name or team_name  ).

Temporal Analysis: Filters and analyzes data for any specific month of the year.

Robust Error Handling: Features a resilient workflow with multiple retry attempts for file access and user input.

Automated Reporting: Outputs a clean C-Sat Result.xlsx file with agent-level performance metrics.

📊 Output Report
The tool generates an Excel file (C-Sat Result.xlsx) with the following columns for each agent:

User Name: The agent's identifier.

All Survey: Total number of surveys received.

Promoters: Count of ratings 9-10.

Natural: Count of ratings 7-8.

Detractors: Count of ratings 0-6.

Answered: Total number of answered surveys (Promoters + Natural + Detractors).

NPS%: The final Net Promoter Score percentage.
