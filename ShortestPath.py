grid = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 2]]

queue = []
queue.append('Node00')
nodes = []
nodes.append('Node00')
nodeParent = {}
print(grid[1][0])

def goalSearch(x,y):

    
    i = 0
    while(True):
        parent = nodes[0]
        print(parent)
        parentX = x
        parentY = y
        if(i==20):
            break
        if(grid[x][y]==2):
            print('goal found!')
            return
        if ((x < len(grid)-1 )):
            if(grid[parentX+1][y] == 0):
                print('x+1')
                name = 'Node'+str(x+1)+str(y)
                nodes.append(name)
                print(nodes)
                nodeParent[name] = parent
                print(parent,':', name)
                parentX = x+1
                

        if ((y>0 )):
            if(grid[x][y-1] == 0):
                print('y-1')
                name = 'Node'+str(x)+str(y-1)
                nodes.append(name)
                nodeParent[name] = parent
                print(nodes)
                print(parent,':', name)
                y = y-1
                

        if ((x>0 )):
            if(grid[x-1][y] == 0):
                print('x-1')
                name = 'Node'+str(x-1)+str(y)
                nodes.append(name)
                nodeParent[name] = parent
                print(nodes)
                print(parent,':', name)
                x = x-1
                

        if ((y < len(grid)-1 )):
            if(grid[x][y+1] == 0):
                print('y+1')
                name = 'Node'+str(x)+str(y+1)
                nodes.append(name)
                nodeParent[name] = parent
                print(nodes)
                print(parent,':', name)
                y = y+1
            
        nodes.pop(0)
        return
            
        i+= 1  

    
        

goalSearch(0,0)
        
