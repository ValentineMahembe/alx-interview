#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    bytes_to_follow = 0

    for byte in data:
        # Check if the byte is the start of a new UTF-8 character
        if bytes_to_follow == 0:
            if (byte >> 7) == 0b0:  # 0xxxxxxx
                continue
            elif (byte >> 5) == 0b110:  # 110xxxxx
                bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx
                bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx
                bytes_to_follow = 3
            else:
                return False
        else:
            # Check if the current byte is of form 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            bytes_to_follow -= 1

    # Check if there are remaining bytes_to_follow
    if bytes_to_follow != 0:
        return False

    return True


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
