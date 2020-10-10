#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("largest element in the list is :", max(lst)),


# In[2]:


lst=[12,34,56,78,90,87]
lst.sort(reverse=True)
print("second largest number of the list is:{}".format(lst[1]))


# In[3]:


lst_1=[90,87,67,54,34,12]
lst_2=[12,34,56,78,90,65]
lst_merged=lst_1+lst_2
lst_merged.sort()
lst_merged


# In[4]:


mylist=[12,35,9,56,24]
size=len(mylist)
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print("list after swapping:",mylist)


# In[ ]:




