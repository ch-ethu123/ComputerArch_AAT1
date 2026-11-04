'''
Write a Python program to perform and verify the results of the following shift operations on 8-bit binary numbers:
a) Logical left shift of 1111110110 by 2 positions.
b) Logical right shift of 10010100 by 2 positions.
For each operation, display the original 8-bit binary number, demonstrate the shifting process step by step, 
and display the final 8-bit binary result. 
Verify the program output against the results obtained through manual calculations. 
Ensure that the output remains in 8-bit format.
'''
def logical_left_shift(binary, positions):
    print("\nLogical Left Shift")
    print("Original:", binary)

    for i in range(positions):
        binary = binary[1:] + '0'
        print("Step", i + 1, ":", binary)

    print("Final Result:", binary)


def logical_right_shift(binary, positions):
    print("\nLogical Right Shift")
    print("Original:", binary)

    for i in range(positions):
        binary = '0' + binary[:-1]
        print("Step", i + 1, ":", binary)

    print("Final Result:", binary)


# (a) Logical Left Shift
logical_left_shift("11110110", 2)

# (b) Logical Right Shift
logical_right_shift("10010100", 2)
