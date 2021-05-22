""" this file create bmp rgb file """

def byrevrs(bytesstring):
    """reverse order of array in bytes"""
    fsa=bytearray(bytesstring)
    fsr=b''
    for i in range(len(fsa)):
        n=('%x' % fsa.pop())
        fsr=fsr+bytes.fromhex(n.zfill(2))
    return fsr

def byencdltl(intnumber, b):
    '''convert number in bytestring lenght of b with byteorder=little'''
    hstr=('%x' % intnumber)
    bstr=bytes.fromhex(hstr.zfill(2*b))
    bsr=byrevrs(bstr)
    return bsr

head=b'BM'
filesize="calculate later 4 bytes byteorder=little"
res4=b'\x00\x00\x00\x00'
offset=54#b'6\x00\x00\x00' #offset=54
dibsize=b'\x28\x00\x00\x00' #dibsize=40
bmpw=512 #bitmap width: 4 bytes little signed
bmph=512#bitmap heigh: 4 bytes little signed
NCP=1 #number of color planes: 2 bytes signed
bpp=24 #bits per pixel: 2 bytes ... bd: 24 but maybe 1,2,4,8,16,24,32
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
#print (fout.tell(), offset)
from random import getrandbits
#s4=getrandbits(rs*8)
print ("bmprsize=", bmprsize)
#print(s4,byencdltl(s4,int(bmprsize/8)))
from readdata import dff, sortxy
#data=dff()
datain=[]
from math import sin, cos, sqrt, exp, expm1
R=128
for tl in range(628):
    t=tl/100
    x,y=R*sin(t)+256,R*cos(t)+256
    rd=(int(x),int(y),255)
    datain.append(rd)

data=sorted(sorted(set(datain),key=lambda x: x[0]),key=lambda y: y[1])#sortxy(datain)

en=len(data)
nl=0
cx,cy=int(bmpw/2),int(bmph/2)
print(cx,cy)
sgm=1
ampltd=16777215#2**24-1

for r in range(bmph):
    for p in range(bmpw):
        v=((p-cx)**2+(r-cy)**2)**.5
        dpf=ampltd*(expm1(-((v-R)/4/sgm)**2)+1)#*(1/(sgm*sqrt(6.2831853)))
        s4=round(dpf)
        #print (p,r,v,byencdltl(s4,int(3)),dpf)
        fout.write(1*byencdltl(s4,int(3)))
        #print (nl,s4)

fout.close()