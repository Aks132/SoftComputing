# Python program to convert decimal to binary

# Function to convert Decimal number
# to Binary number
def decimalToBinary(n):
	return bin(n).replace("0b", "")

# Driver code
if __name__ == '__main__':
	print(decimalToBinary(0))
	print(decimalToBinary(1))
	print(decimalToBinary(2))
    print(decimalToBinary(3))
    print(decimalToBinary(4))
    print(decimalToBinary(5))
    print(decimalToBinary(6))
    print(decimalToBinary(7))
    print(decimalToBinary(8))
    print(decimalToBinary(9))
