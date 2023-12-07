#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Portfolio Project - Web Scraping Largest Companies by Revenue
#Skills Used: Web Scraping with BeautifulSoup, importing data into Pandas


# # Web Scraping with BeautifulSoup

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[7]:


URL = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html')


# In[8]:


print(soup)


# In[12]:


table = soup.find_all('table')[1]
print(table)


# In[16]:


public_titles = table.find_all('th')


# In[19]:


public_table_titles = [title.text.strip() for title in public_titles]
print(public_table_titles)


# # Importing into Pandas Dataframe

# In[20]:


import pandas as pd


# In[42]:


df = pd.DataFrame(columns = public_table_titles)
df


# In[43]:


column_data = table.find_all('tr')


# In[44]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data


# In[45]:


df


# In[ ]:





# In[47]:


df.to_csv(r'C:\Users\KayleighMacdonald\Documents\Largest_Companies.csv', index = False)


# In[ ]:




