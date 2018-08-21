
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords


stopswords_english = set(stopwords.words('english'))

def tokenize_and_clean_text(s):
    return [token.lower() for token in wordpunct_tokenize(s) 
            if token.isalpha() 
            and token.lower() not in stopswords_english]

def tokenize_dataset(input_csv_file):
    output_csv_file = input_csv_file.replace('.csv', '_tokenized.csv')


    # In[3]:


    df = pd.read_csv(input_csv_file)
    df.head()


    df = df.dropna()


    # In[7]:


    df['data'] = df['data'].apply(tokenize_and_clean_text)


    # In[8]:


    df.head()


    # In[9]:


    df.to_csv(output_csv_file, index=False)
