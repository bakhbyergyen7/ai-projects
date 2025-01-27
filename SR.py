# Simple reflex agent for vacuum environment

# S/R table for the agent
s_r_table = {
    ('A', 'Clean'): 'Left',
    ('A', 'Dirty'): 'Left',
    ('B', 'Clean'): 'Left',
    ('B', 'Dirty'): 'Left',
}

# Function to simulate the environment
def simulate_environment(initial_state, steps):
    state = initial_state
    performance = 0
    
    for step in range(steps):
        # Get the action from the S/R table based on the current state
        current_location, dirt_status = state
        action = s_r_table[(current_location, dirt_status)]
        
        # Perform the action and update the state
        if action == 'Left':
            if current_location == 'A':
                state = ('B', state[1])
            else:
                state = ('A', state[1])
                
        if dirt_status == 'Dirty':
            performance -= 1
            state = (state[0], 'Clean')
            
    return performance

# Loop over all possible initial configurations and record the performance
performance_scores = []

for current_location in ['A', 'B']:
    for dirt_status in ['Clean', 'Dirty']:
        initial_state = (current_location, dirt_status)
        performance = simulate_environment(initial_state, steps=10)
        performance_scores.append(performance)
        print(f"Initial state: {initial_state}, Performance: {performance}")
        
# Compute the overall average score
average_score = sum(performance_scores) / len(performance_scores)
print(f"Overall average score: {average_score}")
