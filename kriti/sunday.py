#!/usr/bin/env python
# coding: utf-8

# In[13]:


for i in range(10):
    print(i)
    if i==5:
        break


# In[15]:


for i in range(10):
    if i==5:
        continue
    print(i)


# In[30]:


a="Ram has a cat"
def search(word):
    if 'cat' in word:
        return True
search(a)


# In[47]:


a=[10,15,20,25,30,35,40]
def sum_digits(x,y):
    return(x+y)
for i in range(5):
    print(sum_digits(a[i],a[i+1]))


# In[55]:


def convert(f):
    c=(f-32)*5/9;
    return c
print(convert(100))


# In[59]:


f=[100,200,300]
def convert(x):
    return((x-32)*5/9)
for i in range(3):
    print(convert(f[i]))
    


# In[61]:


d={'dog':1,'cat':2}
for i in d:
    print(i)


# dog=key
# 1=value
#           (1 ko key dog ho)

# In[69]:


d={'dog':1,'cat':2}
for x,y in d.items():
    print(x,y)


# tuple unpacking

# In[66]:


def squrt(a):
    return(a**0.5)
squrt(16)


# In[ ]:




