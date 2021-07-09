#!/usr/bin/env python
# coding: utf-8

# In[1]:


def file_length(file_name):
    file = open(file_name)
    contents = file.read()
    file.close()
    print(len(contents))


# In[ ]:




