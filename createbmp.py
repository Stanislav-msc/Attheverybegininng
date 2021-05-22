""" this file contain function createbmp(bmprow, filename="create", colorspace="colorful",bmpw=512,bmph=512) to create bmpfile from bmprow bytesraw and CLUT from CLUTs module"""

from bytetools import *
''' writing colors pallete -- color lookup table (CLUT)'''
from CLUTs import CLUT
imagewidth=512
imageheigth=512

def createbmp(bmprow, filename="create", colorspace="colorful",bmpw=512,bmph=512):
    '''create and write bmp with custom attributes'''
    pallete=CLUT(colorspace)

    filename=filename+'.bmp'

    head=b'BM'
    res4=b'\x00\x00\x00\x00'
    offset=len(pallete)+54
    dibsize=b'\x28\x00\x00\x00' #dibsize=40
    if bmpw!=imagewidth or bmph!=imageheigth:
         print (f"something wrong? {bmpw=} and {bmph=}")#bitmap width: 4 bytes little signed
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
    #fsd=byencdltl(filesize,4)
    #size=int.from_bytes(fsd, byteorder='little')
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
