# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 05:01:42 2021

@author: Tasneem Said
"""

#1.	Read the dataset, convert it to DataFrame and display some from it.
import pandas as pd
import matplotlib.pyplot as plt

#2.	Display structure and summary of the data.
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()

#3.	Clean the data (null, duplications)
dataset.drop_duplicates(subset =["Title","Company","Location","Type",
                        "Level","YearsExp","Country","Skills"],
                        keep = "first", inplace = True)

#4.	Count the jobs for each company 
T=dataset['Title'].value_counts() 
#5.	Show step 4 in a pie chart
plt.pie(T)

#6.	Find out what are the most popular job titles.
#7.	Show step 6 in bar chart
TK=T.keys()
plt.bar(TK,T, color ='maroon', width = 0.4)
#applied step 6,7 on less data
databar = {'Accountant':57, 'Sales Representative':47,
           'Graphic Designer':43,'Digital Marketing Specialist':26,
		   'Sales Manager':25,'Social Media Specialist':25,
           'Receptionist':23,'Executive Secretary':21,
           'Sales Executive':18,'Marketing Specialist':17}
Title = list(databar.keys())
values = list(databar.values())
plt.bar(Title,values, color ='maroon', width = 0.4)

#8.	Find out the most popular areas
#9.	Show step 8 in bar chart
L=dataset['Location'].value_counts() 
Lk=L.keys()
plt.bar(Lk,L, color ='maroon', width = 0.4)

#10.Print skills one by one 
S=dataset['Skills'].value_counts() 
dataset.sort_values("Skills", inplace = True)
print(dataset['Skills'])



