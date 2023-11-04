# Shannon's "Mind Reading" Machine

# When flipped a coin, there are two possible outcomes: Head (H) and Tail (T)
import random

state = "H" # start state
STEPS = 20

# in Python range(N) produces the values 0 to N-1;
# hence useful to repeat something N times
for i in range(STEPS+1): 
    print(state, end=", ")  # print(state) would end with the default newline
    r = random.random() # pick a uniform random number 0 <= r < 1
    if state == "S":
        if r <= 0.5:
            nextstate = "S"
        else:
            nextstate = "C"
    elif state == "C":
        if r <= 0.5:
            nextstate = "S"
        elif r <= 0.75:
            nextstate = "C"
        else:
            nextstate = "R"
    else: # state == "R"
        if r <= 0.5:
            nextstate = "C"
        else:
            nexstate = "R"
    state = nextstate