#!/usr/bin/env python
# coding: utf-8

# In[4]:


for i in range(10):
    pass


# In[3]:


for i in range(10):


# In[6]:


for i in range(10):
    print(i)
    if i==5:
        break


# In[8]:


for i in range(10):
    if i==5:
        continue
    print(i)


# Methods vs functions

# In[13]:


a="Ram has a cat"
def check_cat(word):
    if 'cat' in word:
        return True
check_cat(a)
    
    


# In[18]:


a=[10,15,20,25,30,35]
def sum_digits(x,y):
    return (x+y)
for i in range(5):
      print(sum_digits(a[i],a[i+1]))


# In[23]:


def convert(f):
    return ((f-32)*5/9)
print(convert(100))
 


# In[25]:


f=[100,98,56,35,68]
def convert(x):
    return ((x-32)*5/9)
for i in range(5):
    print(convert(f[i]))


# In[27]:


d={'stat':5,'dsa':6,'cg':7}
for i in d:
    print(i)


# In[28]:


d={'stat':5,'dsa':6,'cg':7}
for i in d.items():
    print(i)


# In[30]:


def sqrt(a):
    return (a**0.5)
sqrt(4)


# tupple unpacking

# In[34]:


d={'stat':5,'dsa':6,'cg':7}
for x,y in d.items():
    print(x,y)


# In[ ]:




