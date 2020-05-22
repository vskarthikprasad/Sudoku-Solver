#!/usr/bin/env python
# coding: utf-8

# In[7]:


grid=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# In[8]:


import numpy as np
print(np.matrix(grid))


# In[9]:


def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n :
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x_new=(x//3)*3
    y_new=(y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[i+y_new][j+x_new] == n:
                return False
    return True
        


# In[10]:


possible(4,4,5)


# In[11]:


def solve():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if possible(i,j,k): 
                        grid[i][j] = k
                        solve()
                        grid[i][j] = 0
                return
    print(np.matrix(grid))
    input("More?")


# In[12]:


solve()


# In[ ]:




