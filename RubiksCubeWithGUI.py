from tkinter import *
import tkinter as tk
import numpy as np
from random import randint
from datetime import datetime
import time
import tkMessageBox

final = []

master= tk.Tk()

scrollbar = Scrollbar(master) 
scrollbar.pack( side = RIGHT, fill = BOTH ) 
mylist = Listbox(master, yscrollcommand = scrollbar.set )

mylist.pack( side = LEFT, fill = BOTH )

scrollbar.config( command = mylist.yview )
    



canvas1 = tk.Canvas(master, width = 1280, height = 700)
canvas1.pack()


e1 = tk.Entry(master, width="4")
e2 = tk.Entry(master, width="4")
e3 = tk.Entry(master, width="4")
e4 = tk.Entry(master, width="4")
e5 = tk.Entry(master, width="4")
e6 = tk.Entry(master, width="4")
e7 = tk.Entry(master, width="4")
e8 = tk.Entry(master, width="4")
e9 = tk.Entry(master, width="4")
e10 = tk.Entry(master, width="4")
e11= tk.Entry(master, width="4")
e12 = tk.Entry(master, width="4")
e13 = tk.Entry(master, width="4")
e14 = tk.Entry(master, width="4")
e15 = tk.Entry(master, width="4")
e16 = tk.Entry(master, width="4")
e17 = tk.Entry(master, width="4")
e18 = tk.Entry(master, width="4")
e19 = tk.Entry(master, width="4")
e20= tk.Entry(master, width="4")
e21 = tk.Entry(master, width="4")
e22 = tk.Entry(master, width="4")
e23= tk.Entry(master, width="4")
e24 = tk.Entry(master, width="4")
e25 = tk.Entry(master, width="4")
e26= tk.Entry(master, width="4")
e27 = tk.Entry(master, width="4")
e28= tk.Entry(master, width="4")
e29= tk.Entry(master, width="4")
e30= tk.Entry(master, width="4")
e31= tk.Entry(master, width="4")
e32= tk.Entry(master, width="4")
e33= tk.Entry(master, width="4")
e34= tk.Entry(master, width="4")
e35 = tk.Entry(master, width="4")
e36 = tk.Entry(master, width="4")
e37= tk.Entry(master, width="4")
e38= tk.Entry(master, width="4")
e39 = tk.Entry(master, width="4")
e40 = tk.Entry(master, width="4")
e41 = tk.Entry(master, width="4")
e42 = tk.Entry(master, width="4")
e43 = tk.Entry(master, width="4")
e44 = tk.Entry(master, width="4")
e45 = tk.Entry(master, width="4")
e46 = tk.Entry(master, width="4")
e47 = tk.Entry(master, width="4")
e48 = tk.Entry(master, width="4")
e49 = tk.Entry(master, width="4")
e50 = tk.Entry(master, width="4")
e51 = tk.Entry(master, width="4")
e52 = tk.Entry(master, width="4")
e53 = tk.Entry(master, width="4")
e54 = tk.Entry(master, width="4")

canvas1.create_window(900,50, window=e1,width = "20")
canvas1.create_window(930,50, window=e2,width = "20")
canvas1.create_window(960,50, window=e3,width = "20")

canvas1.create_window(900,80, window=e4,width = "20")
canvas1.create_window(930,80, window=e5,width = "20")
canvas1.create_window(960,80, window=e6,width = "20")

canvas1.create_window(900,110, window=e7,width = "20")
canvas1.create_window(930,110, window=e8,width = "20")
canvas1.create_window(960,110, window=e9,width = "20")

canvas1.create_window(800,150, window=e10,width = "20")
canvas1.create_window(830,150, window=e11,width = "20")
canvas1.create_window(860,150, window=e12,width = "20")

canvas1.create_window(800,180, window=e13,width = "20")
canvas1.create_window(830,180, window=e14,width = "20")
canvas1.create_window(860,180, window=e15,width = "20")

canvas1.create_window(800,210, window=e16,width = "20")
canvas1.create_window(830,210, window=e17,width = "20")
canvas1.create_window(860,210, window=e18,width = "20")

canvas1.create_window(900,150, window=e19,width = "20")
canvas1.create_window(930,150, window=e20,width = "20")
canvas1.create_window(960,150, window=e21,width = "20")

canvas1.create_window(900,180, window=e22,width = "20")
canvas1.create_window(930,180, window=e23,width = "20")
canvas1.create_window(960,180, window=e24,width = "20")

canvas1.create_window(900,210, window=e25,width = "20")
canvas1.create_window(930,210, window=e26,width = "20")
canvas1.create_window(960,210, window=e27,width = "20")

canvas1.create_window(1000,150, window=e28,width = "20")
canvas1.create_window(1030,150, window=e29,width = "20")
canvas1.create_window(1060,150, window=e30,width = "20")

canvas1.create_window(1000,180, window=e31,width = "20")
canvas1.create_window(1030,180, window=e32,width = "20")
canvas1.create_window(1060,180, window=e33,width = "20")

canvas1.create_window(1000,210, window=e34,width = "20")
canvas1.create_window(1030,210, window=e35,width = "20")
canvas1.create_window(1060,210, window=e36,width = "20")


canvas1.create_window(1100,150, window=e37,width = "20")
canvas1.create_window(1130,150, window=e38,width = "20")
canvas1.create_window(1160,150, window=e39,width = "20")

canvas1.create_window(1100,180, window=e40,width = "20")
canvas1.create_window(1130,180, window=e41,width = "20")
canvas1.create_window(1160,180, window=e42,width = "20")

canvas1.create_window(1100,210, window=e43,width = "20")
canvas1.create_window(1130,210, window=e44,width = "20")
canvas1.create_window(1160,210, window=e45,width = "20")

canvas1.create_window(900,250, window=e46,width = "20")
canvas1.create_window(930,250, window=e47,width = "20")
canvas1.create_window(960,250, window=e48,width = "20")

canvas1.create_window(900,280, window=e49,width = "20")
canvas1.create_window(930,280, window=e50,width = "20")
canvas1.create_window(960,280, window=e51,width = "20")

canvas1.create_window(900,310, window=e52,width = "20")
canvas1.create_window(930,310, window=e53,width = "20")
canvas1.create_window(960,310, window=e54,width = "20")



def printTheCube():
    goal[0][0] = e1.get()
    goal[0][1] = e2.get()
    goal[0][2] = e3.get()

    goal[1][0] = e4.get()
    goal[1][1] = e5.get()
    goal[1][2] = e6.get()

    goal[2][0] = e7.get()
    goal[2][1] = e8.get()
    goal[2][2] = e9.get()


    goal[3][0] = e10.get()
    goal[3][1] = e11.get()
    goal[3][2] = e12.get()

    goal[4][0] = e13.get()
    goal[4][1] = e14.get()
    goal[4][2] = e15.get()

    goal[5][0] = e16.get()
    goal[5][1] = e17.get()
    goal[5][2] = e18.get()


    goal[6][0] = e19.get()
    goal[6][1] = e20.get()
    goal[6][2] = e21.get()

    goal[7][0] = e22.get()
    goal[7][1] = e23.get()
    goal[7][2] = e24.get()

    goal[8][0] = e25.get()
    goal[8][1] = e26.get()
    goal[8][2] = e27.get()


    goal[9][0] = e28.get()
    goal[9][1] = e29.get()
    goal[9][2] = e30.get()

    goal[10][0] = e31.get()
    goal[10][1] = e32.get()
    goal[10][2] = e33.get()

    goal[11][0] = e34.get()
    goal[11][1] = e35.get()
    goal[11][2] = e36.get()


    goal[12][0] = e37.get()
    goal[12][1] = e38.get()
    goal[12][2] = e39.get()

    goal[13][0] = e40.get()
    goal[13][1] = e41.get()
    goal[13][2] = e42.get()

    goal[14][0] = e43.get()
    goal[14][1] = e44.get()
    goal[14][2] = e45.get()


    goal[15][0] = e46.get()
    goal[15][1] = e47.get()
    goal[15][2] = e48.get()

    goal[16][0] = e49.get()
    goal[16][1] = e50.get()
    goal[16][2] = e51.get()

    goal[17][0] = e52.get()
    goal[17][1] = e53.get()
    goal[17][2] = e54.get()



    tkMessageBox.showinfo("Confirmation", "Are you sure?!")
    x[0:18,0:3]=goal[0:18,0:3]
    PrintCube()
    

    

    
    
    
    
        
button1 = tk.Button(text='Take The Input', command=printTheCube, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(930, 400, window=button1)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

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
            mylist.insert(END, 'Front Clock Wise')
            
       
        if move==2:
        
            print("Front Anti Clock Wise")
            mylist.insert(END, 'Front Anti Clock Wise')
            
       
        if move==3:
            
            print("Up Clock Wise")
            mylist.insert(END, 'Up Clock Wise')
        
        if move==4:
        
            print("Up Anti Clock Wise")
            mylist.insert(END, 'Up Anti Clock Wise')
        
        if move==5:
        
            print("Down Clock Wise")
            mylist.insert(END, 'Down Clock Wise')
        
        if move==6:
        
            print("Down Anti Clock Wise")
            mylist.insert(END, 'Down Anti Clock Wise')
        
        if move==7:
        
            print("Left Clock Wise")
            mylist.insert(END, 'Left Clock Wise')
        
        if move==8:
        
            print("Left Anti Clock Wise")
            mylist.insert(END, 'Left Anti Clock Wise')
        
        if move==9:
        
            print("Right Clock Wise")
            mylist.insert(END, 'Right Clock Wise')
        
        if move==10:
        
            print("Right Anti Clock Wise")
            mylist.insert(END, 'Right Anti Clock Wise')
        
        if move==11:
        
            print("Back Clock Wise")
            mylist.insert(END, 'Back Clock Wise')
       
        if move==12:
        
            print("Back Anti Clock Wise")
            mylist.insert(END, 'Back Anti Clock Wise')

        counter += 1
        
    


def GO():
    
    time.ctime()
    fmt = '%H:%M:%S'
    start = time.strftime(fmt)
    searchGoal()
    solve(goalNode[0])
    solutionMoves()

    time.ctime()
    end = time.strftime(fmt)
    print('Time taken(sec):'+str(datetime.strptime(end, fmt) - datetime.strptime(start, fmt)))

     
    
button2 = tk.Button(text='Solve The Cube!', command=GO, bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(930, 440, window=button2)
tk.mainloop()
