file = open('./py/py/bd.txt', 'r')
list_bd = list()
a = 0
while True:
    line = file.readline()
    if not line:
        break
    line = line.replace('\n','')
    list_bd.insert(a,line)
    a = a +1
    
if 'head_accessory_1.pnghair.pngface.pngface_accessory_1.pngclothes_1.pngaccessory_2.png' in list_bd:
    print('yes')
