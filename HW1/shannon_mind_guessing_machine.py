import random

# Markov chain transition probabilities
p_H_to_H = 7/12 # 4/9
p_H_to_T = 5/12 # 5/9
p_T_to_T = 3/8 #  6/11
p_T_to_H = 5/8 #  5/11

# Experimental data for my 32 tosses
data = "TTHTHHHTHHHHHTTHTTHHTHTHHTHTTHHT"
data1 = "THHHTTHHHTHTHTTTTHTTTHTTHHTTHHHH" # this is the data for the friend's experiment

# Number of wrong guesses
error_count = 0

print("Experimental data: ", " ".join(data[22:32]))

# Iterate through the data starting from the 22nd toss
print("Predicted data:     ", end ="")
for i in range(22, 32):
    last_toss = data[i-1]
    if last_toss == "H":
        prob = random.random()
        if prob < p_H_to_T:
            guess = "T"
        else:
            guess = "H"
    elif last_toss == "T":
        prob = random.random()
        if prob < p_T_to_H:
            guess = "H"
        else:
            guess = "T"
    if guess != data[i]:
        error_count += 1
    print(guess, end=" ")
print("\nNumber of wrong guesses:", error_count)