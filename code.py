# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:52:53 2023

@author: CN
"""
import math 
import io

## Importing the data created by ORDEM for a given mission.
## File is open and the .out file is converted to a list to be exploited
with open("BFLY_SC.OUT", 'r') as f,\
    open('test_output.txt', 'w+') as f2:
    for lines in f:
        if not lines.startswith('#'):
            f2.write(lines)
    f2.close()
    
with open('test_output.txt', 'r') as f2:
    data_int = f2.read()
#    print(data)    
    
#print(data[2])
data_tab=data_int.split()

data=[]
for i in range(360):
    data.append(data_tab[69+8*i:69+8*(i+1)])

## list has been succesfully imported.
#diameters of interest for space debris: choose between [1E-5,1E-4,1E-3,1E-2,1E-1]
my_dico={"1E-5":"2","1E-4":"3","1E-3":"4","1E-2":"5","1E-1":"6","1E-0":"7"}
size_of_debris_min="1E-4";
size_of_debris_max="1E-3"
print(my_dico[size_of_debris_min])

flux_of_interest=[]
for j in range(len(data)-1):
    to_add=float(data[j][int(my_dico[size_of_debris_min])])-float(data[j][int(my_dico[size_of_debris_max])])
    flux_of_interest.append([data[j][0],data[j][1],to_add])

## The matrix flux_of_interest now contains the flux of objects (/m2/year) 
## with a size beteen "size_of_debris" and size_of_debris_max.
    

    

     