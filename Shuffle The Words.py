#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random
import nltk
from nltk.tokenize import RegexpTokenizer


# In[ ]:





# In[ ]:





# 

# In[2]:


with open(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\Medbot_Dataset.json','r',encoding='UTF-8') as file:
    data=json.load(file)
train = [[] for i in range(1000)]


# In[3]:


i=0
for intent in data['intents']: 
     for tag in intent['tag']:   
        for code in intent['code']:
                tokenizer = RegexpTokenizer(r'\w+')
                line=tokenizer.tokenize(code)
                for j in range(len(line)):
                    find1=line[:]
                    random.shuffle(find1)
                    find2=" ".join(find1)
                    if find2 not in train[i]:
                        train[i].append(find2)
                    print(find2)
     i=i+1    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


with open(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\Final_Medbot_Dataset.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


# In[ ]:




