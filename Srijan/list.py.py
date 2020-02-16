#!/usr/bin/env python
# coding: utf-8

# List
# List is an ordered sequence of elements upon which array like operations can be performed

# In[1]:


a="sam"


# In[12]:


a=[4,4,"hello"]
(/jun, sukai, data, type, ni, rakhna, milxa)


# In[13]:


a[0]


# In[33]:


a="sam"


# In[39]:


a.upper()//upper case ma convert garera print garaune


# In[43]:


a=[0,2,45,"hey"]
a.append(0)//adds element to the last of list

a[4]


# In[44]:


type(a)


# In[47]:


a="Hello World"
a.split()


# In[48]:


type(a.split())


# In[52]:


a="Hera Pheri"


# In[53]:


a.split('e')


# In[55]:


b = a.split('e')


# In[56]:


1+1


# In[57]:


'1'+'1'


# In[58]:


"hello"+"world"


# In[ ]:


a=[1,1.1,"Hello"]


# In[60]:


a="Hello\tWorld"
print(a)


# In[61]:


a[0]


# In[62]:


a=[1,1.1,["hello","world"]]//nested list


# In[64]:


a[2][1]


# In[65]:


a=[0,2,29,6,8]


# In[67]:


a.sort()//sorts element of list a
print(a)


# In[68]:


Dictionary 
Unordered pair arrangement
a=['key':'value']


# In[70]:


a={'rollnumber':1,'name':'Aanchal','gender':'Female'}


# In[74]:


a['rollnumber']
a['name']


# Tuple: same as list but yesto () ma

# In[76]:


a=(1,1.1,'Hello World')


# In[77]:


a[0]


# In[78]:


a[2]


# In[80]:


list = [1,1.1,"Hello World"]


# In[81]:


tuple =(1,1.1,"Hello World")


# In[83]:


list[0]


# In[85]:


list[0]=2//yesto garna milxa list ma but tuple ma mildaina so list is mutable 


# In[86]:


list


# tuple(0)=1  ma error so tuple is immutable

# In[93]:


list


# In[94]:


list.append(56)// adds element to the last of list


# In[95]:


list


# In[96]:


list.pop()


# In[97]:


list


# In[99]:


list.append(45)


# In[100]:


list.append(58)


# In[101]:


list.pop(0)


# In[102]:


list


# In[103]:


SET:
    should alays contain unique value


# In[105]:


a=[1,1,2.3]
set(a)//converts list to set i.e only unique elements


# In[107]:


a.pop()


# In[108]:


a


# In[109]:


get_ipython().run_cell_magic('writefile', 'lesson.txt', 'This is my first python lesson\nI am learning python')


# Simple input output operations
# 

# In[111]:


my_file=open('lesson.txt')


# In[112]:


my_file.read()


# In[113]:


my_file.read()


# In[115]:


my_file.seek(0)///0 position ma pugxa 


# In[116]:


my_file.read()


# In[118]:


with open("lesson.txt") as my_file:
    my_file.seek(0)
    my_file.read()


# In[ ]:




