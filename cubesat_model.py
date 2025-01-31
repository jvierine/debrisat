import numpy as n
import scipy.constants as c
import matplotlib.pyplot as plt

def debris_collecting_area(P_t=0.25, # 24 dBm
                           T_sys=10e3,
                           wavelength=3e-3,
                           snr_threshold=25,
                           B=10e3,
                           debris_diameter=1e-3,
                           antenna_diameter=0.1):

    # antenna gain, assumed constant and defined on perfect antenna area
    G=4.0*n.pi*antenna_diameter**2.0/wavelength**2.0

    # radar cross-section of space debris object (geometric scatter)
    sigma = 0.25*n.pi*debris_diameter**2.0

    # radar cross-section if Rayleigh scatter 
    if debris_diameter < wavelength/(n.pi*n.sqrt(3)):
        sigma = (0.25*n.pi*debris_diameter**2.0)*9*(n.pi*debris_diameter/wavelength)**4

    # maximum detection distance (meters) based on the radar equation
    R_max = ((P_t*(G**2)*(wavelength**2.0)*sigma)/( (4*n.pi)**3*snr_threshold*c.k*T_sys*B))**(1/4)

    # antenna high gain beam width, assuming symmetric beam shape
    theta=wavelength/antenna_diameter

    # area of beam "cap" at maximum detection distance, assuming radar pointed towards debris flux
    A_deb1 = n.pi*(R_max*n.sin(theta/2))**2
    # area of the triangular beam cross-section. assuming antenna pointed perpendicular to direction where
    # debris comes from
    A_deb2 = R_max**2.0*n.sin(theta/2) # propto antenna_diameter

    # we want to find the best of these two cases
    A_deb=n.maximum(A_deb1,A_deb2)
    
    return(R_max, A_deb1, A_deb2, A_deb)

if __name__ == "__main__":
    antenna_diameters =n.linspace(1e-3,0.1,num=1000)
    P_t=0.25
    R_max,a1,a2,A=debris_collecting_area(antenna_diameter=antenna_diameters,P_t=0.25)
    plt.plot(antenna_diameters*1e3,A)
    plt.title("P_tx = %1.2f W"%(P_t))
    plt.xlabel("Antenna diameter (mm)")
    plt.ylabel("Effective collecting area (m$^2$)")
    plt.show()
    
        
