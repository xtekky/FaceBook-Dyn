import re, json

html_content = open("meta.html").read() 

pattern = r'data-content-len="\d+" data-sjs>(.*?)<\/script>'

contents = re.findall(pattern, html_content)
module_list = []

for match in contents:
    # if 'rsrcMap' in match:
    #     json_data = json.loads(match)
    #     modules = json_data['require'][0][3][0]['rsrcMap']
        
    #     for key in modules.keys():
    #         key = (modules[key]['p'])
    #         key = int(key[1:])
            
    #         module_list.append(key)
    
    if 'ScheduledServerJS' in match:
        json_data = json.loads(match)
        
        bbox_list = json_data['require'][0][3]
        for bbox in bbox_list:
            if bbox['__bbox'].get("define"):
                for module in bbox['__bbox']['define']:
                    if module[3] != -1:
                        print(module[3])
                        module_list.append(module[3])


g = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"

# Initializing the module list representation and cache
modules = module_list
compressed_cache = None

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

print(to_compressed_string())