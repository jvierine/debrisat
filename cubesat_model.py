import numpy as n
import scipy.constants as c
import matplotlib.pyplot as plt

def debris_collecting_area(P_t=10,
                           T_sys=10e3,
                           wavelength=3e-3,
                           snr_threshold=25,
                           B=10e3,
                           debris_diameter=1e-3,
                           antenna_diameter=0.1):

    G=4.0*n.pi*antenna_diameter**2.0/wavelength**2.0
    #print(G)
    sigma = 0.25*n.pi*debris_diameter**2.0


    if debris_diameter < wavelength/(n.pi*n.sqrt(3)):
        sigma = (0.25*n.pi*debris_diameter**2.0)*9*(n.pi*debris_diameter/wavwelength)**4
    #print(sigma)
    R_max = ((P_t*(G**2)*(wavelength**2.0)*sigma)/( (4*n.pi)**3*snr_threshold*c.k*T_sys*B))**(1/4)

    print(R_max)

    theta=wavelength/antenna_diameter
    #print("antenna beam angle %1.2f (deg)"%(180*theta/n.pi))
    
    A_deb1 = n.pi*(R_max*n.sin(theta/2))**2
    A_deb2 = R_max**2.0*n.sin(theta/2)

    A_deb=n.maximum(A_deb1,A_deb2)
    
    return(R_max, A_deb1, A_deb2, A_deb)

if __name__ == "__main__":
    antenna_diameters =n.linspace(1e-3,0.1,num=1000)
    R_max,a1,a2,A=debris_collecting_area(antenna_diameter=antenna_diameters)
    plt.plot(antenna_diameters,A)
    plt.show()
    
        
