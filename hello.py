from PIL import GifImagePlugin
import PIL,os
from PIL import Image, ImageDraw, ImageSequence
test = Image.open('test1.gif')
test2 = Image.open('./py/face/face_1.png').convert("RGBA").resize(test.size)
mask = Image.new("L", test.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((140, 50, 260, 170), fill=255)
test3 = Image.composite(test,test2,mask)
test3.save('test.gif', save_all=True, append_images = [test, test2])




gif = Image.open('test1.gif')
#frames = []
tst = []
i = 0
if gif.format == 'GIF' and gif.is_animated:
    for frame in ImageSequence.Iterator(gif):
        frame.save('./buffer/'+ str(i)+'.png')
        i = i + 1
        tst.append(frame)
#img1 = Image.new("L", test.size,0)
#img1.save("test2.gif", save_all=True, append_images = [tst[1]])
#print(tst)
r = []
for b in range (0, len(list(os.listdir('./buffer/')))):
    r.append( Image.open('./buffer/'+str(b)+'.png') )
    r[b] = Image.alpha_composite(r[b].convert("RGBA"),test2)
    
r[0].save("test2.gif",save_all=True, append_images = r[1:],loop=0,optimized = True,duration = 40)