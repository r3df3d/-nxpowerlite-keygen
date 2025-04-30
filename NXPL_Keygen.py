# NXPowerLite Keygen by redfed
# https://github.com/r3df3d

import random
import hashlib

CHARSET = '3V8W4M56F9ABZUCKDSEYG2HJLN7PQRTX'

def buffer_to_binary(value):
    """Converts a byte value (0-255) to a list of 8 binary bits."""
    return [(value >> i) & 1 for i in reversed(range(8))]

def generate_reg_code():
    # Step 1: Generate 8 random bytes with specific constraints
    arr1 = [random.randint(0, 255) for _ in range(8)]
    arr1[0] = 0xFF
    arr1[2] = 3
    arr1[7] &= 0xFE

    # Step 2: Compute MD5 hash
    md5 = hashlib.md5(bytes(arr1)).digest()

    # Step 3: XOR hash[8..15] with hash[0..7]
    arr2 = [md5[i + 8] ^ md5[i] for i in range(8)]

    # Step 4: Convert each byte in arr1 and arr2 to binary and store in arr3 and arr4
    arr3 = [bit for byte in arr1 for bit in buffer_to_binary(byte)]
    arr4 = [bit for byte in arr2 for bit in buffer_to_binary(byte)]

    # Step 5: Interleave arr3 and arr4 to form arr6 (128 bits)
    arr6 = []
    for i in range(64):
        arr6.append(arr3[i])
        arr6.append(arr4[i])

    # Step 6: Convert every 5 bits into a character from CHARSET (25 characters total)
    result = ''
    n = 0
    for _ in range(25):
        k = 0
        l = 1
        n += 5
        m = n
        for _ in range(5):
            m -= 1
            k += l * arr6[m]
            l *= 2
        result += CHARSET[k]

    # Step 7: Insert hyphens for final format XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
    formatted_result = (
        result[:5] + '-' +
        result[5:10] + '-' +
        result[10:15] + '-' +
        result[15:20] + '-' +
        result[20:25]
    )

    return formatted_result

# Display with styling using ANSI escape codes
BOLD = '\033[1m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

print(CYAN + BOLD + "\n==============================")
print(" NXPowerLite Keygen by redfed")
print(" GitHub: https://github.com/r3df3d")
print("==============================" + RESET)

print(GREEN + BOLD + "\n[ License Key ]")
print("  " + generate_reg_code())
print(RESET)
