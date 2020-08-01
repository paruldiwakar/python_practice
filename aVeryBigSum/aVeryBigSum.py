#!/usr/bin/env python
# coding: utf-8

# In[12]:


def aVeryBigSum(a,n):
    sum = 0
    for i in range(n):
        sum += a[i]
    return sum


# In[13]:


n = int(input())

a = [int(a) for a in input().split()]
print(aVeryBigSum(a,n))


# In[ ]:




