# Tutorial 2 | Simple Convertors
# Example 1
a_int = 3
b_int = 2

c_float_sum = float(a_int+b_int) # Adds integer values in a_int and b_int and converts them into a float sum

# Practice 1i
binary_base2 = "1001"
float_base2 = float(int(binary_base2,2))
print (float_base2)

# Practice 2 Binary 10101010(int).0101(float) into decimal number
binary_int = "10101010"
binary_float = "0101"

float_int = float(int(binary_int,2))
float_float = float(int(binary_float,2))
final_float = float_int + (float_float / 10)
print ("Binary 10101010.0101 in Float is =", final_float)

# Practice 2 Octal 
# Convert the Octals 6.6 66.66 666.666 and 6666.6666 into Float
# Hint = an octal is a base 8 number

# Octal 6.6 float
octal_int = "6"
octal_float = "6"
octalfloat_int = float(int(octal_int, 8))
octalfloat_dec = float(int(octal_float, 8))
final_octal = octalfloat_int + (octalfloat_dec / 10)
print ("Octal 6.6 in Float is =", final_octal)

# Octal 66.66 float
octal_int66 = "66"
octal_float66 = "66"
octalfloat_int66 = float(int(octal_int66, 8))
octalfloat_dec66 = float(int(octal_float66, 8))
final_octal66 = octalfloat_int66 + (octalfloat_dec66 / 100)
print ("Octal 66.66 in Float is =", final_octal66)

# Hexadecimal
hex_1 = eval ('0xdeadbeea')
print ("Hexadecimal 0xdeadbeea into int", hex_1)

# Further research on this topic is required...
