""" this file create bmp rgb file """

from bytetools import *
''' writing colors pallete -- color lookup table (CLUT)'''
from CLUTs import CLUT

pallete=CLUT("colorful")
head=b'BM'
filesize="calculate later 4 bytes byteorder=little"
res4=b'\x00\x00\x00\x00'
offset=len(pallete)+54#b'6\x00\x00\x00' #offset=54
dibsize=b'\x28\x00\x00\x00' #dibsize=40
bmpw=512 #bitmap width: 4 bytes little signed
bmph=512#bitmap heigh: 4 bytes little signed
NCP=1 #number of color planes: 2 bytes signed
bpp=8 #bits per pixel: 2 bytes ... bd: 24 but maybe 1,2,4,8,16,24,32
compression=0 #no compression: 4 from_bytes
bmprsize="calculate later 4 bytes"
hdpm=2835 #4 bytes for pixel per meter resolution
vdpm=2835 #4 bytes 2835 is equal to 72dpi
palette=0 #4 bytes: the number of colors in the color palette, or 0 to default to 2^n
NIC=0 #4 byets for number of important colors

from math import ceil, floor
#rsf=4*ceil(bpp*bmpw/32) #rowsize
#rsc=4*floor((bpp*bmpw+31)/32) #rowsize
rs=4*ceil(bpp*bmpw/32) #rowsize
#print ("rowsize=", rs)
bmprsize=rs*bmph
filesize=bmprsize+offset


cimg="create.bmp"
fout=open(cimg,'wb')
fout.write(head)
fs=('%x' % filesize)
#print ("filesize=", filesize,'\n', "fs=", fs)
#fsd=bytes.fromhex(fs.zfill(8))
#print ("fsd=", fsd, "len", len(fsd))

fsd=byencdltl(filesize,4)
size=int.from_bytes(fsd, byteorder='little')
#print ("size=", size,"current position=", fout.tell())
fout.write(byencdltl(filesize,4))
fout.write(res4)
fout.write(byencdltl(offset,4))
fout.write(dibsize)
fout.write(byencdltl(bmpw,4))
fout.write(byencdltl(bmph,4))
fout.write(byencdltl(NCP,2))
fout.write(byencdltl(bpp,2))
fout.write(byencdltl(compression,4))
fout.write(byencdltl(bmprsize,4))
fout.write(byencdltl(hdpm,4))
fout.write(byencdltl(vdpm,4))
fout.write(byencdltl(palette,4))
fout.write(byencdltl(NIC,4))
fout.write(pallete)

#print (fout.tell(), offset)
from random import getrandbits
#s4=getrandbits(rs*8)
#print ("bmprsize=", bmprsize)
#print(s4,byencdltl(s4,int(bmprsize/8)))
from readdata import dff, sortxy
datain=dff(filename="D:\PY\imgrec\data.xls")
#datain=[]
from math import sin, cos, sqrt, exp, expm1
'''R=64
for tl in range(628):
    t=tl/100
    x,y=R*sin(t)+256,R*cos(t)+256
    rd=(int(x),int(y),255)
    datain.append(rd)'''

data=sorted(sorted(set(datain),key=lambda x: x[0]),key=lambda y: y[1])#sortxy(datain)

en=len(data)
#nl=0
cx,cy=int(bmpw/2),int(bmph/2)
print(cx,cy)
sgm=4

bmprow=b''
for r in range(bmph):
    #print (f'{r}\t{int(r/512*100)}%')
    print (f'{r}\t{int(r/512*100)}%', sep='; ')
    for p in range(bmpw):
        s4=255#2**24-1#getrandbits(24)
        for d in data:
            x,y,s=d[0],d[1],d[2]
            delta2=((p-x*8)**2+(r-y*8)**2)
            if delta2<32:
                 #nl<(en-1):
                 s4=255-int(d[2]*(1+expm1(-delta2/16)))
            #print (p,r,s4, data[nl][0],data[nl][1],data[nl][2])
            #nl+=1
            #else:
            #s4=255
        '''v=((p-cx)**2+(r-cy)**2)**.5
        dpf=255*exp(-((v-R)/4/sgm)**2)#*(1/(sgm*sqrt(6.2831853)))
        s4=255-int(dpf)'''
        #print (p,r,v,s4,dpf)
        bmprow+=1*byencdltl(s4,int(1))
        #fout.write(1*byencdltl(s4,int(1)))
        #print (nl,s4)
fout.write(bmprow)
fout.close()
