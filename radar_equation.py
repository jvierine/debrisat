import numpy as n
import scipy.constants as c
import matplotlib.pyplot as plt\

def hard_target_enr(gain_tx, gain_rx,
                    wavelength_m, power_tx,
                    range_tx_m, range_rx_m,
                    diameter_m=0.01, bandwidth=10,
                    rx_noise_temp=150.0):
    '''
    Deterine the energy-to-noise ratio for a hard target (signal-to-noise ratio).
    Assume a smooth transition between Rayleigh and optical scattering.

    gain_tx - transmit antenna gain, linear
    gain_rx - receiver antenna gain, linear
    wavelength_m - radar wavelength (meters)
    power_tx - transmit power (W)
    range_tx_m - range from transmitter to target (meters)
    range_rx_m - range from target to receiver (meters)
    diameter_m - object diameter (meters)
    bandwidth - effective receiver noise bandwidth for incoherent integration (tx_len*n_ipp/sample_rate)
    rx_noise_temp - receiver noise temperature (K)
    (Markkanen et.al., 1999)

    Info about radar cross-section on page 17-18 of:
    https://www.sgo.fi/~jussi/spade/FR_16Apr2002.pdf
    '''
    ##
    ## Determine returned signal power, given diameter of sphere
    ## Ignore Mie regime and use either optical or rayleigh scatter
    ##
    is_rayleigh = diameter_m < wavelength_m/(n.pi*n.sqrt(3.0))
    is_optical = diameter_m >= wavelength_m/(n.pi*n.sqrt(3.0))
    rayleigh_power = (9.0*power_tx*(((gain_tx*gain_rx)*(n.pi**2.0)*(diameter_m**6.0))/(256.0*(wavelength_m**2.0)*(range_rx_m**2.0*range_tx_m**2.0))))
    optical_power = (power_tx*(((gain_tx*gain_rx)*(wavelength_m**2.0)*(diameter_m**2.0)))/(256.0*(n.pi**2)*(range_rx_m**2.0*range_tx_m**2.0)))
    rx_noise = c.k*rx_noise_temp*bandwidth
    return(((is_rayleigh)*rayleigh_power + (is_optical)*optical_power)/rx_noise)
    



def sweep_distance():
    # AWR1843 demo board peak gain 10.5 dBi
    G=10**(10.5/10.0)
    Ptx = 8 # Watts (Elligsen said this could be achievable)
    # convert dBi to linear gain
    # note that this is peak gain, ignoring the antenna gain pattern.
    freq=80e9
    lam = c.c/freq
    print(lam)
    # 
    ranges = n.linspace(1,1000,num=100)
    d=lam
    # one radar pulse of length 30 microseconds
    B = 1/30e-6
    T_sys = 9170 # Kelvin, based on AWR1843 data sheet with 15 dB noise figure

    # eiscat
    if False:
        Ptx=1e6
        G=10**4.8
        freq=930e6
        lam=c.c/freq
        ranges=n.linspace(100e3,1000e3,num=100)
        d=0.02
        B=45
        T_sys=100
    
    enrs=hard_target_enr(G,
                         G,
                         lam,
                         Ptx,
                         ranges, ranges,
                         diameter_m=d,
                         bandwidth=B,
                         rx_noise_temp=T_sys)
    plt.loglog(ranges,enrs)
    plt.grid()
    plt.xlabel("Distance (m)")
    plt.ylabel("Signal-to-noise ratio")
    plt.show()


sweep_distance()
