#!/usr/bin/env python
# coding: utf-8

# Print Formatting

# In[1]:


print("Hurry makes a bad curry")


# In[2]:


print("The earth rotates around the sun")


# In[4]:


print("{t} earth rotates {a} the {s}".format(t="The",a="around",s="sun"))


# In[5]:


print("{t} earth rotates {t} the {t}".format(t="The",a="around",s="sun"))


# In[6]:


result=9/5
print(result)


# In[7]:


result=100/3


# In[ ]:


result=100/3


# In[10]:


print("The result is {r:1.4f}".format(r=result))


# In[11]:


celsius=((132-32)*5)/9
print(celsius)


# In[13]:


print("The result is {c:1.2f}".format(c=celsius))


# Boolean

# In[ ]:


a=True


# In[14]:


a=False


#  Operators

# In[15]:


5<=6


# In[16]:


5>=5


# 5>=6

# <,>,>=,<=,==,!=

# In[18]:


5<=6 and 6<=7


# In[19]:


5<=6 and 6>=7


# In[20]:


1<=3 or 5>=6


# In[21]:


not 5<=6


# Looping 

# In[28]:


a="Hello";
if a.lower() == "hello":
    print(a)
elif a.lower() == "mello":
    print(a)
    


# In[31]:


a="Mllo";
if a.lower() == "hello":
    print(a)
elif a.lower() == "mello":
      print(a)
else:
    print(a)
     


# In[32]:


a="hello"
for variable in a:
    print(variable)
    
    


# In[33]:


a= ["hello","world"]
for variable in a:
    print (variable)


# In[34]:


for i in range(0,10):
    print(i)
    


# In[35]:


for i in range(0,10):
    print(i)


# In[36]:


for i in range(0,10,2):
    print(i)


# In[37]:


for i in range(0,10,4):
    print(i)


# In[38]:


for i in range(0,10,2):
    print (i)


# In[39]:


for i in range(1,10,2):
    print(i)


# In[40]:


abc = [(0,1),(2,3),(4,5),(5,6),(6,7)]
for i in abc:
    print(i)
    


# In[42]:


abc = [(0,1),(2,3),(4,5),(5,6),(6,7)]
for first_number,second_number in abc:
    print(second_number)


# In[46]:


abc = [(0,1),(2,3),(4,5),(5,6),(6,7)]
for first_number,second_number in abc:
    print(first_number)


# In[44]:


a=[1,2,3,4,5]
for i in zip(a):
    print (i)


# List Comprehension

# In[51]:


a="Hello"
b=[]
for i in a:
  b.append(i)
print(b)
 


# In[52]:


a="Hello"
b=[]
for i in a:
  b.append(i)
  print(b)


# In[53]:


m= "Hello"
n=[x for x in m]
print(n)


# In[54]:



n=[x for x in range(0,10,2)]
print(n)


# In[61]:


m="Hello"
n=[y for (x,y) in enumerate(m) if x%2 == 0]
print(n)


# while loop

# In[65]:


x=0
while x<=5:
 print (x)
 x=x+1
else:
    print(x)


# In[66]:


x=0
while x<=5:
 print (x)
 x=x+1


# In[ ]:




