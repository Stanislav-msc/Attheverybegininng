"""file contains tool to handle bytes for file.write"""

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
