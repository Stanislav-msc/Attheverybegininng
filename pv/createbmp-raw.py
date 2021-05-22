""" this file create bmp rgb file """

from bytetools import *
''' writing colors pallete -- color lookup table (CLUT)'''
from CLUTs import CLUT
imagewidth=512
imageheigth=512

def createbmp(bmprow, filename="create13", colorspace="colorful",bmpw=512,bmph=512):

    pallete=CLUT(colorspace)

    filename=filename+'.bmp'

    head=b'BM'
    res4=b'\x00\x00\x00\x00'
    offset=len(pallete)+54
    dibsize=b'\x28\x00\x00\x00' #dibsize=40
    if bmpw!=imagewidth or bmph!=imageheigth:
         print (f"something wrong {bmpw=} and {bmph=}")#bitmap width: 4 bytes little signed
         #bitmap heigh: 4 bytes little signed
    NCP=1 #number of color planes: 2 bytes signed
    if len(pallete)==0:
        bpp=24
    else:
        bpp=8 #bits per pixel: 2 bytes ... bd: 24 but maybe 1,2,4,8,16,24,32
    compression=0 #no compression: 4 from_bytes
    hdpm=2835 #4 bytes for pixel per meter resolution
    vdpm=2835 #4 bytes 2835 is equal to 72dpi
    cpalette=0 #4 bytes: the number of colors in the color palette, or 0 to default to 2^n
    NIC=0 #4 byets for number of important colors

    from math import ceil, floor
    #rsf=4*ceil(bpp*bmpw/32) #rowsize
    #rsc=4*floor((bpp*bmpw+31)/32) #rowsize
    rs=4*ceil(bpp*bmpw/32) #rowsize
    #print ("rowsize=", rs)
    bmprsize=rs*bmph
    if bmprsize!=len(bmprow):
        print (f"something wrong {bmprsize=} and {len(bmprow)=}")
    filesize=bmprsize+offset

    fout=open(filename,'wb')
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
    fout.write(byencdltl(cpalette,4))
    fout.write(byencdltl(NIC,4))
    fout.write(pallete)
    fout.write(bmprow)
    fout.close()

#print (fout.tell(), offset)
from random import getrandbits
#s4=getrandbits(rs*8)
#print ("bmprsize=", bmprsize)
#print(s4,byencdltl(s4,int(bmprsize/8)))
from readdata import dff, sortxy
#data=dff()
datain=[]
from math import sin, cos, sqrt, exp, expm1
R=64
for tl in range(628):
    t=tl/100
    x,y=R*sin(t)+256,R*cos(t)+256
    rd=(int(x),int(y),255)
    datain.append(rd)

data=sorted(sorted(set(datain),key=lambda x: x[0]),key=lambda y: y[1])#sortxy(datain)

en=len(data)
#nl=0
cx,cy=int(imagewidth/2),int(imageheigth/2)
print(cx,cy)
sgm=4

bmprow=b''
for r in range(imageheigth):
    #print (f'{r}\t{int(r/512*100)}%')
    print (f'{r}\t{int(r/512*100)}%', sep='; ')
    for p in range(imagewidth):
        s4=255#2**24-1#getrandbits(24)
        for d in data:
            '''x,y,s=d[0],d[1],d[2]
            if ((p-x)**2+(r-y)**2)<16:
                 #nl<(en-1):
                 s4=255-d[2]
            #print (p,r,s4, data[nl][0],data[nl][1],data[nl][2])
            #nl+=1
            #else:
            #s4=255'''
        v=((p-cx)**2+(r-cy)**2)**.5
        dpf=255*exp(-((v-R)/4/sgm)**2)#*(1/(sgm*sqrt(6.2831853)))
        s4=255-int(dpf)
        #print (p,r,v,s4,dpf)
        bmprow+=1*byencdltl(s4,int(1))
        #fout.write(1*byencdltl(s4,int(1)))
        #print (nl,s4)
print (f'{len(bmprow)=}')
createbmp(bmprow,"create14")
