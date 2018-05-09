
# coding: utf-8

# In[8]:


get_ipython().run_line_magic('pylab', 'inline')


# In[9]:


import urllib.request
import re
import time


# This webspider needs two inputs: The URL to start from and a maximum number of links the spider should follow through.
# In addition you should decide if you want to do a depth or breadth first spider, use the proper cells accordingly.
# The spider should start at the url provided by startURL and then explore follow each link on the page, the resulting URLs should be stored in a list and returned. The list should not contain duplicate URLs, since that would indicate double downloads. Also the list should only contain URLs the spider downloaded, not the list of potential links

# In[10]:


#BOF
def spiderBreadthFirst(startURL,maxnumoflinks):
    #get the html from the the URL supplied by the user
    html=str(urllib.request.urlopen(startURL).read())
    #create an empty list and store all hyperlinks in this. the regex function looks for anything
    #that matches http:// or https://
    NL=[]
    NL.append(re.findall('"(https?://.*?)"',html,re.DOTALL))
    #create a reservoir, store the starturl in this
    res=[]
    res.append(startURL)
    #run the function while the reservoir is less than the max links
    while (len(res)<maxnumoflinks):
        for i in range(len(res)):
            #adds a time delay to make the spider seems more "human"
            time.sleep(np.random.randint(0,5))
            #gets the html data for each index inside the reservoir
            html1 = str(urllib.request.urlopen(res[i]).read())
            #store all hyperlinks in an intermediate list to compare with the reservoir
            check = re.findall('"(https?://.*?)"',html1,re.DOTALL)
            #only appends reservoir based on following if conditions
            for j in range(len(check)):
                if (check[j] not in res and len(res)<maxnumoflinks):
                    res.append(check[j])
    return res
                    
#EOF
#startURL is being updated again and again


# In[11]:


res = spiderBreadthFirst('http://alproductions.us/spider/page_0.html',70)

print(res)
print(len(res))

