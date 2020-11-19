"""
Author: John Schulz
Date: 11/17/2020
Project: Logic Gate Delayed Neural Network (LGDNN)
Description: Utilize Logic-Gates to create a network to solve different logic gates.

Neural Architecture: 2 input nodes, 2 hidden layers, 1 output node.
Output Type: Boolean Output
Input Type: Boolean Input

Results:
* Successfully forwardly computes: AND, OR, NOR, XNOR, NAND, XOR
"""


import numpy as np
import logic
bool = logic.bool()

# --------------------------- User Vars ------------------------------
max_delay = 1  # Max Delay

# --------------------------- Inputs ---------------------------------
input = np.array([[False, False], [False, True], [True, False], [True, True]])

# ----------------------  Output Solutions ---------------------------
and_table = np.array([False, False, False, True])
nand_table = np.array([True, True, True, False])
or_table = np.array([False, True, True, True])
xor_table = np.array([False, True, True, False])
xnor_table = np.array([True, False, False, True])
nor_table = np.array([True, False, False, False])


# Generate Random Delays
d1 = np.random.randint(0, max_delay+1, size=6)
d2 = np.random.randint(0, max_delay+1, size=9)
d3 = np.random.randint(0, max_delay+1, size=3)
d4 = np.random.randint(0, max_delay+1, size=1)




def forward_prop(input, d1, d2, d3, d4):

    s0 = input
    s1 = np.array([False, False, False])
    s2 = np.array([False, False, False])
    s3 = np.array([False])

    for tick in range(0, d4[0]+1):

        # Input --> Hidden Layer 1
        s1[0] = bool.OR(np.logical_and(d1[0:2] <= tick, s0))
        s1[1] = bool.NOR(np.logical_and(d1[2:4] <= tick, s0))
        s1[2] = bool.OR(np.logical_and(d1[4:6] <= tick, s0))

        # Hidden Layer 1 --> Hidden Layer 2
        s2[0] = bool.NOR(np.logical_and(d2[0:3] <= tick, s1))
        s2[1] = bool.OR(np.logical_and(d2[3:6] <= tick, s1))
        s2[2] = bool.NOR(np.logical_and(d2[6:9] <= tick, s1))

        # Hidden Layer 2 --> Output
        s3[0] = bool.XNOR(np.logical_and(d3 <= tick, s2))

    return s3[0]

# Guess for a solution
def rand_find_solution(input_table, max_delay):

    # Init Var
    output = np.array([False, False, False, False])

    # Keep searching until solution found
    while not(np.array_equal(input_table, output)):

        # Generate Random Delays
        d1 = np.random.randint(0, max_delay+1, size=6)
        d2 = np.random.randint(0, max_delay+1, size=9)
        d3 = np.random.randint(0, max_delay+1, size=3)
        d4 = np.random.randint(0, max_delay+1, size=1)

        for index in range(0, 4):
            output[index] = forward_prop(input[index, :], d1, d2, d3, d4)

    # Print solution
    if np.array_equal(input_table, output):
        print(d1, d2, d3, d4)

        for index in range(0, 4):
            print(forward_prop(input[index, :], d1, d2, d3, d4))


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
print(d1, d2, d3, d4)

for index in range(0, 4):
    print(forward_prop(input[index, :], d1, d2, d3, d4))
"""
