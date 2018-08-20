
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups


# In[2]:



def load_data(option='train'):
    newsgroups_train = fetch_20newsgroups(subset=option,
                                          remove=('headers', 'footers', 'quotes'))


    # In[3]:


    newsgroups_train.keys()


    # In[4]:


    len(newsgroups_train.data)


    # In[5]:


    newsgroups_train.target


    # In[10]:


    newsgroups_train.keys()


    # In[14]:


    df_train = pd.DataFrame(newsgroups_train.data, columns=['data'])


    # In[19]:


    df_train['target'] = newsgroups_train.target


    # In[22]:


    df_train['targetnames'] = df_train['target'].apply(lambda n: newsgroups_train.target_names[n])


    # In[25]:


    df_train.to_csv(f'data/data_{option}.csv', index=None)





