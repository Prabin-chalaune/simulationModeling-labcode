
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

W = 1.0
F = 1.0
xi_values = [0.1, 0.6, 0.8, 1.0, 3.0]


time = np.linspace(0, 20, 600)
def damped_oscillator(x, t, xi, W, F):
    x1, x2 = x
    dx1dt = x2
    dx2dt = -2 * xi * W * x2 - W**2 * x1 + W**2 * F
    return [dx1dt, dx2dt]

x0 = [0, 0]

plt.figure(figsize=(10, 6))

# Solve and plot for each damping ratio
for xi in xi_values:
    solution = odeint(damped_oscillator, x0, time, args=(xi, W, F))
    plt.plot(time, solution[:, 0], label=f"ζ = {xi}")


plt.title("Response of Damped Oscillator for Various Damping Ratios")
plt.xlabel("Time (t)")
plt.ylabel("Displacement (x(t))")
plt.legend()
plt.grid()
plt.show()
