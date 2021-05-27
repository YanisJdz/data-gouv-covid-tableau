import pandas as pd
import glob
import re

region = 32 #Hauts de France
age = 0 #Tout-âge

#Ouverture des fichiers dans le répertoires et itération dessus
for file_name in glob.glob("*.csv"):

    dataFrame = pd.read_csv(file_name, delimiter=";", keep_default_na=False)

    dataFrame_out = dataFrame[(dataFrame.reg == region) & (dataFrame.cl_age90 == age)]

    file_date = dataFrame_out.iloc[0]['semaine']
    index = 0
    weekly_filtered_dataframe = pd.DataFrame(columns=dataFrame_out.columns)

    while index < dataFrame_out.shape[0]:
        if dataFrame_out.iloc[index]['semaine'] == file_date: #Ici besoin de la condition où "file_date" changerait après chaque '.append()'
            weekly_filtered_dataframe = weekly_filtered_dataframe.append(dataFrame_out.iloc[index])
            #Ici une fois le .append on chercherait à modifier file_date pour rentrer dans condition
            #Exemple : premieres dates = 2021-02-12-2021-02-18
            #Après être rentré dans la condition if on changerait la valeur de file_date par = 2021-02-19-2021-02-25
            #Tout ça pour ne selectionné qu'une ligne par semaine, en démarrant par les premières dates du fichier (ligne 16)
        index += 1

    print(weekly_filtered_dataframe)

#Réécriture dans un nouveau fichier csv
    #dataFrame_out.to_csv('extracted_csv/extracted_'+file_name, header=True, index=False)


#Essayer de récupérer la date de début des test (regexp) type "%d-%d-%d"
#puis traduire en date et TU !!

#Faire attention aux commentaires => Nommer correctement les fonctions peut permettre
#d'éviter de faire des commentaires inutiles

#Éviter les "magiques numbers" en nommant des variables ou autre