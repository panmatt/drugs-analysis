# https://catalog.data.gov/dataset/accidental-drug-related-deaths-january-2012-sept-2015
#
#   Accidental_Drug_Related_Deaths_2012-2018
#
#  

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
import subprocess

def clear():
    os_in_execution = os.name
    if os_in_execution == "nt":
        subprocess.call("cls",shell=True)
    else:
        subprocess.call("clear",shell=True)

csv_file = "Accidental_Drug_Related_Deaths_2012-2018.csv"
clear()
try:
    data = pd.read_csv(csv_file,sep=',')
except FileNotFoundError:
    print("{} could not be found in your path. Make sure it's in the same path of this file." .format(csv_file))
    exit()
# data.shape    5105 rows and 41 columns
columns = np.array(data.columns.values)  
data.drop(columns[[1,2,6,7,8,12,19,39,5,9,10,11,14,15,16,38,40,0,37,17]],axis=1,inplace=True)
# data.shape 5105 rows and 21 rows
male = 0
for x in data["Sex"] == "Male":
    male += x
print("[*] There have been {} males dead due to accidental drug use between 2012 and 2018." .format(male))
female = 0
for y in data["Sex"] == "Female":
    female += y
print("[*] There have been {} females dead due to accidental drug use between 2012 and 2018." .format(female))
unk = 0
for tot in data["Sex"]:
    if tot != "Female" and tot != "Male":
        unk += 1
print("[*] We have no information about {} people." .format(unk))
x = input("[*] Press Y if you want to see the graph or press any other key to skip and go ahead : ")
if x == "Y" or x == "y":
    percentage = [73.90,25.96,0.13]  # correct order : males,females
    labels = ["Males","Females","ND"]
    plt.title("Dead people due to the accidental use of drugs")
    plt.pie(percentage,autopct="%1.1f%%",explode=(0.0,0.05,0.0),labels=labels,shadow=False,startangle=90,colors=["Orange","Blue","Black"])
    plt.show()
else:
    pass
clear()
# 4 ranges : < 18 , 18 - 30, 30 - 45 , 45+
count = 0
for age in data["Age"]:
    if age in range(0,18):
        if str(age) == "Nan":
            continue
        else:
            count += 1
print("[*] Among all the people who died, {} of them are underage." .format(count))
count = 0
for age in data["Age"]:
    if age in range(18,30):
        count += 1
print("[*] Also , {} of them are aged between 18 and 30 years old." .format(count))
count = 0
for age in data["Age"]:
    if age in range(30,45):
        count += 1
print("[*] {} of them are aged between 30 and 45 years old." .format(count))
count = 0
for age in data["Age"]:
    if age in range(45,100):
        count += 1
print("[*] Last but not least , {} of them are aged over 45 years old." .format(count))
count = 0
for age in data["Age"]:
    if str(age) == "nan" or str(age) == "Nan":
        count += 1
print("[*] However , there's no data available for {} people." .format(count))
x = input("[*] Press Y if you want to see the graph or press any other key to skip and go ahead : ")
if x == "Y" or x == "y":
    labs = ["0 - 18","18 - 30","30 - 45","45+","ND"]
    estimated_percentages = [0.25,19.50,36.30,43.90,0.05] # 0-18,18-30,30-45,45+,none
    colors = ["Yellow","Blue","Red","Green","Black"]
    plt.pie(estimated_percentages,autopct="%1.1f%%",explode=(0.0,0.05,0.05,0.0,0.0),labels=labs,colors=colors,shadow=False,startangle=90)
    plt.title("Age range of dead people due to the accidental use of drugs")
    plt.show()
else:
    pass
clear()
cocaine_involved = 0
heroin_involved = 0
benzodiazepine_involved = 0
hydromorphone_involved = 0
ethanol_involved = 0
fent_involved = 0
oxymorph_involved = 0
for x in data["Cocaine"]:
    if x == "Y" or x == "y":
        cocaine_involved += 1
perc_cocaine_involved = (cocaine_involved / 5105) * 100
for x in data["Heroin"]:
    if x == "Y" or x == "y":
        heroin_involved += 1
perc_heroin_involved = (heroin_involved / 5105) * 100
for x in data["Fentanyl"]:
    if x == "Y" or x == "y":
        fent_involved += 1
perc_fent_involved = (fent_involved / 5105) * 100
for x in data["Benzodiazepine"]:
    if x == "Y" or x == "y":
        benzodiazepine_involved += 1
perc_benzos_involved = (benzodiazepine_involved / 5105) * 100
for x in data["Hydromorphone"]:
    if x == "Y" or x == "y":
        hydromorphone_involved += 1
perc_hydro_involved = (hydromorphone_involved / 5105) * 100
for x in data["Ethanol"]:
    if x == "Y" or x == "y":
        ethanol_involved += 1
perc_eth_involved = (ethanol_involved / 5105) * 100
for x in data["Oxymorphone"]:
    if x == "Y" or x == "y":
        oxymorph_involved += 1
perc_oxy_involved = (oxymorph_involved / 5105) * 100
z = input("[*] Press Y if you want to see the graph of drugs involvement in deaths or press any other key to skip and go ahead : ")
if z == "Y" or z == "y":   # 7 drugs
    lab_ = ['Cocaine','Heroin','Fentanyl','Benzodiazepine','Hydromorphone','Ethanol','Oxymorphone']
    colors = ["Red","Orange","Blue","Violet","Black","Gray","Yellow"]
    perc = [perc_cocaine_involved,perc_heroin_involved,perc_fent_involved,perc_benzos_involved,perc_hydro_involved,perc_eth_involved,perc_oxy_involved]
    plt.pie(perc,explode=(0.0,0.03,0.03,0.02,0.04,0.00,0.00),labels=lab_,colors=colors,autopct="%1.1f%%",shadow=True,startangle=90)
    plt.title("Drugs involved in deaths")
    plt.show()
else:
    pass
clear()
print("[*] The most involved drug in deaths is heroin , which is subsequently followed by fentanyl, cocaine , benzodiazepines , ethanol , oxymorphone and hydrocodone.")






