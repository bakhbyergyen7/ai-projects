import numpy as np
from gridworld import GridWorld

# Declare our environmnet variable
# The world has 3 rows and 4 columns
env = GridWorld(3, 4)
# Define the state matrix
# Adding obstacle at position (1,1)
# Adding the two terminal states
state_matrix = np.zeros((3,4))
state_matrix[0, 3] = 1
state_matrix[1, 3] = 1
state_matrix[1, 1] = -1
# Define the reward matrix
# The reward is -0.04 for all states but the terminal
reward_matrix = np.full((3,4), -0.04)
reward_matrix[0, 3] = 1
reward_matrix[1, 3] = -1
# Define the transition matrix
# For each one of the four actions there is a probability
transition_matrix = np.array([[0.8, 0.1, 0.0, 0.1],
                              [0.1, 0.8, 0.1, 0.0],
                              [0.0, 0.1, 0.8, 0.1],
                              [0.1, 0.0, 0.1, 0.8]])
# Define the policy matrix
# 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT, NaN=Obstacle, -1=NoAction
# This is the optimal policy for world with reward=-0.04
policy_matrix = np.array([[1,      1,  1,  -1],
                          [0, np.NaN,  0,  -1],
                          [0,      3,  3,   3]])
# Set the matrices 
env.setStateMatrix(state_matrix)
env.setRewardMatrix(reward_matrix)
env.setTransitionMatrix(transition_matrix)