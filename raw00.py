""" this file create bmp file from numbers or table """

bmpw=256
bmph=256
colorspace="colorful"
filename="images\create15"

from createbmp import createbmp
from bytetools import byencdltl
from readdata import dff, sortxy

from random import getrandbits
from math import sin, cos, sqrt, exp, expm1


#data=dff()
datain=[]
R=64
for tl in range(628):
    t=tl/100
    x,y=R*sin(t)+256,R*cos(t)+256
    rd=(int(x),int(y),255)
    datain.append(rd)

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
        #bmprow+=3*byencdltl(s4,int(1))
        #print (nl,s4)
print (f'{len(bmprow)=}')
createbmp(bmprow,filename,bmpw=bmpw,bmph=bmph)
