import sys
import pandas as pd
import glob
import functions
import os

region = 32  # Hauts de France
reg_date = '^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])-[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$'
cl_age90 = ['0', '09', '19', '29', '39', '49', '59', '69', '79', '89', '90']
output_directory = 'extracted_csv/'

# Ouverture des fichiers dans le répertoires et itération dessus
for file_name in glob.glob("*.csv"):
    try:
        dataframe = pd.read_csv(file_name, delimiter=";", keep_default_na=False)
        filtered_dataframe = dataframe[(dataframe.reg == region) & (dataframe.cl_age90 == int(cl_age90[0]))]
        week = filtered_dataframe.iloc[0]['semaine']
        index = 0
        weekly_filtered_dataframe = pd.DataFrame(columns=filtered_dataframe.columns)

        while index < filtered_dataframe.shape[0]:
            current_row = filtered_dataframe.iloc[index]
            if functions.verify_format_regex(reg_date, current_row['semaine']):
                if current_row['semaine'] == week:
                    try:
                        weekly_filtered_dataframe = weekly_filtered_dataframe.append(
                            functions.replace_dot_by_coma(current_row))
                        week = functions.add_week(current_row['semaine'])
                    except ValueError:
                        print('Data missing')
            else:
                print('Error in dates')
                print('Error at index ' + str(index))
                print("Invalid format. Expected 'YYYY-mm-dd-YYYY-mm-dd' date format, and dates found are '" +
                      current_row['semaine'] + "'")
                sys.exit('Cannot write new csv file')
            index += 1
        for values in weekly_filtered_dataframe.values:
            for value in values:
                weekly_filtered_dataframe = weekly_filtered_dataframe.replace(value, functions.replace_dot_by_coma(str(value)))
        functions.write_csv(weekly_filtered_dataframe, file_name,output_directory)

    except ValueError:
        print('Error reading csv')
