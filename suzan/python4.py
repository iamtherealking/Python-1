#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in range (10):
    print(i)


# In[9]:


for i in range (10):
    if i==5:
        continue
    print(i)


# In[10]:


for i in range (10):
    if i==5:
        break
    print(i)


# In[18]:


a="Ram has a cat"
a.split()


# In[20]:



a="Ram has a cat"
if 'cat' in a:
    print(True)


# In[21]:


a="Ram has a cat"
if 'shyam' in a:
    print(True)
else:
    print(False)


# In[50]:


a="Ram has a cat"
def check_cat(a):
    if 'cat' in a:
        print ("there is a cat")
check_cat(a)
    
    


# In[53]:


a="Ram has a cat"
def check_cat(a):
    if 'rat' in a:
        print ("there is:")
    else:
        print("there is no:")
check_cat(a)    


# In[58]:


a=[10,15,20,25,30,35,40]
def sum_digit(a,b):
    return (a+b)
print(sum_digit(a[0],a[1]))
print(sum_digit(a[1],a[2]))
print(sum_digit(a[2],a[3]))
print(sum_digit(a[3],a[4]))
print(sum_digit(a[4],a[5]))
print(sum_digit(a[5],a[6]))


# using loop

# In[61]:


a=[10,15,20,25,30,35,40]
def sum_digit(a,b):
    return (a+b)
for i in range(6):
    print(sum_digit(a[i],a[i+1]))


# In[63]:


a="ram has a cat"
if 'cat' in a:
    pass


# In[76]:


def convert(f):
    C = ((f-32)*5/9)
    return C
convert(34)


# In[84]:


def sq_root(a):
    s = a**0.5
    return s
sq_root(2)


# In[88]:


d={'apple':10,'banana':20,'cat':30,'dog':40}
for i in d:
    print (i)


# In[90]:


d={'apple':10,'banana':20,'cat':30,'dog':40}
for i in d.items():
    print (i)


# In[92]:


d={'apple':10,'banana':20,'cat':30,'dog':40}
for (x,y) in d.items():
    print (x)


# In[93]:


d={'apple':10,'banana':20,'cat':30,'dog':40}
for (x,y) in d.items():
    print (y)


# In[ ]:




