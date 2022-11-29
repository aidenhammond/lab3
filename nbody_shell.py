# VP03 shell code
# Electic Fields due to part charges
# by Jeff Gritton, Fall 2015
# edited by PCS Fall 2017

from __future__ import division, print_function
from vpython import *
from math import *
import numpy as np

#scene.width = 800
#scene.height = 800

# Constants

num_char = 50
cnt = 0
e0 = 8.85e-12 #C^2 N^-1 m^-2
q_base = 1.60217662e-19 #Coulombs
q_elec = -1.60217662e-19 #Coulombs
m_elec = 9.10938356e-31 #kg
k0 = 1.0/(4.0*pi*e0)
deltat = 1.0e-3
#tmax = 10*365*24*60*60    # 10 years
tmax = 120        # 60 seconds
pscale = 0.3
Fscale = 2000e9

#Read in file ef1.txt
x,y,z,ch = np.loadtxt('ef1.txt', unpack=True)



## try starting with different initial electron positions
# Electron setup and initialization
elec = sphere(pos=vector(10,5,0), radius=1.0, color=color.red, make_trail=True)

# Loop over file input for random charges
i=0
while i<num_char:
    pos_vec = vector(x[i], y[i], z[i])
    #print(pos_vec)
    charge = sphere(pos=pos_vec, radius=1.0*abs(ch[i]), color=color.blue)
    if ch[i] > 0.0:
        charge.color=color.orange
    i=i+1



Farr = arrow(color=color.red)
Parr = arrow(color=color.blue)

## try various initial electron velocities
v_elec = vector(0,1,0)
p_elec = m_elec*v_elec
t = 0
print("p_elec", p_elec)
# Calculation loop
while t < tmax:
    rate(1)    # slow down motion to make animation look nicer
    j=0
    F_net=vector(0,0,0)
    while j < num_char:
        # Force calculation for electron
        pos_vec = vector(x[j], y[j], z[j])
        dP = elec.pos - pos_vec
        #print("dp", dP)
        F_net +=  dP.hat * ch[j] *k0 * q_elec / (dP.mag)**2
        j += 1;

    ## add lines to calculate net electric force acting on electron
    ## due to all charges, the charge is given by ch[i]*q_base 
#    print(j,t,F_net)
    # Momentum Principle and position update

    ## add electron momentum update equation
    ## add electron position update equation
    print("F_net", F_net)
    print("f*t", F_net*deltat)
    p_elec = p_elec + F_net*deltat   
    print("pelec:", p_elec)
    v = (p_elec/m_elec)
    scale = 1e-14
    elec.pos = elec.pos + scale*v*deltat
    print((p_elec/m_elec)*deltat)
    #print(p_elec)
    #print("fnet", F_net)
    

    # Object update
    ## adjust Fscale to show the net force vector
    Farr.pos = elec.pos
    Farr.axis = F_net*Fscale
    print("FARR: ", Farr.axis)
    Parr.pos = elec.pos
    Parr.axis = p_elec*1e14

    #Leaves domain?
    if  abs(elec.pos.x) > 200 or abs(elec.pos.y) > 200 or abs(elec.pos.z) > 200:
        print('GONE!')
        break
    t = t + deltat

while True:
    continue
