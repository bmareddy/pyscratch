
# coding: utf-8

# In[2]:


import spacy


# In[3]:


nlp = spacy.load("en_core_web_lg")


# In[5]:


len(nlp.vocab)


# In[7]:


nlp.vocab.strings["apple"]


# In[8]:


len(nlp.vocab.vectors)


# In[10]:


print(type(nlp.vocab),type(nlp.vocab.vectors))


# In[4]:


for word in nlp.vocab:
    pass
print(list(word.vocab.strings))


# In[5]:


print("Hello")


# In[6]:


for key, vector in nlp.vocab.vectors.items():
    print(key, nlp.vocab.strings[key], vector)


# In[8]:


print (key)


# In[15]:


from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import random as rand


# In[12]:


cosine_similarity(vector.reshape(1,300),vector.reshape(1,300))


# In[13]:


space = "DMT"
wd = "C:\\Users\\bmareddy\\Documents\\PyLab\\data"
inFileVecs = "{}\\{}_tags_vectors.json".format(wd,space)


# In[16]:


pageVectors = [json.loads(pv) for pv in open(inFileVecs,"r").read().splitlines()]
page_pos = rand.randint(0,len(pageVectors))
print ("Finding words for page: {}".format(pageVectors[page_pos]["pageTitle"]))


# In[17]:


source_vec = np.asarray(pageVectors[page_pos]["vector"])


# In[38]:


by_similarity = [(word.text.lower(), np.asscalar(cosine_similarity(source_vec.reshape(1,300),word.vector.reshape(1,300)))) for word in nlp.vocab if word.prob >= -15]


# In[43]:


sorted_similarity = sorted(list(set(by_similarity)), key = lambda x: x[1], reverse = True)


# In[44]:


len(sorted_similarity)


# In[20]:


sorted_similarity[:5]


# In[25]:


print(nlp.vocab[745513800644165557].text,
nlp.vocab[16396066478604633435].text,
nlp.vocab[15830540981292950885].text,
nlp.vocab[3767271857074311788].text,
nlp.vocab[2781019763248568108].text)


# In[46]:


sorted_similarity[:5]


# In[47]:


page_pos = rand.randint(0,len(pageVectors))
print ("Finding words for page: {}".format(pageVectors[page_pos]["pageTitle"]))
source_vec = np.asarray(pageVectors[page_pos]["vector"])
by_similarity = [(word.text.lower(), np.asscalar(cosine_similarity(source_vec.reshape(1,300),word.vector.reshape(1,300)))) for word in nlp.vocab if word.prob >= -15]
sorted_similarity = sorted(list(set(by_similarity)), key = lambda x: x[1], reverse = True)


# In[48]:


sorted_similarity[:5]


# In[49]:


nlp.vocab.strings["mef"]


# In[52]:


nlp.vocab.strings["meffghksdhj"]


# In[56]:


vector = nlp.random.uniform(-1, 1, (300,))
key = nlp.vocab.strings[u"mef"]
nlp.vocab.vectors.add(key, vector=vector)

