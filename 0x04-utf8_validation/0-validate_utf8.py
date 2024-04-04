#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    A function to determine whether a given dataset represents
    a valid UTF-8 encoding.
    """
    byte_count = 0

    first_bit_mask = 1 << 7
    second_bit_mask = 1 << 6

    for byte in data:

        byte_mask = 1 << 7

        if byte_count == 0:

            while byte_mask & byte:
                byte_count += 1
                byte_mask = byte_mask >> 1

            if byte_count == 0:
                continue

            if byte_count == 1 or byte_count > 4:
                return False

        else:
            if not (byte & first_bit_mask and not (byte & second_bit_mask)):
                return False

        byte_count -= 1

    if byte_count == 0:
        return True

    return False
