#!/usr/bin/env python
# coding: utf-8

# In[7]:


def compareTriplets(a,b):
    score = [0,0]
    for i in range(3):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
    return score


# In[11]:


a = [int(a) for a in input().split()]
b = [int(b) for b in input().split()]
compareTriplets(a,b)


# In[ ]:




