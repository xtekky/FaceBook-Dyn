import re, json

html_content = open("meta.html").read() 

pattern = r'data-content-len="\d+" data-sjs>(.*?)<\/script>'

contents = re.findall(pattern, html_content)
module_list = []

for match in contents:
    if 'rsrcMap' in match:
        json_data = json.loads(match)
        modules = json_data['require'][0][3][0]['rsrcMap']
        
        for key in modules.keys():
            key = (modules[key]['p'])
            key = int(key[1:])
            
            module_list.append(key)
    
    # if 'ScheduledServerJS' in match:
    #     json_data = json.loads(match)
        
    #     bbox_list = json_data['require'][0][3]
    #     for bbox in bbox_list:
    #         if bbox['__bbox'].get("define"):
    #             for module in bbox['__bbox']['define']:
    #                 if module[3] != -1:
    #                     print(module[3])
    #                     module_list.append(module[3])


g = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
_1 = [ None for _ in range(9999999)]
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

print(toCompressedString())