img="image.bmp"
fi=open(img,'rb')
head=fi.read(2)
print (head, head.hex(" "), head.decode('utf-8'), sep='\n')
print ("\tcurrent position=", fi.tell())
size=int.from_bytes(fi.read(4), byteorder='little')
print ("size=", size,"current position=", fi.tell())
print ("reserved 2+2 bytes: ", fi.read(4).hex('_'),"current position=", fi.tell())

offset= fi.read(4)

print ("the offset=", int.from_bytes(offset, byteorder='little'), '\t', offset.hex('_'), offset, "\tcurrent position=", fi.tell(),sep=' ')

print("DIB header")
print ("dib size=", int.from_bytes(fi.read(4),'little'), "\tcurrent position=", fi.tell())

bmpw=int.from_bytes(fi.read(4),'little', signed=True)

print ("bitmap width=", bmpw, "\tcurrent position=", fi.tell())

bmph=int.from_bytes(fi.read(4), 'little', signed=True)

print ("bitmap height=", bmph, "\tcurrent position=", fi.tell())
print ("num/color planes=", int.from_bytes(fi.read(2),'little', signed=True), "\tcurrent position=", fi.tell())

bpp=int.from_bytes(fi.read(2),'little')

print ("bit per pixel=", bpp, "\tcurrent position=", fi.tell())
print ("compession=", int.from_bytes(fi.read(4),'little'), "\tcurrent position=", fi.tell())

bdata=int.from_bytes(fi.read(4),'little')

print ("bitmap data size in bytes =", bdata, "\tcurrent position=", fi.tell(), fi.tell(), fi.tell()+bdata )
print ("the horizont_resolution of the image dpmetr=", int.from_bytes(fi.read(4),'little', signed=True), "\tcurrent position=", fi.tell())
print ("the vertical_resolution of the image dpmetr=", int.from_bytes(fi.read(4),'little', signed=True), "\tcurrent position=", fi.tell())
print ("the number of colors in the color palette, or 0 to default to 2^n=", int.from_bytes(fi.read(4),'little', signed=True), "\tcurrent position=", fi.tell())
print ("the number of important colors", int.from_bytes(fi.read(4),'little', signed=True), "\tcurrent position=", fi.tell())

from math import floor, ceil
rsf=4*ceil(bpp*bmpw/32) #rowsize
rsc=4*floor((bpp*bmpw+31)/32) #rowsize
rs=rsf
print ("rowsize=",rsf, rsc, rs)

fout=open('data.txt', 'w')
fout.write("x\ty\tp\n")
data=[]
for y in range(bmph):
    for x in range(bmpw):
        R, GB=fi.read(1),fi.read(2)
        shadow=int.from_bytes(R, 'little')
        if shadow<127:
            p=255-shadow#255:
            xyp=(x,y,p)
            data.append(xyp)
            row=f'{x}\t{y}\t{p}\n'
            print (row)
            fout.write(row)
#print (data)

fout.close()
fi.close()
