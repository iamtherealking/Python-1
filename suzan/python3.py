#!/usr/bin/env python
# coding: utf-8

# Print formatting

# In[1]:


print ("hurry makes a bad curry")


# In[3]:


print("{1} makes a bad {0}".format("curry","hurry"))


# In[7]:


print("The {e} rotates {a} a {s}".format(e="Earth",a="around",s="Sun"))


# In[8]:


result=9/5
print(result)


# In[9]:


result=100/3
print(result)


# In[82]:


print("the result is {r:1.4f}".format(r=result))


# In[13]:


celsius=((132-32)*5)/9


# In[14]:


print(celsius)


# boolean

# In[17]:


a=True


# In[18]:


a=False


# Operators

# In[20]:


5>=6


# In[21]:


not 5>=6


# looping
# 

# In[23]:


a="hello";
if a.lower()=="hello":
    print(a)
elif  a.lower()=="hello":
    print(a)
else:
    print(a)


# In[24]:


a="hello"
for variable in a:
    print(variable)


# In[28]:


a=["hello","world"]
for variable in a:
    print (variable)


# In[29]:


for i in range (0,10,2):
    print(i)


# In[30]:


for i in range(0,10):
    print(i%2)


# In[31]:


abc=[(0,1),(2,3),(4,5),(5,6),(6,7)]
for i in abc:
    print(i)


# In[33]:


abc=[(0,1),(2,3),(4,5),(5,6),(6,7)]
for first_number,second_number in abc:
    print(second_number)


# In[34]:


abc=[(0,1),(2,3),(4,5),(5,6),(6,7)]
for first_number,second_number in abc:
    print(first_number)


# In[35]:


abc="hello"
for i in enumerate(abc):
    print(i)


# In[36]:


abc="hello"
for index,value in enumerate(abc):
    print(value)


# In[39]:


abc="hello"
for index, value in enumerate(abc):
    print(index)


# In[40]:


a=[1,2,3,4,5]
b=[6,7,8,9,10]
for i in zip(a,b):
    print(i)


# In[67]:


a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[11,12,13,14,15]
for i in zip(a,b,c):
    print(i)


# List Comprehension

# In[66]:


a="hello"
b=[ ]
for i in a:
    b.append(i)
    print(b)


# In[68]:


m="hello"
n=[x for x in m]
print (n)


# In[81]:


a=[]
b=[x for x in range (0,10,2)]
print(b)


# In[83]:


a="hello"
b=[x  for x in enumerate(a)]
print(b)


# In[109]:


a="hello"
b=[y for (x,y) in enumerate(a) if x%2 == 0]
print(b)


# While loop

# In[111]:


x=0
while x<=5:
    print(x)
    x=x+1
else:
    print(x)


# In[112]:


x=0
while x<=5:
    print(x)
    x=x+1
    


# In[ ]:




