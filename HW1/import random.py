import random
import time

def addition(int1, int2):
    # Input processing
    num1 = int(int1)
    num2 = int(int2)
    
    # Arithmetic
    result = num1 + num2
    
    # Randomness
    if random.random() < 0.05:
        result += random.randint(-5, 5)
    
    # Timing
    delay = random.randint(5, 30)
    start_time = time.time() #timer starts
    for j in range(0, delay):
        for i in range(0, 100000000):
            i += 1
    end_time = time.time() #timer ends
    total_time = int(end_time - start_time)
    print("It took {} seconds to compute the result".format(total_time))
    return result

# Testing
int1 = 45628
int2 = 12648
result = addition(int1, int2)
print("The result of adding {} and {} is: {}".format(int1, int2, result))