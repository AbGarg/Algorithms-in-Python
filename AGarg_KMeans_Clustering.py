
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('pylab', 'inline')


# In[17]:


from pandas import *
import pandas 
import numpy
import matplotlib.pyplot as plt


# First I create a function to calculate the euclidean distance. I assume that user gets two lists as coordinates with arbitrary dimensions, len(A)==len(B)

# In[18]:


#BOF
def dist(A,B):
    a=0
    for i in range(len(A)):
         a+= ((B[i]-A[i])**2)
    b=(a**(1/2))
    return b
#EOF


# Data generator (emitter) Function:  I design a function that receives a list of column names and a length and a number of clusters to generate a DataFrame with the appropriate column and an extra list with labels "class". The class contains the actual class labels.

# In[19]:


#BOF
#create a function to generate a random dataset based on number of column, 
#length of columns, number of cluster
def generateTable(columnNames,length,K):
    table=DataFrame()
    classLabels=[]
    classLabels=[0]*length

    for X in columnNames:
        table[X]=[0.0]*length

    for k in range(K):
        #randomize variables for mean and stdev to create random datapoints 
        xc=(numpy.random.random()*1.0)
        stdev=0.1+(numpy.random.random()*0.2)
        for i in columnNames:
            for j in range(int((k*length/K)),int(length/K+(k*length/K))):
                #means and stdev in the numpy.random.normal function change consistently
                table[i][j]=numpy.random.normal(xc,stdev)
                classLabels[j]=k
    return table, classLabels


#EOF


# Create a dataset with random unclustered data

# In[20]:


#random dataset to test clustering algorithm on
table_1, classLabels = generateTable(("A", "B"), 1000, 5)
cols=["r","g","b","y","m","c","k"]
for i in range(len(table_1)):
    plt.plot(table_1["A"][i],table_1["B"][i],"."+cols[classLabels[i]])


# The next function takes two list, and we assume that
# one list is the correct labeled classes and the other list
# is whatever your clustering algorithm created. Compare both lists
# and compute a matching coefficient. If all labels are identical
# the score is 1.0 if all labels are wrong (impossible) the result should 
# be 0.0 the rest should be proportionally matched between both extremes

# ## Create a K-means clustering algorithm

# In[21]:


#BOF
def kmeans(table,K):
    #counter for the number of iterations
    counter=0
    #initialize two empty lists
    centroid_int=[]
    new_centroid=[]
    #step1: store the initial guesses for centroids picked randomly in a list
    for k in range(K):
        centroid_int.append(list(table.loc[numpy.random.randint(0,len(table))]))

######## step 2: for all points, all centroids, compute distance
#keep running until new centroids are different than previous iteration of centroids
    while(centroid_int!=new_centroid):
        #create some empty lists for labels, storing centroid distances, intermediate storage
        labels=[]
        Z=[]
        int_list=[]
        #find distances and store them 
        for n in range(len(table)):
            Z.append([])
            for m in range(len(centroid_int)):
                Z[n].append(dist(centroid_int[m],list(table.loc[n])))
                
        #store classlabels based on distances identified, identify min distances
        for n in range(len(Z)):
            labels.append(Z[n].index(min(Z[n])))
        #intermediate list for data manipulation and moving the centroids
        for i in range(K):
            int_list.append([])
        for i in range(len(labels)):
            int_list[labels[i]].append(list(table.loc[i]))
            
        #calculate new centroids based on average distances
        for i in range(len(int_list)):
            new_centroid.append(list(np.average(int_list[i],axis=0)))
        #if the new centroids are different from previous iteration, empty lists and use the 
        #newly calculated centroids to calculate distances again
        if new_centroid!=centroid_int:
            centroid_int=[]
            centroid_int=new_centroid
            new_centroid=[]
        else:
        #if centroids are same, stop and store them as final centroids
            centroid_final=[]
            centroid_final=new_centroid
        counter+=1
    return (labels,centroid_final,counter)
    #return the labels, centroid locations and the number of iterations
#EOF


# plot and see if the algorithm can properly cluster random data

# In[24]:


labels, centroid_final,counter = kmeans(table_1,4)
for i in range(len(table_1)):
    plt.plot(table_1["A"][i],table_1["B"][i],"."+cols[labels[i]])
cols=["r","g","b","y","m","c","k"]
for i in range(len(centroid_final)):
    plt.plot([centroid_final[i][0]],[centroid_final[i][1]], "o", markersize = 10, color = "k")    
#EOF
print(counter)

