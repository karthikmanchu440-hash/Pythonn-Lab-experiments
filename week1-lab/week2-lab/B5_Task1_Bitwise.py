# B5_Task1_Bitwise.py
# Lab Task B5: Bitwise Operators

p = 12  # Binary: 1100
q = 10  # Binary: 1010

print("bin(p):", bin(p))
print("bin(q):", bin(q))

# AND: bits are 1 if both corresponding bits are 1
# 1100 & 1010 = 1000 (8 in decimal)
print("p & q :", p & q)

# OR: bits are 1 if either corresponding bit is 1
# 1100 | 1010 = 1110 (14 in decimal)
print("p | q :", p | q)

# XOR: bits are 1 if corresponding bits are different
# 1100 ^ 1010 = 0110 (6 in decimal)
print("p ^ q :", p ^ q)

# NOT: inverts the bits. Formula is ~x = -(x + 1)
# ~12 = -13
print("~p    :", ~p)

# Left Shift: shifts bits to the left by 2 positions
# 1100 << 2 = 110000 (48 in decimal)
print("p << 2:", p << 2)

# Right Shift: shifts bits to the right by 2 positions
# 1100 >> 2 = 11 (3 in decimal)
print("p >> 2:", p >> 2)
