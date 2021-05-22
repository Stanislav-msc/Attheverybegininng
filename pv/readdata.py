def dff(filename=None):
    '''reture list of tuples from file .tabsv'''
    if filename==None:
        filename='data.xls'
    data=[]
    with open(filename, 'r') as fi:
        #n=0
        for l in fi:
            row=l.split()
            x,y,p=int(row[0]),int(row[1]),int(row[2])
            data.append((x,y,p))
            #print (n,data[n][0],data[n][1],data[n][2])
            #n=n+1
    return data

def sortxy(dataxyz):
    '''sort list of tuples by y value'''
    "data=sorted(sorted(set(datain),key=lambda x: x[0]),key=lambda y: y[1])"
    dataset=set(dataxyz)
    data1=sorted(dataset,key=lambda x: x[0])
    data=sorted(data1,key=lambda y: y[1])
    return data
