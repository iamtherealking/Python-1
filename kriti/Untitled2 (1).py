#!/usr/bin/env python
# coding: utf-8

# List
# It is an ordered sequence of elements upon which array like operations can be performed
# list is mutable 
# tuple is immutable

# In[1]:


a = [4,4.5,"Hello"]


# In[2]:


a[0]


# In[3]:


a = "sam"
a[0] ="p"


# In[8]:


a =[1,2,"Hi"]


# In[9]:


a ="Hello World"


# In[10]:


a.upper()


# In[11]:


a.lower()


# In[12]:


type(a)


# In[13]:


a.split()


# In[14]:


type(a.split())


# In[15]:


a ="HeraPheri"


# In[16]:


a.split('e')


# In[17]:


'1'+'6'


# '1'+'6' =concatination

# In[18]:


a=[1,1.1,"Hello"]


# In[19]:


a[0]


# In[20]:


a[2]


# In[22]:


a=[1,1.1,["Hello","World"]]


# In[28]:


a[2][1]


# In[31]:


a = [3,2,1,5,6,7]


# In[32]:


a.sort()


# In[33]:


print (a)


# In[ ]:


Dictionary
Unordered pair arrangement 
a ={'key': 'value'}


# In[34]:


a={'rollnumber': 18,'name':'Kriteeka','gender':'Female'}


# In[36]:


a['name']


# Tuple:(1,1,1,'Hello World)

# In[38]:


a=(1,1.1,'Hello World')


# In[39]:


a[0]


# In[ ]:


list=[1,1.1,'Hello World']


# In[40]:


tuple=(1,1.1,'Hello World')


# In[41]:


tuple[0]


# In[42]:


tuple[0]=2


# In[52]:


a=[1,1.1,"Hello"]


# In[53]:


a.pop(1)


# In[54]:


a


# In[65]:


a.pop()


# append=add

# In[66]:


a.append("world")


# In[67]:


a


# set:
#     should always contain unique value

# In[69]:


a=[1,2,3,1,1,2,4,5,2]


# In[70]:


set(a)


# Simple I/O operations

# In[72]:


get_ipython().run_cell_magic('writefile', 'lesson.txt', 'This is my first python lesson \nI am learning python')


# In[74]:


my_file=open('lesson.txt')


# In[75]:


my_file.read()


# In[76]:


my_file.read()


# In[77]:


my_file.seek(0)


# In[80]:


my_file.read()


# In[83]:


my_file.seek(6)


# In[84]:


my_file.read()


# In[85]:


with open ("lesson.txt") as my_file:
    my_file.seek(0)
    my_file.read()


# In[ ]:




