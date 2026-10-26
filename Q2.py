# Rotate Left Operations on 8-bit Binary Numbers

def rotate_left_without_carry(binary, positions):
    print("\nRotate Left Without Carry (ROL)")
    print("Original Binary:", binary)

    for i in range(positions):
        binary = binary[1:] + binary[0]
        print("Step", i + 1, ":", binary)

    print("Final Result:", binary)


def rotate_left_with_carry(binary, carry, positions):
    print("\nRotate Left With Carry (RCL)")
    print("Original Binary:", binary)
    print("Initial Carry:", carry)

    for i in range(positions):
        new_carry = binary[0]
        binary = binary[1:] + carry
        carry = new_carry

        print("Step", i + 1, ":", binary, "| Carry:", carry)

    print("Final Result:", binary)
    print("Final Carry:", carry)


# Given 8-bit binary number
number = "10110110"

# (a) Rotate left without carry by 2 positions
rotate_left_without_carry(number, 2)

# (b) Rotate left with carry by 2 positions
initial_carry = "0"
rotate_left_with_carry(number, initial_carry, 2)