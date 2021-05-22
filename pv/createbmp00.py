""" this file create bmp rgb file """

head=b'BM'
filesize="calculate later 4 bytes byteorder=little"
res4=b'\x00\x00\x00\x00'
offset=54#b'6\x00\x00\x00' #offset=54
dibsize=b'\x28\x00\x00\x00' #dibsize=40
bmpw=512 #bitmap width: 4 bytes little signed
bmph=512 #bitmap heigh: 4 bytes little signed
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
print ("rowsize=", rs)
bmprsize=rs*bmph
filesize=bmprsize+offset


cimg="create.bmp"
fout=open(cimg,'wb')
fout.write(head)
fs=('%x' % filesize)
print ("filesize=", filesize,'\n', "fs=", fs)
#fsd=bytes.fromhex(fs.zfill(8))
#print ("fsd=", fsd, "len", len(fsd))

def byrevrs(bytesstring):
    fsa=bytearray(bytesstring)
    fsr=b''
    for i in range(len(fsa)):
        n=('%x' % fsa.pop())
        fsr=fsr+bytes.fromhex(n.zfill(2))
    return fsr

def byencdltl(intnumber, b):
    hstr=('%x' % intnumber)
    bstr=bytes.fromhex(hstr.zfill(2*b))
    bsr=byrevrs(bstr)
    return bsr


fsd=byencdltl(filesize,4)
size=int.from_bytes(fsd, byteorder='little')
print ("size=", size,"current position=", fout.tell())
fout.write(byencdltl(filesize,4))
fout.close()
