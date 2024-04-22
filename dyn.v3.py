module_list = module_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    29,
    30,
    31,
    32,
    33,
    34,
    36,
    40,
    42,
    45,
    46,
    47,
    48,
    53,
    55,
    56,
    66,
    71,
    75,
    78,
    83,
    86,
    88,
    27273,
    27274,
    27275,
    27276,
    27277,
    27278,
    27279,
    27280,
    27292,
    27330,
    27331,
    27372,
    27389,
    27652,
    27693,
    27707,
    27708,
    27709,
    27710,
    27731,
    28128,
    28190,
    28191,
    28192,
    28228,
    28229,
    28257,
    28260,
    28261,
    28265,
    28273,
    28274,
    28285,
    28290,
    28291,
    28292,
    28303,
    28699,
    28700,
    28701,
    28715,
    28799,
    28908,
    28909,
    29018,
    29658,
    29659,
    30302,
    30396,
    30397,
    30398,
    30478,
    30479,
    30482,
    30500,
    30513,
    30514,
    30515,
    30516,
    30517,
    30518,
    30519,
    30619,
    30620
]




g = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"

# Initializing the module list representation and cache
modules = [0] * 999999
compressed_cache = None

for module_number in module_list:
    modules[module_number] = 1

def to_string():
    """Converts the module list to a binary string."""
    return ''.join('1' if x else '0' for x in modules)

def h(value):
    """Converts a number to a binary string with a padding of zeros."""
    binary = bin(value)[2:]  # Convert to binary and remove '0b'
    return '0' * (len(binary) - 1) + binary

def i(binary_string):
    """Encodes binary string to the custom base64-like encoding."""
    # Append enough zeros to make the length a multiple of 6
    padded_binary = (binary_string + "00000")[:len(binary_string) + (6 - len(binary_string) % 6)]
    # Split into chunks of 6
    chunks = [padded_binary[i:i+6] for i in range(0, len(padded_binary), 6)]
    # Convert each chunk from binary to integer and then to the custom base64 character
    return ''.join(g[int(chunk, 2)] for chunk in chunks if chunk)

def to_compressed_string():
    global compressed_cache

    if not modules:
        return ""
    if compressed_cache is not None:
        return compressed_cache

    result = []
    current_value = modules[0] if len(modules) > 0 else 0
    count = 1
    binary_prefix = bin(current_value)[2:]

    for value in modules[1:]:
        if value == current_value:
            count += 1
        else:
            result.append(h(count))
            current_value = value
            count = 1

    # Append the last count
    if count:
        result.append(h(count))

    # Cache the result
    compressed_cache = i(binary_prefix + ''.join(result))
    return compressed_cache


print(to_compressed_string(), "| python")
print("gTdLExd2pbGiK00qz0gbwBga8gw46wEzi1i0oO3RwzgrFet2F6aw6boS1jwr41Iw2vQ0a2wnm1fix6ce1zg | real")