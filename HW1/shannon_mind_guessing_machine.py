# Toss a coin 32 times and record the outcome (as a string of H and T);
# Compute the experimentally observed probability of heads over tosses 2 through 21, inclusive (20 outcomes);
# Compute the Markov chain transition probabilities over the first 21 tosses (viz., the first 20 transitions).

# Computer program that uses the Markov chain model to predict the final ten transitions of each data set 
# (throws 23-32 given the values of throws 22-31, respectively).  That is, given the previous state (throw i), 
# compute the next state (throw i+1) using the model, compare with the actual data, and tally the error function (# of wrong guesses).

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
