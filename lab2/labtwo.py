import matplotlib.pyplot as plt

a11 = -60.0
a21 = -10000.0
a22 = 25.50
b1 = -a11
b2 = -a21

# Initial values
t = 0.0
v1 = 0.0
v2 = 0.0
h = 0.005
e1 = 1.5
n = 26

times = []
voltages_v1 = []
voltages_v2 = []

for i in range(1, n + 1):

    k11 = h * ((a11 * v1) + b1 * e1)
    k21 = h * (a11 * (v1 + 0.5 * k11) + b1 * e1)
    k31 = h * (a11 * (v1 + 0.5 * k21) + b1 * e1)
    k41 = h * (a11 * (v1 + k31) + b1 * e1)

    v1 = v1 + (k11 + 2.0 * k21 + 2.0 * k31 + k41) / 6.0

    # Calculate k values for v2
    k12 = h * ((a21 * v1) + (a22 * v2) + b2 * e1)
    k22 = h * (a21 * (v1 + 0.5 * k11) + a22 * (v2 + 0.5 * k12) + b2 * e1)
    k32 = h * (a21 * (v1 + 0.5 * k21) + a22 * (v2 + 0.5 * k22) + b2 * e1)
    k42 = h * (a21 * (v1 + k31) + a22 * (v2 + k32) + b2 * e1)

    v2 = v2 + (k12 + 2.0 * k22 + 2.0 * k32 + k42) / 6.0

    # Update time
    t += h

    # Store data for plotting
    times.append(t)
    voltages_v1.append(v1)
    voltages_v2.append(v2)

plt.figure(figsize=(10, 6))
plt.plot(times, voltages_v1, label='Voltage v1', color='blue', linewidth=2)
plt.plot(times, voltages_v2, label='Voltage v2', color='red', linewidth=2)

plt.xlabel('Time (U/sec)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Time')
plt.legend()

plt.grid(True)
plt.show()

