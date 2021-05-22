
from bytetools import byencdltl#, byrevrs
def CLUT(choice=None):
    """return bytes for GLUT of given choice:
    grey\n\ttruecolor\n\tcolorbw\n\tcolorscale"""
    if choice==None:
        return b''
    t=bytearray()
    #print(f"{t.__class__= }")
    if choice=="grey":
        for c in range(256):
            t+=3*byencdltl(c,1)
            t+=(b'\x00')
    if choice=="color":
        for c in range(0,256,4):
            t+=(b'\x00')
            t+=byencdltl(c,1)
            t+=(b'\xff')
            t+=(b'\x00')
        for c in range(255,0,-4):
            t+=(b'\x00')
            t+=(b'\xff')
            t+=byencdltl(c,1)
            t+=(b'\x00')
        for c in range(0,256,4):
            t+=byencdltl(c,1)
            t+=(b'\xff')
            t+=(b'\x00')
            t+=(b'\x00')
        for c in range(255,0,-4):
            t+=(b'\xff')
            t+=byencdltl(c,1)
            t+=(b'\x00')
            t+=(b'\x00')
    if choice=="colorbw":
        t+=4*(b'\xff')
        for c in range(0,256,4):
            t+=(b'\x00')
            t+=byencdltl(c,1)
            t+=(b'\xff')
            t+=(b'\x00')
        for c in range(251,0,-4):
            t+=(b'\x00')
            t+=(b'\xff')
            t+=byencdltl(c,1)
            t+=(b'\x00')
        for c in range(0,256,4):
            t+=byencdltl(c,1)
            t+=(b'\xff')
            t+=(b'\x00')
            t+=(b'\x00')
        for c in range(251,0,-4):
            t+=(b'\xff')
            t+=byencdltl(c,1)
            t+=(b'\x00')
            t+=(b'\x00')
        t+=4*(b'\x00')
    if choice=="colorful":
        for c in range(0,256,6):
            t+=byencdltl(c,1)
            t+=(b'\x00')
            t+=(b'\x00')
            t+=(b'\x00')
        for c in range(5,256,6):
            t+=(b'\xff')
            t+=byencdltl(c,1)
            t+=(b'\x00')
            t+=(b'\x00')
        for c in range(251,0,-6):
            t+=byencdltl(c,1)
            t+=(b'\xff')
            t+=(b'\x00')
            t+=(b'\x00')
        for c in range(0,256,6):
            t+=(b'\x00')
            t+=(b'\xff')
            t+=byencdltl(c,1)
            t+=(b'\x00')
        for c in range(251,0,-6):
            t+=(b'\x00')
            t+=byencdltl(c,1)
            t+=(b'\xff')
            t+=(b'\x00')
        for c in range(0,255,6):
            t+=2*byencdltl(c,1)
            t+=(b'\xff')
            t+=(b'\x00')
        t+=4*(b'\xff')
    return bytes(t)
if __name__ == "__main__":
    # execute only if run as a script
    print (len(CLUT("colorful")))
    print (CLUT("colorful")[168:180])
    print (CLUT("colorful")[336:348])
    print (CLUT("colorful")[676:688])
    print (CLUT("colorful")[848:868])
    print (CLUT("colorful")[1020:1028])#.__doc__)
    print (CLUT(), len(CLUT()))
