'''
Develop a Python program to perform signed binary arithmetic using the 16-bit 2's complement representation. 
Use the program to verify the results of the following arithmetic expressions:
a) (24 + (+17))
b) ((-25) + (-18))
For each expression, display the operands in 8-bit 2's complement binary format, perform the binary arithmetic operation, 
and display the final result in both binary and decimal formats. 
Verify the program output against the results obtained through manual binary calculations and identify any arithmetic overflow.
'''


def to_2s_complement(number, bits):
    return format(number & ((1 << bits) - 1), f'0{bits}b')


def binary_addition(a, b):
    print("\nOperand 1 (8-bit):", to_2s_complement(a, 8))
    print("Operand 2 (8-bit):", to_2s_complement(b, 8))

    # Convert operands to 16-bit representation
    bin_a = to_2s_complement(a, 16)
    bin_b = to_2s_complement(b, 16)

    result = a + b

    print("\n16-bit Binary Addition:")
    print("  ", bin_a)
    print("+ ", bin_b)
    print("-" * 21)
    print("  ", to_2s_complement(result, 16))

    print("\nDecimal Result:", result)
    print("Binary Result:", to_2s_complement(result, 16))

    # Check 16-bit signed overflow
    if result < -32768 or result > 32767:
        print("16-bit Overflow: YES")
    else:
        print("16-bit Overflow: NO")


print("Expression (a): 24 + (+17)")
binary_addition(24, 17)

print("\n---------------------------")

print("Expression (b): (-25) + (-18)")
binary_addition(-25, -18)
