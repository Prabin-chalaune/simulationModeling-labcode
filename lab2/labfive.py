import math

def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    m = int(input("Enter the value of m: "))

    seed = int(input("Enter the seed value: "))
    n = int(input("Enter the number of random numbers to be generated: "))
    chi_square = 0.0
    observed_frequency = [0] * 10

    # Generate random numbers
    r = seed
    print("Generated random numbers:")
    for _ in range(n):
        r = (a * r + b) % m
        print(r)
        observed_frequency[r % 10] += 1

    expected_frequency = n / 10.0

    for freq in observed_frequency:
        chi_square += (math.pow(freq - expected_frequency, 2)) / expected_frequency

    print(f"Chi-square statistic: {chi_square:.2f}")

    if chi_square < 16.92:  # Critical value for df = 9 and alpha = 0.05
        print("The distribution of random numbers is consistent with a uniform distribution.")
    else:
        print("The distribution of random numbers is not consistent with a uniform distribution.")

if __name__ == "__main__":
    main()

