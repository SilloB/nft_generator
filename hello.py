import os
from PIL import Image, ImageSequence
gif = Image.open('test1.gif')
test2 = Image.open('./py/face/face_1.png').convert("RGBA").resize(gif.size)
i = 0
if gif.format == 'GIF' and gif.is_animated:
    for frame in ImageSequence.Iterator(gif):
        frame.save('./buffer/'+ str(i)+'.png')
        i = i + 1
r = []
for b in range (0, len(list(os.listdir('./buffer/')))):
    r.append( Image.open('./buffer/'+str(b)+'.png') )
    r[b] = Image.alpha_composite(r[b].convert("RGBA"),test2)
r[0].save("test2.gif",save_all=True, append_images = r[1:],loop=0,optimized = True,duration = 40)