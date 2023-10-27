class ParityBitPython:
    @staticmethod
    def validate_client_number(client_number: str) -> bool:
        # Check if the client number is of length 10
        if len(client_number) != 10:
            return False

        # Check if the client number contains only digits
        if not client_number.isdigit():
            return False

        # Convert the client number to binary
        binary_representation = bin(int(client_number))[2:]

        # Count the number of "1"s in the binary representation
        ones_count = binary_representation.count('1')

        # Return True if the number of "1"s is even, otherwise return False
        return ones_count % 2 == 0


# Tests for the given scenarios
def test_parity_bit_python():
    # Valid client number
    assert ParityBitPython.validate_client_number("8456894318") == True
    # Invalid client number
    assert ParityBitPython.validate_client_number("3456848879") == False
    # Client number with non-digit character
    assert ParityBitPython.validate_client_number("34568488a9") == False
    # Client number with wrong length
    assert ParityBitPython.validate_client_number("34568488") == False
    # Another valid client number
    assert ParityBitPython.validate_client_number("0000000000") == True  # 0 in binary has even number of "1"s (0)

    print("All tests passed!")