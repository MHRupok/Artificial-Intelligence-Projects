import numpy as np
from random import randint
from datetime import datetime
import time

nodeMoves     = {}
nodeParent    = {}
parentChild   = {}

solution      = []
goalNode      = []
solutionPath  = []
solutionMove  = []
childNodeList = []
nodeQueue     = []
nodeList      = []


'''         00  01  02
            10  11  12
            20  21  22
        
30 31 32    60  61  62    90   91  92     120 121 122
40 41 42    70  71  72    100  101 102    130 131 132
50 51 52    80  81  82    110  111 112    140 141 142

            150 151 152
            160 161 162
            170 171 172


            W   W   W
    
            W   W   W

            W   W   W

B   B   B   R   R   R   G   G   G   O   O   O

B   B   B   R   R   R   G   G   G   O   O   O

B   B   B   R   R   R   G   G   G   O   O   O

            Y   Y   Y

            Y   Y   Y

            Y   Y   Y          

'''

xInitial= np.array(
    [
                
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],        
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y']

        
        
    ]
)

'''goal = np.array(
[['W','W','R'],
 ['W','W','R'],
 ['Y','Y','G'],
 ['B','B','G'],
 ['B','B','G'],
 ['B','B','O'],
 ['R','R','W'],
 ['R','R','O'],
 ['Y','Y','O'],
 ['R','B','B'],
 ['G','G','W'],
 ['G','G','W'],
 ['Y','O','O'],
 ['R','O','O'],
 ['R','O','O'],
 ['G','G','W'],
 ['Y','Y','W'],
 ['Y','Y','B']]
)'''

goal = np.array(
[       ['G', 'W', 'W'],
        ['O', 'W', 'W'],
        ['B', 'R', 'R'],
        ['O', 'B', 'R'],
        ['O', 'B', 'R'],
        ['W', 'G', 'Y'],        
        ['W', 'G', 'G'],
        ['W', 'R', 'Y'],
        ['O', 'B', 'Y'],
        ['W', 'O', 'O'],
        ['R', 'G', 'G'],
        ['B', 'B', 'Y'],
        ['B', 'B', 'Y'],
        ['W', 'O', 'Y'],
        ['R', 'G', 'G'],
        ['B', 'R', 'R'],
        ['Y', 'Y', 'Y'],
        ['O', 'O', 'G']]
    )
    


def restore_x():
    x[0:18,0:3]=xInitial[0:18,0:3]
    

def Fc(): #move 1
    
    x[6:9,0:3]=np.fliplr(x[6:9,0:3].transpose())    
    temp1=np.array(x[2, 0:3])
    temp2=np.array(x[9:12,0])
    temp3=np.array(x[15,0:3])
    temp4=np.array(x[3:6,2])    
    x[2, 0:3]=np.fliplr([temp4])[0]
    x [9:12,0]=temp1
    x[15,0:3]=np.fliplr([temp2])[0]
    x[3:6,2]=temp3

def Fac(): # move 2
    Fc()
    Fc()
    Fc()
    

def Uc(): #move 3
    x[0:3,0:3]=np.fliplr(x[0:3,0:3].transpose())
    temp1=np.array(x[12, 0:3])
    temp2=np.array(x [9,0:3])
    temp3=np.array(x[6,0:3])
    temp4=np.array(x[3,0:3])
    x[12, 0:3]=temp4
    x[9,0:3]=temp1
    x[6,0:3]=temp2
    x[3,0:3]=temp3

def Uac(): #move 4
    Uc()
    Uc()
    Uc()

def Dc():# move 5
    
    x[15:18,0:3]=np.fliplr(x[15:18,0:3].transpose())
    temp1=np.array(x[8, 0:3])
    temp2=np.array(x [11,0:3])
    temp3=np.array(x[14,0:3])
    temp4=np.array(x[5,0:3])
    x[8, 0:3]=temp4
    x[11,0:3]=temp1
    x[14,0:3]=temp2
    x[5,0:3]=temp3

def Dac(): #move 6
    Dc()
    Dc()
    Dc()

    
def Lc(): #move 7

    x[3:6,0:3]=np.fliplr(x[3:6,0:3].transpose())
    temp1=np.array(x[0:3, 0])
    temp2=np.array(x [6:9,0])
    temp3=np.array(x[15:18,0])
    temp4=np.array(x[12:15,2])
    x[0:3, 0]=np.fliplr([temp4])[0]
    x[6:9,0]=temp1
    x[15:18,0]=temp2
    x[12:15,2]=np.fliplr([temp3])[0]

def Lac(): #move 8
    Lc()
    Lc()
    Lc()


def Rc():   #move 9

    x[9:12,0:3]=np.fliplr(x[9:12,0:3].transpose())
    temp1=np.array(x[0:3, 2])
    temp2=np.array(x [12:15,0])
    temp3=np.array(x[15:18,2])
    temp4=np.array(x[6:9,2])
    x[0:3, 2]=temp4
    x[12:15,0]=np.fliplr([temp1])[0]
    x[15:18,2]=np.fliplr([temp2])[0]
    x[6:9,2]=temp3

def Rac(): # move 10
    Rc()
    Rc()
    Rc()

def Bc():   # move 11

    x[12:15,:]=np.fliplr(x[12:15,:].transpose())   
    temp1=np.array(x[0, 0:3])
    temp2=np.array(x[3:6,0])
    temp3=np.array(x[17,0:3])
    temp4=np.array(x[9:12,2])
    x[0, 0:3]=temp4
    x[3:6,0]=np.fliplr([temp1])[0]
    x[17,0:3]=temp2
    x[9:12,2]=np.fliplr([temp3])[0]
    
def Bac(): # move 12
    Bc()
    Bc()
    Bc()


def PrintCube():
    
    print("                "+str(x[0,0:3]))
    print("                "+str(x[1,0:3]))
    print("                "+str(x[2,0:3]))
    print('')
    print(str(x[3,0:3])+'\t'+str(x[6,0:3])+'\t'+str(x[9,0:3])+'\t'+str(x[12,0:3]))
    print(str(x[4,0:3])+'\t'+str(x[7,0:3])+'\t'+str(x[10,0:3])+'\t'+str(x[13,0:3]))
    print(str(x[5,0:3])+'\t'+str(x[8,0:3])+'\t'+str(x[11,0:3])+'\t'+str(x[14,0:3]))
    print('')
    print("             "+'\t'+str(x[15,0:3]))
    print("             "+'\t'+str(x[16,0:3]))
    print("             "+'\t'+str(x[17,0:3]))

def make_move(move, reverse ,printCube):
   
    if reverse==1:
        if move%2==0:
            move=move-1
        else:
                move=move+1        
    if move==1:
        Fc()
        #print("Front Clock Wise")
       
    if move==2:
        Fac()
        #print("Front Anti Clock Wise")
       
    if move==3:
        Uc()
        #print("Up Clock Wise")
        
    if move==4:
        Uac()
        #print("Up Anti Clock Wise")
        
    if move==5:
        Dc()
        #print("Down Clock Wise")
        
    if move==6:
        Dac()
        #print("Down Anti Clock Wise")
        
    if move==7:
        Lc()
        #print("Left Clock Wise")
        
    if move==8:
        Lac()
        #print("Left Anti Clock Wise")
        
    if move==9:
        Rc()
        #print("Right Clock Wise")
        
    if move==10:
        Rac()
        #print("Right Anti Clock Wise")
        
    if move==11:
        Bc()
        #print("Back Clock Wise")
       
    if move==12:
        Bac()
        #print("Back Anti Clock Wise")

    if printCube==1:
        PrintCube()
        
    

#solved cube x

y=np.array(xInitial)
x=np.array(goal)
Nodes = {'node 0':x}

nodeQueue.append('node 0')


print("x intialized")
PrintCube()
print('Searching for solution.....')


def searchGoal():
    level = 0
    nodeCounter = 1
    finish =0
    frontierCounter = 0           

    while(True):
        global x
        if(np.array_equal(x,y)==True):
            print('Goal Found!')
            
            goalNode.append(nodeName)
            break
        if(nodeQueue==[]):
            print("empty!")
            break
        
        q = Nodes[nodeQueue[0]]
        x = np.array(q)


        parent = nodeQueue[0]     
        
        
        child = 1
        while(child<13):
            nodeName = 'node '+str(nodeCounter)
            #print('nodeCounter : ' +str(nodeCounter))

            #child er list banaisi ekta
            #arekta holo ekta parent er under e tar shob gula child ke dhukaisi

            childNodeList.append(nodeName)
            parentChild.setdefault(parent, []).append(nodeName)
            nodeQueue.append(nodeName)
            nodeMoves[nodeName]=child
            nodeParent[nodeName] = parent

            
            make_move(child,0,0)
            solution.append(child)
            
            #print('move'+str(child))
            #dic.add(nodeName,x)
            #Nodes.update(nodeName = np.array(x))
            #nodeList.append(x)
            #print('pushed!')
            #for temporary array copy
            z = np.array(x)  
            Nodes[nodeName] = z
            
            
            if(np.array_equal(x,y)==True):
                break
            if(child%2==0):
                move = child -1
                make_move(move,0,0)
            elif(child%2!=0):
                move = child + 1
                make_move(move,0,0)
            
          
            nodeCounter = nodeCounter + 1
            child = child+1
        
        
        nodeQueue.pop(0)
        
            


def solve(node):
    while(True):
        if(node=='node 0'):
            break
        solutionPath.append(nodeParent[node])
        solutionMove.append(nodeMoves[node])
        node= nodeParent[node]
        
def solutionMoves():
    counter = 1
    for move in range(len(solutionMove)-1,-1,-1):
        print('Step' + str(counter)+' : ')
        move = solutionMove[move]
        if move==1:
        
            print("Front Clock Wise")
       
        if move==2:
        
            print("Front Anti Clock Wise")
       
        if move==3:
            
            print("Up Clock Wise")
        
        if move==4:
        
            print("Up Anti Clock Wise")
        
        if move==5:
        
            print("Down Clock Wise")
        
        if move==6:
        
            print("Down Anti Clock Wise")
        
        if move==7:
        
            print("Left Clock Wise")
        
        if move==8:
        
            print("Left Anti Clock Wise")
        
        if move==9:
        
            print("Right Clock Wise")
        
        if move==10:
        
            print("Right Anti Clock Wise")
        
        if move==11:
        
            print("Back Clock Wise")
       
        if move==12:
        
            print("Back Anti Clock Wise")

        counter += 1
    

    
    


#print(Nodes)
#print(parentChild)
#print(nodeQueue)
#print(Nodes['node 892'])
#print(nodeMoves)
#print(nodeParent)
#print(goalNode[0])
#print(nodeParent[goalNode[0]])

#print(solutionMove)

time.ctime()
fmt = '%H:%M:%S'
start = time.strftime(fmt)

searchGoal()
solve(goalNode[0])
solutionMoves()

time.ctime()
end = time.strftime(fmt)
print(end)
print('Time taken(sec):'+str(datetime.strptime(end, fmt) - datetime.strptime(start, fmt)))






