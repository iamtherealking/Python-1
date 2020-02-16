#!/usr/bin/env python
# coding: utf-8

# Print Formatting

# In[1]:


print ("Hurry makes a bad curry")


# In[4]:


print ("{c} makes a bad {h}".format(c="curry",h="hurry"))


# In[8]:


print ("The {0} rotates round the {1}".format("earth","sun"))


# In[9]:


result = 9/5
print (result)


# In[13]:


result = 100/3


# In[59]:


print ("The result is {r:1.4f}".format(r=result))


# In[16]:


celsius = ((132-32)*5)/9


# In[17]:


print (celsius)


# In[19]:


Boolean


# In[20]:


a = True


# In[21]:


a = False


# Operators

# In[22]:


5 <= 6


# In[23]:


< , > , >= , <= , ==


# In[26]:


5 <= 6 6 >= 7


# In[27]:


5 <=6 or 6 >=7


# In[28]:


not 5<=6


# Looping

# In[43]:


a= "Mello";
if a.lower() == "Hello":
    print(a)
elif a.lower() == "Mello":
    print(a)
else:
    print(a)


# In[44]:



a= ["hello", "world"]
for variable in a:
    print (variable)


# In[41]:


for f in range(0,10,3):
     print (f)


# In[46]:


abc = [(0,1),(2,3),(4,5),(5,6),(6,7)]
for i in abc:
    print(i)


# In[47]:


abc = [(0,1),(2,3),(4,5),(5,6),(6,7)]
for (first_number,second_number) in abc:
    print(second_number)


# In[50]:


abc = [(0,1),(2,3),(4,5),(5,6),(6,7)]
for first_number , second_number in abc:
    print(first_number)


# In[51]:


a=[1,2,3,4,5]
for i in zip(a):
    print (i)


# In[ ]:


List Comprehension


# In[52]:


a=["Hello"]
for i in zip (a):
    print (i)


# In[53]:


a = "hello"
b =[]
for i in a:
    b.append(i)
    print(b)


# In[54]:


a = "hello"
b =[]
for i in a:
    b.append(i)
print(b)


# In[ ]:


List Comprehension


# In[56]:


m= "Hello"
n=[x for x in m]
print (n)


# In[58]:


n=[x for x in range(0,10,2)]
print(n)


# In[65]:


m= "hello"
n= [x for x in enumerate(m)]
print(n)


# In[67]:


m= "hello"
n= [x for x in enumerate()]
print(n)


# In[69]:


a= "Hello"
b=[y for (x,y) in enumerate(a) if x%2 == 0]
print(b)


# In[70]:


a= "Hello"
b=[x for (x,y) in enumerate(a) if x%2 == 0]
print(b)


# while loop
# 

# In[73]:


x=0
while x<=5:
 print (x)
 x=x+1
else:
    print(x)


# In[74]:


x=0
while x<=5:
 print (x)
 x=x+1


# In[ ]:




