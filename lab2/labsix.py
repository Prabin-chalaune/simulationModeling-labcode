N = 10

def calculate_consumption(Y_lag, T_lag):
    return 30 + 0.8 * (Y_lag - T_lag)
def calculate_investment(Y_lag):
    return 2 + 0.15 * Y_lag
def calculate_taxes(Y_lag):
    return 0.3 * Y_lag
def calculate_national_income(C_lag, I_lag, G_lag):
    return C_lag + I_lag + G_lag

def main():
    C = [0] * N
    I = [0] * N
    T = [0] * N
    Y = [0] * N
    G = [0] * N
    Y[0] = 100
    new_G_values = [50, 42, 58, 61, 68, 75, 59, 70, 65]

    for t in range(1, N):
        G[t] = new_G_values[t - 1]
        C[t] = calculate_consumption(Y[t - 1], T[t - 1])
        I[t] = calculate_investment(Y[t - 1])
        T[t] = calculate_taxes(Y[t - 1])
        Y[t] = calculate_national_income(C[t], I[t], G[t])

        print(f"Period {t}: Y = {Y[t]:.2f}, C = {C[t]:.2f}, I = {I[t]:.2f}, "
              f"T = {T[t]:.2f}, G = {G[t]:.2f}")

if __name__ == "__main__":
    main()
