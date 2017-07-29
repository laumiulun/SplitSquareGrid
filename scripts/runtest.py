import itertools
import sys

############################################################
#Ask User the corresponding Bound
def AskUSER(xbound):
    num=float(input(xbound))
    return num
############################################################
xmin=AskUSER('X-Min: ')
xmax=AskUSER('X-Max: ')

ymin=AskUSER('Y-Min: ')
ymax=AskUSER('Y-Max: ')

zmin=AskUSER('Z-Min: ')
zmax=AskUSER('Z-Max: ')

##xmin=324547.91
##xmax=346279.17
##
##ymin=4256315.96
##ymax=4271658.24
##
##zmin=-5000
##zmax=2770.56
#Ask User for number of node
numofnode=int(input('Number of Node: '))


# Create list of number each limit
xlist=[]
for i in range(numofnode):
    xlist.append([])
    xincr=(xmax-xmin)/(numofnode-1)
    xlist[i]=xmin+i*xincr

ylist=[]
for i in range(numofnode):
    ylist.append([])
    yincr=(ymax-ymin)/(numofnode-1)
    ylist[i]=ymin+i*yincr

zlist=[]
for i in range(numofnode):
    zlist.append([])
    zincr=(zmax-zmin)/(numofnode-1)
    zlist[i]=zmin+i*zincr

# Mix X,Y, and Z together into one combine list
a=[xlist,ylist,zlist]


# Get every combination of the 3 lists
b=list(itertools.product(*a))

# Write to out.txt, and remove commas and brackets
with open('out.txt','w') as f:
    for i in range(len(b)):
        m=str(b[i])
        n=m[1:-1]
        n=n.replace(',',' ')
        f.write(n)
        f.write('\n')

