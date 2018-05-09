
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from pandas import *
import random


# I implement three graph generators, where you receive a number of nodes and a number of edges.

# In[4]:


def graphAsMatrix(nodes,edges):
    #i create an empty list and add several lists to it equaling the number of nodes
    matrix=[]
    for i in range(nodes):
        matrix.append([])
        #set all values as 0 initially 
        matrix[i]=[0]*nodes
    
    #initialize an empty list and while the length of the edge list is less than the # of edges, keep creating random edges
    EdgeList=[]
    while len(EdgeList)<edges:
        edge = random.sample(range(0,nodes),2)
        #ensure that a duplicate edge such as [0,0] isnt created
        if edge not in EdgeList and edge[0]!=edge[1]:
            EdgeList.append(edge)
            #append to the matrix based on the edge coordinates
            matrix[edge[0]][edge[1]]=1
    print(EdgeList)
    return matrix

Matrix=graphAsMatrix(4,9)
Matrix


# In[5]:


def graphAsEdgeList(nodes,edges):
    #initialize empty list and fill it with edges until the # of edges required is met
    EdgeList=[]
    while len(EdgeList)<edges:
        edge = random.sample(range(0,nodes),2)
        if (edge not in EdgeList):
            EdgeList.append(edge)
            
    return EdgeList

EdgeL = graphAsEdgeList(4,9)
EdgeL


# In[6]:


def graphAsEdgeDictionary(nodes,edges): 
    # i create the edges first using the same ideology as above
    EdgeList=[]
    while len(EdgeList)<edges:
        edge = random.sample(range(0,nodes),2)
        if (edge not in EdgeList):
            EdgeList.append(edge)
    print(EdgeList)
    #create an empty dictionary and append the key with the first coordinate and the values with the second
    EdgeDict = {}          
    for edge in EdgeList:
        if edge[0] in EdgeDict:
            EdgeDict[edge[0]].append(edge[1])
        else:
            EdgeDict[edge[0]] = [edge[1]]
    return EdgeDict

graphAsEdgeDictionary(4,9)


# Now I implement all the translator functions from one data format to the other.

# In[7]:


def MatrixToEdgeList(theMatrix):
    #create an empty edge list
    EdgeList=[]
    #loop through the entire matrix and when matrix value equals 1, use the indices as the edge values
    for i in range(len(theMatrix)):
        for j in range(len(theMatrix)):
            if theMatrix[i][j]==1:
                EdgeList.append([i,j])
    print(theMatrix)
    return EdgeList

#Verify Results
MatrixToEdgeList(Matrix)


# In[8]:


def MatrixToEdgeDictionary(theMatrix): 
    EdgeDict={}
    #loop through each list and then through the elements within the list
    for i in range(len(theMatrix)):
        for j in range(len(theMatrix[i])):
            #if the matrix coordinate is 1 and if the key exists, add the value to the dictionary
            if theMatrix[i][j]==1:
                if i in EdgeDict:
                    EdgeDict[i].append(j)
                else:
                    EdgeDict[i] = [j]
    print(theMatrix)
    return EdgeDict
    
#compare with the matrix created in the generator
EdgeDictionary = MatrixToEdgeDictionary(Matrix)
EdgeDictionary


# In[9]:


def EdgeDictionaryToMatrix(edgeDictionary):
    #create an empty matrix with the len of the dictionary
    matrix_1=[]
    for i in range(len(edgeDictionary)):
        matrix_1.append([])
        matrix_1[i]=[0]*(len(edgeDictionary))
    
    #loop through each key of the dictionary and each value for the keys
    for i in range(len(edgeDictionary)):
        for j in range(len(edgeDictionary[i])):
            #check if key exists and if the value exists
            if i in edgeDictionary:
                k=edgeDictionary[i][j]
                matrix_1[i][k]=1
    
    print(edgeDictionary)
    return matrix_1

EdgeDictionaryToMatrix(EdgeDictionary)


# In[10]:


def EdgeListToEdgeDictionary(edgeList):
    EdgeDict = {}  
    #run through each edge. for each edge, the first number in the edge is the key. Check if key exists and append if it does.
    #otherwise
    for edge in edgeList:
        if edge[0] in EdgeDict:
            EdgeDict[edge[0]].append(edge[1])
        else:
            EdgeDict[edge[0]] = [edge[1]]
    print(edgeList)
    return EdgeDict

EdgeListToEdgeDictionary(EdgeL)


# In[12]:


# retired 
def EdgeDictionaryToMatrix(nodesEdgeSet):
    #create an empty matrix with the len of the dictionary
    matrix=[]
    for i in range(len(nodesEdgeSet)):
        matrix.append([])
        matrix[i]=[0]*(len(nodesEdgeSet))
    
    #loop through each key of the dictionary and each value for the keys
    for i in range(len(nodesEdgeSet)):
        for j in range(len(nodesEdgeSet[i])):
            #check if key exists and if the value exists
            if i in nodesEdgeSet:
                k=nodesEdgeSet[i][j]
                matrix[i][k]=1
    
    print(nodesEdgeSet)
    return matrix

EdgeDictionaryToMatrix(EdgeDictionary)


# In[11]:


#retired 
def EdgeDictionaryToEdgeList(nodesEdgeSet):
    nodes_list=list(nodesEdgeSet.keys())
    edges_list=list(nodesEdgeSet.values())

    EdgeList=[]
    for i in range(len(nodes_list)):
        for j in range(len(edges_list[i])):
            edge=[i,edges_list[i][j]]
            EdgeList.append(edge)
    print(nodesEdgeSet)
    return EdgeList

EdgeDictionaryToEdgeList(EdgeDictionary)

