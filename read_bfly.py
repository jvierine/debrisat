import numpy as n
import matplotlib.pyplot as plt


def read_bfly(fname="ordem_runs/550km_polar/BFLY_SC.OUT"):
    a=n.genfromtxt(fname,skip_header=15)
    azmin=a[:,0]
    azmax=a[:,1]
    mmflux=a[:,4]
    cmflux=a[:,5]    
    plt.plot(azmin,42000*cmflux*5)
    plt.show()
    plt.plot(azmin,n.cumsum(42000*cmflux*5))
    plt.title("Number of collisions of >1cm objects on the Starlink fleet (42000 active satellites)")
    plt.show()
    print(a)



read_bfly()
    
