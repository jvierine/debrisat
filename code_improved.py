# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:52:53 2023

@author: CN
"""
import math 
import io
import matplotlib.pyplot as plt

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
size_of_debris_min="1E-3";
size_of_debris_max="1E-2"

flux_of_interest=[]
flux_copy=[]
for j in range(len(data)-1):
    to_add=float(data[j][int(my_dico[size_of_debris_min])])-float(data[j][int(my_dico[size_of_debris_max])])
    flux_of_interest.append([data[j][0],data[j][1],to_add])
    flux_copy.append([data[j][0],data[j][1],to_add])


## The matrix flux_of_interest now contains the flux of objects (/m2/year) 
## with a size beteen "size_of_debris" and size_of_debris_max.

## Adding the Radar parameters
theta=30
D=100
R=D/math.cos(theta*math.pi/180)
R_0=D*math.tan(theta*math.pi/180)
A=math.pi*R_0*R_0
# Diffraction limit= Theta lim
#D_sat is the size of the antenna_radar payload: around 0.1m
c=3E8
f=80E9
Lambda=c/f
D_sat=0.1
theta_max=2*Lambda/D_sat
theta_max_deg=theta_max*180/math.pi

## Mission Parameters
## lenght of the mission should be in months
lenght_of_mission=6

#Assumption: flux is symetrical
flux_work=flux_of_interest[180:]
# # Detections
somme=0
for k in range (1,theta+1):
    somme+=flux_work[k-1][2]*((math.tan(k*math.pi/180))**2-(math.tan((k-1)*math.pi/180)**2))
    # print(somme)
somme=math.pi*D**2*somme


## Adapting to the duration of the mission (flux are /year)
somme=somme*lenght_of_mission/12

print(somme)





# ## Create plots
# x_axis=[]
# y_axis=[]
# for l in range (len(flux_of_interest)):
#     x_axis.append(nb_obj[l][0])
#     y_axis.append(nb_obj[l][2])


# plt.plot(x_axis,y_axis)
# plt.title("Number of objects deteted for a mission of 6 months")
# plt.xlabel("Degrees")
# plt.ylabel("Numbers of objects detected in the area A")
# plt.show()

# print(detections)

    
    



    

     