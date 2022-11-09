from pylab import *

# values
Mass = 5.972e24  # kg
Radius = 4.2164e7  # m # radius of earth + orbit distance from surface
startVelocity = 3.0746e3  # m/s
Gravity = 6.673e-11  # m^3 kg^-1 s^-2
Friction = 0.00001
MassOfRocket = 1000  # kg

# Initial conditions
r0 = Radius * array([1, 0])  # m
v0 = startVelocity * array([0, 1])  # m/s

# Numerical values
time = 60 * 60 * 24 * 30 * 1  # s
dt = 1  # s

# Setup simulation
n = int(ceil(time / dt))
r = zeros((n, 2), float)
v = zeros((n, 2), float)
t = zeros((n, 1), float)
r[0] = r0  # vectors
v[0] = v0  # vectors
GM = Gravity * Mass

# draw the earth
theta = linspace(0, 2 * pi, 100)
x = 6.371e6 * cos(theta)
y = 6.371e6 * sin(theta)
plot(x, y, 'g-')
# Loop calculation
for i in range(n - 1):
    rr = norm(r[i, :])
    a = -GM * r[i] / rr ** 3 - Friction * v[i]
    v[i + 1] = v[i] + dt * a
    r[i + 1] = r[i] + dt * v[i + 1]
    t[i + 1] = t[i] + dt
    if rr <= 6.371e6:
        print("Crashed!!")
        break

    sys.stdout.write(f"\rTime: {t[i + 1] / 60} minutes")
    sys.stdout.write(f"Distance from surface: {rr - 6.371e6} meters")
    sys.stdout.write(f"Velocity: {norm(v[i + 1])} m/s")
    sys.stdout.flush()

# Plot the results
plot(r[:, 0], r[:, 1])
xlabel('x [m]')
ylabel('y [m]')
title('Orbit of a planet around a star')
show()
