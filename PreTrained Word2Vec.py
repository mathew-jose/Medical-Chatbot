#!/usr/bin/env python
# coding: utf-8

# In[5]:


import gensim


# In[7]:


model = gensim.models.KeyedVectors.load_word2vec_format(r"C:\Users\mjose\Desktop\COURSES\NLP\machine_learning_examples-master\large_files\GoogleNews-vectors-negative300.bin", binary=True)
    


# In[10]:


similar=model.most_similar(positive=['happy'], topn = 10)


# In[13]:


sim=[i for i,j in similar]
print(sim)


# In[ ]:





# In[ ]:




