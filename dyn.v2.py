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

_1 = [0] * 999999
_2 = None

for module_number in module_list:
    _1[module_number] = 1

def toString():
    a = []
    for b in range(len(_1)):
        a.append(1 if _1[b] else 0)
    return i("".join(map(str, a))) if len(a) else ""

def h(a):
    a = bin(a)[2:]
    b = "0" * (len(a) - 1)
    return b + a

def i(a):
    a = (a + "00000")
    a = [a[i:i+6] for i in range(0, len(a), 6)]
    b = ""
    for c in range(len(a)):
        b += g[int(a[c], 2)]
    return b

def toCompressedString():
    global _2
    
    if len(_1) == 0:
        return ""
    if _2 is not None:
        return _2

    a = []
    b = 1
    c = _1[0] if _1[0] else 0
    d = bin(c)[2:]

    for e in range(1, len(_1)):
        f = _1[e] if _1[e] else 0
        if f == c:
            b += 1
        else:
            a.append(h(b))
            c = f
            b = 1

    if b:
        a.append(h(b))

    _2 = i(d + "".join(a))
    return _2

# let a = "0001111000010011101110000101101000000101011010000101111000000101110010001011100000101110100101100100010000000011000101100001011110000001000011100000001000100110001110100000110110100000110000100000110001100000001001101010000010110110000000010010010110000011100010000100011000000000100101111110011010000001001110100000000110000101100000001100001110000000100010101000000110011110001100100000000101110000100001000110000001011111100000001001010110000001111100100000100101010000001010011000000110100110000000110000011000000010011100100000001010110010001111101110000000101000111000010011100000101010100011101000000010011100100000100000100000110001100000101110100000101011100000001000111011100000010111001000000010101111100001111110000000010010110110000010110110000011011010001010100011011000000001000001101000000010111101100000011011111000001101111000001100011000000001000101101000000110110010000001101001111000000101010110000000010010000110000111101000001011101000010111111000111110000100001"
# print(i(a))

print(toCompressedString(), "| python")
