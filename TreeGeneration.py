Nodes = {}
parentChild = {}
childNode = []
nodes = []
x= 0
def treeGenerator():
    nodeCounter = 0
    currentCounter = 0

    while(True):

        if(nodeCounter==2):
            break
        i = 0
        while(i<12):
            childNode.append(str(currentCounter+1))
            
            currentCounter = currentCounter + 1
            #parentChild.update({'level '+str(nodeCounter):currentCounter})
            keys = 'level '+str(nodeCounter)
            if(nodeCounter==0):
                Nodes.update({keys:currentCounter})
                print('nodes')
                print(nodes)
                

            else:
                Nodes[keys].append(currentCounter) 
                
                
                       
            
            i = i + 1
        
        #print(tempList)
        
        
        

        

        nodeCounter = nodeCounter + 1
        print (nodeCounter)
        
        childNode[:] = []

treeGenerator()
print('parentchild')

print (parentChild)





            
