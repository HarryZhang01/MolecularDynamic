# Wenhan Zhang
# MD code integration of Verlet algorithm
from numpy import cos, array
import matplotlib.pyplot as plt

k = 1
m = 1
dt = 0.1
tm = 10

x = [1]
v = [0]
t = [0]

i = 0
while t[-1] <= tm:
    a = -(k/m) * x[i]

    if i == 0:
        v_next = v[i] + a * dt
        x_next = x[i] + v_next * dt

    else:
        x_next = 2 * x[i] - x[i - 1] + a * dt**2


    x.append(x_next)

    t.append(t[i] + dt)

    i += 1

omg = (k/m)**0.5
xa = x[0] * cos(omg * array(t))

plt.plot(t, xa, label = "Analytical")
plt.plot(t, x, "ro", label = "Verlet")
plt.title("Verlet", fontweight = "bold", fontsize = 16)
plt.xlabel("X", fontweight = "bold", fontsize = 14)
plt.ylabel("Y", fontweight = "bold", fontsize = 14)
plt.grid(True)
plt.legend()
plt.show()



