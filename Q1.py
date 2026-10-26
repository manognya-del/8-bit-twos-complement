# Signed Binary Arithmetic using 8-bit 2's Complement

def to_binary(n):
    return format(n & 0xFF, '08b')


def from_binary(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def subtract(a, b):
    # Perform subtraction using 2's complement
    binary_a = to_binary(a)
    binary_b = to_binary(b)

    # Find 2's complement of the second operand
    complement_b = to_binary(~b + 1)

    # Perform 8-bit binary addition
    result_unsigned = int(binary_a, 2) + int(complement_b, 2)
    result_binary = format(result_unsigned & 0xFF, '08b')
    result_decimal = from_binary(result_binary)

    # Check signed arithmetic overflow
    overflow = result_decimal != (a - b)

    print("First Operand  :", binary_a, "(", a, ")")
    print("Second Operand :", binary_b, "(", b, ")")
    print("2's Complement :", complement_b)
    print("Result Binary  :", result_binary)
    print("Result Decimal :", result_decimal)
    print("Overflow       :", "Yes" if overflow else "No")
    print("-" * 40)


# (a) 45 - (+19)
print("(a) 45 - (+19)")
subtract(45, 19)

# (b) (-35) - (-12)
print("(b) (-35) - (-12)")
subtract(-35, -12)