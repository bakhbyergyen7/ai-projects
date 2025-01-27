import numpy as np

np.random.seed(42)

N = 1000000  # Number of samples
p_B = 0.001
p_E = 0.002
p_A_given_BE = 0.98
p_A_given_B_notE = 0.95
p_A_given_notB_E = 0.29
p_A_given_notB_notE = 0.001
p_J_given_A = 0.95
p_M_given_A = 0.70

weights_sum = 0

for _ in range(N):
    B = np.random.choice([True, False], p=[p_B, 1 - p_B])
    E = np.random.choice([True, False], p=[p_E, 1 - p_E])

    if B and E:
        A = np.random.choice([True, False], p=[p_A_given_BE, 1 - p_A_given_BE])
    elif B:
        A = np.random.choice([True, False], p=[p_A_given_B_notE, 1 - p_A_given_B_notE])
    elif E:
        A = np.random.choice([True, False], p=[p_A_given_notB_E, 1 - p_A_given_notB_E])
    else:
        A = np.random.choice([True, False], p=[p_A_given_notB_notE, 1 - p_A_given_notB_notE])

    J = np.random.choice([True, False], p=[p_J_given_A if A else 1 - p_J_given_A, 1 - p_J_given_A if A else p_J_given_A])
    M = np.random.choice([True, False], p=[p_M_given_A if A else 1 - p_M_given_A, 1 - p_M_given_A if A else p_M_given_A])

    if not J and not M and B and E:
        weights_sum += 1

estimated_probability = weights_sum / N
print("Estimated joint probability p(not J, not M, B, E):", estimated_probability)
