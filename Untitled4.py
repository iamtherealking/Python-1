#!/usr/bin/env python
# coding: utf-8

# Print Formatting

# In[1]:


print ("Hurry makes a bad curry")


# In[6]:


print("{c} makes a bad {h}".format(c="curry",h="hurry"))


# In[8]:


print("The {e} rotates around the {s}".format(e="earth",s="sun"))


# In[9]:


result =9/5
print (result)


# In[53]:


result =100/3


# In[55]:


print ("The result is {r:1.4f}".format(r=result))


# In[17]:


celsius = ((132-32)*5)/9


# In[18]:


print (celsius)


# In[ ]:


a = True


# In[19]:


a = False


# Operators

# In[21]:


5 >= 6


# < , > , >= , <=, ==

# In[24]:


5 <=6 or 6 >=7


# In[25]:


not 5<=6


# Looping

# In[29]:


a= "mllo";
if a.lower() == "hello":
    print(a)
elif a.lower() == "mello":
    print(a)
else:
    print(a)
    


# In[31]:


a= ["hello", "world"]
for variable in a:
    print (variable)


# In[35]:


for i in range(1,10,1):
    print (i)


# In[42]:


abc = [(0,1),(2,3),(4,5),(5,6),(6,7)]
for first_number , second_number in abc:
    print(first_number)


# In[43]:


a=[1,2,3,4,5]
for i in zip(a):
    print (i)


# In[46]:


a ="hello"
b =[ ]
for i in a:
    b.append(i)
    print(b)


# In[47]:


a ="hello"
b =[ ]
for i in a:
    b.append(i)
print(b)


# List Comprehension

# In[48]:


m= "Hello"
n=[x for x in m]
print (n)


# In[52]:


n=[x for x in range (0,10,2)]
print (n)


# In[62]:


a= "hello"
b= [y for (x,y) in enumerate(a) if x%2 == 0]
print (b)


# while loop
# 

# In[65]:


x= 0
while x<=5:
    print (x)
    x=x+1


# In[ ]:




