import matplotlib.pyplot as plt

k1 = 0.025
k2 = 0.01
delta = 0.1
time = 15.0

c1 = [40.0]
c2 = [34.0]
c3 = [0.0]

t_values = [0.0]
t = 0.0

# Simulation loop
while t <= time:
    # Calculating next values for c1, c2, and c3
    c1_next = c1[-1] + (k2 * c3[-1] - k1 * c1[-1] * c2[-1]) * delta
    c2_next = c2[-1] + (k2 * c3[-1] - k1 * c1[-1] * c2[-1]) * delta
    c3_next = c3[-1] + (k1 * c1[-1] * c2[-1] - k2 * c3[-1]) * delta

    c1.append(c1_next)
    c2.append(c2_next)
    c3.append(c3_next)

    t += delta
    t_values.append(t)

    if t >= 2.0:
        delta = 0.2
    if t >= 6.0:
        delta = 0.4

plt.figure(figsize=(10, 6))
plt.plot(t_values, c1, label="C1", marker='o')
plt.plot(t_values, c2, label="C2", marker='s')
plt.plot(t_values, c3, label="C3", marker='^')

plt.title("Concentration Changes Over Time")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.grid(True)


plt.show()
