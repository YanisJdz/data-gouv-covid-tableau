import sys

import pandas as pd
import glob
import datetime

region = 32  # Hauts de France
age = 0  # Tout-âge

# Ouverture des fichiers dans le répertoires et itération dessus
for file_name in glob.glob("*.csv"):
    try:
        dataFrame = pd.read_csv(file_name, delimiter=";", keep_default_na=False)
        dataFrame_out = dataFrame[(dataFrame.reg == region) & (dataFrame.cl_age90 == age)]
        file_date = dataFrame_out.iloc[0]['semaine']
        index = 0
        weekly_filtered_dataframe = pd.DataFrame(columns=dataFrame_out.columns)

        while index < dataFrame_out.shape[0]:
            if dataFrame_out.iloc[index]['semaine'] == file_date:
                try:
                    weekly_filtered_dataframe = weekly_filtered_dataframe.append(dataFrame_out.iloc[index])
                    try:
                        dates = dataFrame_out.iloc[index]['semaine'].split('-')
                        next_start = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
                        next_ending = datetime.datetime(int(dates[3]), int(dates[4]), int(dates[5]))
                        next_start = next_start + datetime.timedelta(days=7)
                        next_ending = next_ending + datetime.timedelta(days=7)
                        file_date = next_start.strftime("%Y") + '-' + next_start.strftime("%m") + '-' + next_start.strftime("%d") + '-' + next_ending.strftime("%Y") + '-' + next_ending.strftime("%m") + '-' + next_ending.strftime("%d")
                    except ValueError:
                        print('Error in dates')
                        sys.exit(1)
                except ValueError:
                    print('Data missing')
            index += 1

        # Réécriture dans un nouveau fichier csv
        try:
            weekly_filtered_dataframe.to_csv('extracted_csv/extracted_' + file_name, header=True, index=False)
            print('File created ! ')
        except FileNotFoundError:
            print('Error writing file')

    except ValueError:
        print('Error reading csv')
