#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk 
from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer()
import random
import numpy as np
import re
import tflearn
import tensorflow as tf
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import RegexpTokenizer
import pickle
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.initializers import glorot_uniform
import numpy as np
from keras import layers
from keras.layers import Input, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D
from keras.layers import AveragePooling2D, MaxPooling2D, Dropout, GlobalMaxPooling2D, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
import json
import gensim


# In[2]:


with open(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\Medbot_Dataset.json','r',encoding='UTF-8') as file:
    data=json.load(file)


# In[5]:


try:
    model.load(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\MedBot_Words.bin')
except:
    model = gensim.models.KeyedVectors.load_word2vec_format(r"C:\Users\mjose\Desktop\COURSES\NLP\machine_learning_examples-master\large_files\GoogleNews-vectors-negative300.bin", binary=True)
    model.save_word2vec_format(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\MedBot_Words.bin',binary=True)


# In[6]:


try:
    with open(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\data.pickle','rb',encoding="UTF-8") as f:
        word, labels, train, output=pickle.load(f)
    
except:    
    words=[]
    labels=[]
    docs_x=[]
    docs_y=[]
    trains=[]
    outputs=[]
    missing=[]


    for intent in data['intents']:
            for code in intent['code']:
                line=code.strip()

                tokenizer = RegexpTokenizer(r'\w+')
                find=tokenizer.tokenize(line)
                words.extend(find)
                set=[]
                for sim in find:
                    if len(sim)>3:
                        setting=[]
                        try:
                            similar=model.most_similar(positive=[sim.lower()], topn = 5)
                            added=[i for i,j in similar]    
                            for w in added:
                                        
                                        w=w.split(",")
                                        setting.extend(w)

                        except KeyError:
                            missing.extend(sim)
                        
                        set.extend(setting)
                find.extend(set)
                words.extend(find)
                docs_x.append(find)
                docs_y.append(intent['tag'])
                   
            if(intent['tag'] not in labels):
                labels.append(intent['tag'])

    words=[(w.lower()) for w in words]
    words=sorted(words)
    word=[]
    for w in words:
        if w not in word:
            word.append(w)
    
    labels=sorted(labels)
    out_nul=[0 for _ in range(len(labels))]
    for x,y in enumerate(docs_x):
        bunch=[]
        line=[w.lower() for w in y]                    
        for w in word:
            if w.lower() in line:
                  bunch.append(1)
            else:
                  bunch.append(0)            
        one_hot_row=out_nul[:]
        one_hot_row[labels.index(docs_y[x])]=1
        trains.append(bunch)
        outputs.append(one_hot_row)

    train=np.array(trains)
    output=np.array(outputs)
    with open(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\data.pickle','wb') as f:
            pickle.dump((word,labels,train,output),f)


# In[74]:


def input_process(s,word):
    count_a=0
    count_b=0
    count_c=0
    out_a=0
    out_b=0
    out_c=0
    flag=0
    bag=[0 for _ in range(len(word))]
    line=s.strip()
    tokenizer = RegexpTokenizer(r'\w+')
    find=tokenizer.tokenize(line)
    find=[(w.lower()) for w in find]
    for j in find:
        for x,y in enumerate(word):
            if(y==j):
                bag[x]=1
    for i in range(len(output)):
        
        c=bag*train[i]
        d=np.sum(c)
        flag=max(flag,d)
        if d>count_a:
            count_c=count_b
            out_c=out_b
            count_b=count_a
            out_b=out_a  
            count_a=d
            out_a=i
            
        elif d>count_b:
            count_c=count_b
            out_c=out_b
            count_b=d
            out_b=i
        elif d>count_c:
            count_c=d
            out_c=i    
    return flag,out_a,out_b,out_c            


# In[75]:


s="dizziness"


# In[97]:


def talk():
    print(" The Conversation Begins : Type Stop To Quit\n")
    while True:
        inp=input("User: ")
        if inp.lower()=="stop":
            break
        flag,out_a,out_b,out_c=input_process(inp,word)
        if flag != 0:
            for intent in data["intents"]:
                for tg in intent["tag"]:
                    if docs_y[out_a]==tg.split(","):
                        print(random.choice(intent['response']))

            if out_a != out_b and out_a>33:
                    for intent in data["intents"]:
                        for tg in intent["tag"]:
                            if docs_y[out_b]==tg.split(","):
                                print(random.choice(intent['response']))

            if(out_b!=out_c and out_a!=out_c and out_a>33):
                for intent in data["intents"]:
                    for tg in intent["tag"]:
                        if docs_y[out_c]==tg.split(","):
                            print(random.choice(intent['response']))
        elif flag == 0:
            print("I didn't Understand What You Meant, Do not use shortforms and check for typos  ")


# In[98]:


talk()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




