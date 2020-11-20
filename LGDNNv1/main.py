"""
Author: John Schulz
Date: 11/17/2020
Project: Logic Gate Delayed Neural Network (LGDNN)
Description: Utilize Logic-Gates to create a network to solve different logic gates.

Neural Architecture: 2 input nodes, 3 hidden layers, 1 output node.
Output Type: Boolean Output
Input Type: Boolean Input

"""


import numpy as np
import logic
bool = logic.bool()

#np.random.seed(seed=1)
# --------------------------- User Vars ------------------------------
max_delay = 1  # Max Delay

# --------------------------- Inputs ---------------------------------
input = np.array([[False, False], [False, True], [True, False], [True, True]])

# ----------------------  Output Solutions ---------------------------
# LOGIC GATES - Single Output Node Test
and_table = np.array([False, False, False, True])
nand_table = np.array([True, True, True, False])
or_table = np.array([False, True, True, True])
xor_table = np.array([False, True, True, False])
xnor_table = np.array([True, False, False, True])
nor_table = np.array([True, False, False, False])


# Generate Random Delays
d1 = np.random.randint(0, max_delay+1, size=6)
d2 = np.random.randint(0, max_delay+1, size=3)
d3 = np.random.randint(0, max_delay+1, size=1)


# Compute Forward Propagation
def forward_prop(input, d1, d2, d3):

    s0 = input
    s1 = np.array([False, False, False])
    s2 = np.array([False, False, False])

    for tick in range(0, d3[0]+1):

        # Input --> Hidden Layer 1
        s1[0] = bool.OR(np.logical_and(d1[0:2] <= tick, s0))
        s1[1] = bool.NOR(np.logical_and(d1[2:4] <= tick, s0))
        s1[2] = bool.OR(np.logical_and(d1[4:6] <= tick, s0))

        # Hidden Layer 1 --> Output
        s2[0] = bool.XNOR(np.logical_and(d2 <= tick, s1))

    return s2[0]

# Guess for a solution
def rand_find_solution(input_table, max_delay):

    # Init Var
    output = np.array([False, False, False, False])

    # Keep searching until solution found
    while not(np.array_equal(input_table, output)):

        # Generate Random Delays
        d1 = np.random.randint(0, max_delay+1, size=6)
        d2 = np.random.randint(0, max_delay+1, size=3)
        d3 = np.random.randint(0, max_delay+1, size=1)

        for index in range(0, 4):
            output[index] = forward_prop(input[index, :], d1, d2, d3)

    # Print solution
    if np.array_equal(input_table, output):
        print(d1, d2, d3)

        for index in range(0, 4):
            print(forward_prop(input[index, :], d1, d2, d3))


# -------------------------- Print Results ----------------------------
print('XNOR:')
rand_find_solution(xnor_table, max_delay)
print('\nNOR')
rand_find_solution(nor_table, max_delay)
print('\nOR')
rand_find_solution(or_table, max_delay)
print('\nNAND')
rand_find_solution(nand_table, max_delay)
print('\nXOR')
rand_find_solution(xor_table, max_delay)
print('\nAND')
rand_find_solution(and_table, max_delay)

"""
print(d1, d2, d3)

for index in range(0, 4):
    print(forward_prop(input[index, :], d1, d2, d3))
"""
