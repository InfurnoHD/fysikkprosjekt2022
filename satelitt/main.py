# This is a sample Python script.

# Physical values
from array import array
from pylab import *
import numpy
import matplotlib

#tar utgangspunkt i vær-satelitt
M = 5.972e24 # kg
R = 4.2371e7 # m
v0mag = 3178 # m/s
G = 6.673e-11   # mˆ3\,kgˆ-1 sˆ-2
# Initial conditions
r0 = R*array([1, 0])
#L =  0.0011 #luftmotsand/friksjon

#Draw the earth and set color to green
theta = linspace(0, 2*pi, 100)
x = 6371000*cos(theta)
y = 6371000*sin(theta)
plot(x, y, 'g-')



v0 = v0mag*array([0, 1])
# Numerical values
time = 60*60*24*5 #s
dt = 1000 #s
# Setup Simulation
n = int(round(time/dt))




r = zeros((n, 2), float)
v = zeros((n, 2), float)
t = zeros((n, 1), float)
r[0] = r0 # vectors
v[0] = v0 # vectors
GM = G*M
# Calculation loop
for i in range(n-1):
    rr = norm(r[i, :])
    a = -GM*r[i]/rr**3 #- L
    v[i+1] = v[i] + dt*a
    r[i+1] = r[i] + dt*v[i+1]
    t[i+1] = t[i] + dt
plot(r[:, 0], r[:, 1])
xlabel('x [m]'); ylabel('y [m]')
show()
