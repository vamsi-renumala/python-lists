#!/usr/bin/env python
# coding: utf-8

# ### List

# In[5]:


mylist1=[10,3,1,4,5,8,2]
mylist2=["a","e","i","o","u"]
mylist3=[10,3,1,4,5,8,2,"a","e","e","i","o"]
mylist3


# #### list is a hetrogeneous because, it allows multiple datatypes
# #### we can retrive the elements using index.Index starts from 0.
# #### list has square brackets.

# In[2]:


mylist1[0]


# In[3]:


mylist2[3]="buddy"
mylist2


# #### list is immutable

# In[10]:


mylist=[10,3,1,4,5,8,2,22,18,73,36,9,4,59,34,7,25,8,24,49,33,36,23,58,69]
final_list = list(filter(lambda x: (x%3 ==0) , mylist))
print(final_list)


# In[13]:


final_list1 = list(map(lambda x:x**2, mylist1))
print(final_list1)


# In[23]:


from functools import reduce
final_list2 = reduce(lambda a,b:a*b,mylist1)
print(final_list2)


# In[3]:


mylist2=list("artificial intelligence")
mylist2


# ### or

# In[5]:


type(mylist2)


# In[8]:


mylist2.append(5)
mylist2


# In[13]:


mylist2[20]


# In[16]:


mylist2[20]="N"
mylist2


# ### Methods

# #### 1.append()
# #### 2.copy()
# #### 3.count() - returns No of times the element appears in the list.
# #### 4.insert()
# #### 5.reverse()
# #### 6.remove()
# #### 7.sort()
# #### 8.pop()
# #### 9.extend() - combines two lists into one.
# #### 10.index()
# #### 11.clear()

# In[18]:


empty_list=[]
empty_list


# In[19]:


empty_list.append("Machine Learning")
empty_list


# In[26]:


empty_list.remove("Artificial intelligence")
empty_list


# In[25]:


mylist1=[10,3,1,4,5,8,2]
mylist1.remove(10)
mylist1


# In[27]:


len(mylist1)


# In[28]:


max(mylist1)


# In[29]:


min(mylist1)


# In[31]:


sum(mylist1)


# In[32]:


len(mylist2)


# In[33]:


1 in mylist1


# In[34]:


10 not in mylist1


# In[39]:


empty_list.reverse()
empty_list


# In[41]:


mylist1.sort()
mylist1


# In[9]:


l1=["apple","banana","orange","pineapple","guava","strawberry"]
l1.sort()
l1


# In[10]:


l1.pop()


# In[11]:


l1


# In[12]:


l1.append("strawberry")
l1


# In[16]:


l2=[1,3,6,2,5,6,3,7,9,5,9,5,3,9,4,7,2]
l2.count(5)


# In[17]:


v=l2.copy()
v


# #### List indexing and slicing

# In[18]:


l2


# In[19]:


l2[10]


# In[20]:


l2[-1]


# In[ ]:





# #### Negative indexing starts from n-1.

# #### Nested list

# In[22]:


nested_list=[1,2,3,[4,5,6]]
nested_list


# In[24]:


nested_list2=[[1,2,3],[4,5,6],[7,8,9]]
nested_list2


# In[25]:


nested_list2[0][2]


# In[27]:


nested_list2[1:2]


# In[28]:


nested_list2[1:3]


# In[38]:


nested_list2[0:2:2]


# In[40]:


l2.clear()
l2


# In[41]:


nested_list2.extend([1,2,3])
nested_list2


# In[44]:


nested_list2.pop()
nested_list2


# In[45]:


nested_list2.extend([[1,2,3]])
nested_list2


# In[49]:


#### nested_list[list position].insert(pos in sub list,element)
nested_list2[1].insert(1,11)
nested_list2


# In[ ]:




