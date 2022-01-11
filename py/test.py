from PIL import Image
import pathlib
import os
import random
import binascii

pathlib.Path().absolute()

i = 0
s = 0
while i <=100:
    
    i = i + 1
#####################
# heads accessory

    head_accessory_list = list(os.listdir('./py/head_accessory/'))

# delete ds_store
    if '.DS_Store' in head_accessory_list:
        head_accessory_list.pop(head_accessory_list.index('.DS_Store'))
    

    head_accessory_name = head_accessory_list[random.randrange(0,len(head_accessory_list))]
    head_accessory = Image.open('./py/head_accessory/'+head_accessory_name).convert("RGBA")
    
#####################


#####################
# hairs 

    hair_list = list(os.listdir('./py/hair/'))

# delete ds_store
    if '.DS_Store' in hair_list:
        hair_list.pop(hair_list.index('.DS_Store'))
    

    hair_name = hair_list[random.randrange(0,len(hair_list))]
    hair = Image.open('./py/hair/'+hair_name).convert("RGBA")
    
#####################


    hA_h = Image.alpha_composite(hair,head_accessory)

#####################
# face
    face_list = list(os.listdir('./py/face/'))

# delete ds_store
    if '.DS_Store' in face_list:
        face_list.pop(face_list.index('.DS_Store'))
    

    face_name = face_list[random.randrange(0,len(face_list))]
    face = Image.open('./py/face/'+face_name).convert("RGBA")
    
####################

    hA_h_f = Image.alpha_composite(face,hA_h)

    ####################
    # faces accessory
    face_accessory_list = list(os.listdir('./py/face_accessory/'))

    # delete ds_store
    if '.DS_Store' in face_accessory_list:
        face_accessory_list.pop(face_accessory_list.index('.DS_Store'))
        

    face_accessory_name = face_accessory_list[random.randrange(0,len(face_accessory_list))]
    face_accessory = Image.open('./py/face_accessory/'+face_accessory_name).convert("RGBA")
        
    ####################

    hA_h_f_fA = Image.alpha_composite(hA_h_f,face_accessory)
    ####################
    # clothes
    clothes_list = list(os.listdir('./py/clothes/'))

    # delete ds_store
    if '.DS_Store' in clothes_list:
        clothes_list.pop(clothes_list.index('.DS_Store'))
        

    clothes_name = clothes_list[random.randrange(0,len(clothes_list))]
    clothes = Image.open('./py/clothes/'+clothes_name).convert("RGBA")
        
    ####################

    hA_h_f_fA_c = Image.alpha_composite(hA_h_f_fA, clothes)

    ####################
    # accessory
    accessory_list = list(os.listdir('./py/accessory/'))

    # delete ds_store
    if '.DS_Store' in accessory_list:
        accessory_list.pop(accessory_list.index('.DS_Store'))
        

    accessory_name = accessory_list[random.randrange(0,len(accessory_list))]
    accessory = Image.open('./py/accessory/'+accessory_name).convert("RGBA")
        
    ####################
    hA_h_f_fA_c_a = Image.alpha_composite(hA_h_f_fA_c,accessory)

    final_name = head_accessory_name+'...'+ hair_name+'...' + face_name+'...' + face_accessory_name+'...' + clothes_name+'...' + accessory_name

    sequ = open('./py/py/seq', 'r')
    seque = sequ.read()
    sequ.close()
    print(seque)
    
    print(final_name+"    "+seque)
    

    
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
    if final_name in list_bd:
        i = i -1
        s = s + 1
        if s > 1000:
            print('не удалось подобрать комбинацию')
            break 
    if final_name not in list_bd:
        hA_h_f_fA_c_a.save('./py/py/'+seque+'.png')
        sequ = open('./py/py/seq', 'w')
        less = int(seque) + 1
        sequ.write(str(less))
        sequ.close()
        file = open('./py/py/bd.txt', 'a')
        file.write('\n'+final_name)
        file.close
        
    

    
#img1 = Image.open('./py/py/first.png').convert("RGBA")
#img2 = Image.open('./py/py/second.png').convert("RGBA")


#intermediate = Image.alpha_composite(img1, img2)

#img3 = Image.open('./py/py/last.png').convert("RGBA")

#final = Image.alpha_composite(intermediate, img3)


#final.save('./py/py/final.png')
