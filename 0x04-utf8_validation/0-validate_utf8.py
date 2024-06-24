#!/usr/bin/python3
"""This module determines if a given data set represents a
valid UTF-8 encoding """


def validUTF8(data):
    """a method that determines if a given data set represents
    a valid UTF-8 encoding"""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Mask to keep only the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Check the number of leading 1's to determine
            # the number of bytes in the character
            if (byte & mask1) == 0:
                # 1-byte character
                num_bytes = 0
            elif (byte & (mask1 | mask2)) == mask1:
                # Invalid pattern (10xxxxxx)
                return False
            elif (byte & (mask1 | mask2)) == (mask1 | mask2):
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte & (mask1 | mask2 | (1 << 5))) == (
                mask1 | mask2 | (1 << 5)
            ):
                num_bytes = 2
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (
                mask1 | mask2 | (1 << 5) | (1 << 4)
            ):
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid leading byte
                return False
        else:
            # Continuation byte (10xxxxxx)
            if (byte & (mask1 | mask2)) != mask1:
                return False
            num_bytes -= 1

    # All characters should be completely processed
    return num_bytes == 0
