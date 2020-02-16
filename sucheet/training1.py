#!/usr/bin/env python
# coding: utf-8

# data types are the buiding blocks upon which larger programs are made

# integer

# if first letter of name is capital and the following is in small then such case is known as - PASCAL CASE i.e(Suchitbaniya)

# int suchitBaniya-SNAKE CASE

# int suchit_baniya (python)

# In[1]:


4+5


# In[2]:


4-5


# In[3]:


4**2


# In[4]:


4/5


# In[6]:


print("hello world \n"*100);


# In[10]:


4**0.5  


# In[8]:


4/3


# In[9]:


4%3


# In[11]:


suchit =5


# In[12]:


suchit ="hello";


# mutability/Immutability

# slicing:
# [start : stop : step]

# In[ ]:





# In[15]:


any_world = "hello world";


# In[16]:


any_world [0]


# In[17]:


any_world [2]


# In[18]:


any_world [ : ]


# In[19]:


any_world [:5]


# In[20]:


any_world [::2]


# In[21]:


any_world [::-1]


# list 
# list is an ordered sequence of elements upon which array like operations can be performed

# In[22]:


a = "suman"


# In[23]:


a [0]


# In[25]:


a =[4,4,5,"hello"]


# In[26]:


a[0]


# In[27]:


a="hello world"


# In[28]:


a.upper()


# In[29]:


a.lower()


# In[30]:


a="hello world"


# In[31]:


type(a)


# In[32]:


a.split()


# In[34]:


type(a.split())


# In[37]:


a="suman bhandari"


# In[39]:


a.split("a")


# In[45]:


'1'+'1' 


# In[46]:


a=[1,1,1,"hello"]


# In[49]:


a="hello\nworld"


# In[50]:


print(a)


# In[52]:


a=[1,1.1,"hello"]


# In[54]:


a[0]


# In[55]:


a[2]


# In[64]:


a=[1,1.1,["hello","world"]]


# In[65]:


a[1]


# In[66]:


a[2]


# In[68]:


a[2][1]


# In[70]:


a=[1,2,4,3,5,10]


# In[71]:


a.sort()


# In[72]:


print(a)


# In[75]:


b=['c','d','a','f']


# In[76]:


b.sort()


# In[77]:


print(b)


# Dictionary
# Unordered pair arrangement
# a={'key':'value'}

# In[78]:


a={'rollnumber':1,'name':'rojish','gender':'not defined'}


# In[81]:


a['rollnumber']


# In[82]:


a['gender']


# In[84]:


a['name']


# Tuple
# (1,1,1,"hello world")
# it is immutable

# In[85]:


a=(1,2,3.2,"hello world")


# In[86]:


a[1]


# In[87]:


a=[1,1.2,1]


# In[92]:


a.pop(0)


# In[97]:


a.append(2)


# In[98]:


a


# set
# should always contain unique value

# In[99]:


a=[1,3,6,7,8,9]


# In[100]:


set(a)


# In[102]:


get_ipython().run_cell_magic('writefile', 'training.txt', 'this is my first python lesson.im learning python.')


# In[103]:


my_file =open ("training.txt")


# In[104]:


my_file.read()


# In[107]:


my_file.seek(11)


# In[108]:


my_file.read()


# In[109]:


with open("training.txt") as my_file:
    my_file.seek(0)
    my_file.read()


# In[ ]:




