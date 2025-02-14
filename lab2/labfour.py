def main():
    # Input values for a, b, m
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    m = int(input("Enter the value of m: "))

    seed = int(input("Enter the seed value: "))
    n = int(input("Enter the number of random numbers to be generated: "))

    r = seed
    print("Generated random numbers:")

    # Generate and print random numbers
    for i in range(n):
        r = (a * r + b) % m
        print(r)

if __name__ == "__main__":
    main()
