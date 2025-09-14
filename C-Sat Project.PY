
import numpy as np
import pandas as pd
import os
import time
import openpyxl as excel


current_directory = os.getcwd()

sheet_path = f"{current_directory}\\CN7736 - IVR Retail & CC Survey V3.xlsx"


path_lives = 0
while path_lives != 3  :
    print("Checking The File Accessibility.....")
    time.sleep(1.5)

    if os.path.exists(sheet_path):
        print("Excel file exists.")
        break

    else:
        path_lives += 1
        print("\nExcel file ( CN7736 - IVR Retail & CC Survey V3 ) doesn't exist.")
        input(f"\nAdd the file and press Enter to check again.\n")
        continue

if path_lives == 3 :
    print("All Tries Consumed, please try again later")
    exit()


def clearing_screen() :
    print("Clearing Screen.")
    time.sleep(0.5)

    if os.name == "nt" :
        os.system('cls')
    else:
        os.system('clear')


# clearing_screen()


team_select = ""

team_lives = 0
while team_lives != 3 :
    print(f"\nPlease Choose 1 Or 2\n"
          f"1: CC Consumer Billing.\n"
          f"2: CC High Usage.")

    team_select = str(input("\nEnter Your Choice : "))

    if team_select != "1" and team_select != "2" :
        print(f"{team_select}, Invalid Choice, Please Select 1 or 2")
        team_lives += 1

    else:
        if team_select == "1" :
            team_select = "CC Consumer Billing"
        elif team_select == "2" :
            team_select = "CC High Usage"

        break


if team_lives == 3:
    print("All Tries Consumed, please try again later")
    exit()



month_select = 0

month_lives = 0
while month_lives != 3 :
    # Clean
    print("""
1 - January
2 - February
3 - March
4 - April
5 - May
6 - June
7 - July
8 - August
9 - September
10 - October
11 - November
12 - December """)
    month_select = input("\nPlease Enter Month Number : ")

    if not isinstance(month_select,int) :
        print(f"{month_select}, Invalid Choice, Please Select from 1 to 12")
        month_lives += 1
        continue

    if month_select not in [1,2,3,4,5,6,7,8,9,10,11,12]:
        print(f"{month_select}, Invalid Choice, Please Select from 1 to 12")
        month_lives += 1
        continue

    else:
        break


if month_lives == 3:
    print("All Tries Consumed, please try again later")
    exit()


# Clean
print(f"Loading Data, will take around 2 minutes")
read_file = pd.read_excel(sheet_path)
print(f"Data Loaded....")
# Clean

sat_df = read_file.copy()

df_columns = ["INSERTION_DT","Q1_ANSWER: TNPS","No_of_Answered_Questions","Agent_Id_", "OWNER_TEAM","Survey_Identifier"]
df_rows = sat_df["OWNER_TEAM"] ==  team_select


sat_df = sat_df.loc[ df_rows , df_columns]

sat_df["INSERTION_DT"] = sat_df["INSERTION_DT"].dt.month

sat_df = sat_df.loc[  sat_df["INSERTION_DT"] == month_select   , :]


if sat_df.empty :
    print("Checking the data.....")
    time.sleep(2)
    print(f"There is no data for {team_select} Team, at Entered Date Month {month_select}")
    print("Exit.....")
    time.sleep(2)
    exit()


unique_agents = sat_df["Agent_Id_"].unique()


# Calc Machine.
def calc_machine(each_user) :

    df_per_user = sat_df[sat_df["Agent_Id_"] == each_user]

    na_count = df_per_user[df_per_user["Q1_ANSWER: TNPS"].isna()].count()

    standard_count =  df_per_user["Agent_Id_"].count()

    if na_count["Agent_Id_"] == standard_count :
        return None


    else:

        components_list = []
        # -----------------------------------------------------------------
        agent_name = str(each_user)
        components_list.append(agent_name)
        # -------------------------------------
        all_survey = len(df_per_user)
        components_list.append(all_survey)
        # -------------------------------------

        promoters = 0
        natural = 0
        detractors = 0

        column_nps = df_per_user["Q1_ANSWER: TNPS"]

        for cell in column_nps :
            if cell in [9,10]  :
                promoters += 1

            elif cell in [7,8] :
                natural += 1

            elif cell in [0,1,2,3,4,5,6] :
                detractors += 1


        components_list.append(promoters)
        components_list.append(natural)
        components_list.append(detractors)


        # total_answered = df_per_user[ ~df_per_user["No_of_Answered_Questions"].str.contains("No Answered Questions")   ].count()
        # print(total_answered["No_of_Answered_Questions"])

        total_answered = promoters + natural + detractors

        components_list.append(total_answered)

        NPS_Calculation = f"{ ((promoters-detractors) / total_answered) * 100 }%"
        components_list.append(NPS_Calculation)


        return components_list


# Saving Phase

saved_sheet_path = f"{current_directory}\\C-Sat Result.xlsx"

if os.path.exists(saved_sheet_path):
    print("Excel file exists.")


else:
    print("Excel file doesn't exist. Creating a new one...")

    header = ["User Name", "All Survey", "Promoters", "Natural", "Detractors", "Answered", "NPS%"]

    df = pd.DataFrame(columns=header)
    df.to_excel(saved_sheet_path, index=False)
    print(f"Created new Excel file at: {saved_sheet_path}")



saved_workbook = excel.load_workbook(saved_sheet_path)
saved_excel_sheet = saved_workbook["Sheet1"]



for user_agent in unique_agents :
    returned_data = calc_machine(user_agent)

    if returned_data is not None :
        # Each Row By Row.
        saved_excel_sheet.append(returned_data)



saved_workbook.save(saved_sheet_path)



print("Done")


# -----------------------------------------------------
# Alternative Way

# huge_df = {}
# for key, value in ahmed.items():
#     huge_df[key] = value
#     print(f"{key} -> {value}")
