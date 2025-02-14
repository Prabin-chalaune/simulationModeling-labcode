import random

def monte_carlo_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (4 * inside_circle) / num_points
    return pi_estimate

if __name__ == "__main__":
    num_points = int(input("Enter the number of random points: "))
    pi_value = monte_carlo_pi(num_points)
    print(f"Estimated value of π using {num_points} points: {pi_value:.6f}")
