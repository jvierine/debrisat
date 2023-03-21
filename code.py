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
size_of_debris_min="1E-4";
size_of_debris_max="1E-3"

flux_of_interest=[]
for j in range(len(data)-1):
    to_add=float(data[j][int(my_dico[size_of_debris_min])])-float(data[j][int(my_dico[size_of_debris_max])])
    flux_of_interest.append([data[j][0],data[j][1],to_add])

## The matrix flux_of_interest now contains the flux of objects (/m2/year) 
## with a size beteen "size_of_debris" and size_of_debris_max.

## Adding the Radar parameters
theta=60
D=10
R=D/math.cos(theta*180/math.pi)
R_0=D*math.tan(theta*180/math.pi)
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

## Reducing flux in accordance to the angle of detection of the radar
for  m in range (len(flux_of_interest)):
    if abs(int(flux_of_interest[m][0]))>theta:
        flux_of_interest[m][2]=0



# Detections
nb_obj=[]
detections=0
for k in range(len(flux_of_interest)):
    x=flux_of_interest[k][2]*A*lenght_of_mission/12
    nb_obj.append([flux_of_interest[k][0],flux_of_interest[k][1],x])
    detections+=x


## Create histogram
x_axis=[]
y_axis=[]
for l in range (len(flux_of_interest)):
    x_axis.append(nb_obj[l][0])
    y_axis.append(nb_obj[l][2])


plt.plot(x_axis,y_axis)
plt.title("Number of objects deteted for a mission of 6 months")
plt.xlabel("Degrees")
plt.ylabel("Numbers of objects detected in the area A")
plt.show()

print(detections)

    
    



    

     