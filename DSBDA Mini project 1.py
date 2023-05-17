#!/usr/bin/env python
# coding: utf-8

# ## DSBDA Mini Project - Group C
Name - 1) Prajakta Pramod Ghanwat , Roll No - 2231044
       2) Sujata Mahadev Gawali , Roll No - 2231046
# ### Problem Statement
# Use the following covid_vaccine_statewise.csv dataset and perform following analytics on the
# given dataset
# https://www.kaggle.com/sudalairajkumar/covid19-in-india?select=covid_vaccine_statewise.csv
# a. Describe the dataset
# 
# b. Number of persons state wise vaccinated for first dose in India
# 
# c. Number of persons state wise vaccinated for second dose in India
# 
# d. Number of Males vaccinated
# 
# d. Number of females vaccinated

# In[1]:


# Importing the required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Reading the csv file
data = pd.read_csv("covid_vaccine_statewise.csv")


# In[3]:


# Top five rows
print("The top five rows are: ")
data.head()


# In[4]:


# Last five rows
print("The last five rows are: ")
data.tail()


# In[5]:


# Shape of the dataset in the format of (rows, columns)
print("The shape is: ")
data.shape


# In[6]:


# Names of columns
print("The columns present in the dataset are: ")
data.columns


# ### Describe the dataset

# #### To describe the dataset, we use describe() function. It gives the output as mean, maximum, minimum, count etc

# In[7]:


data.describe()


# In[8]:


data.describe(include='object')


# In[9]:


# Information about the dataset
data.info()


# In[10]:




data.isnull().sum()


# ### For First Dose Administered 

# In[11]:


# Average of First Dose Administered
avg_firstdose = data["First Dose Administered"].astype("float").mean(axis = 0)
print("Average of First Dose:", avg_firstdose)


# In[12]:


# Replacing First Dose Administered
data["First Dose Administered"].fillna(value = avg_firstdose, inplace=True)
data


# ### For Second Dose Administered

# In[13]:


# Average of Second Dose Administered
avg_seconddose = data["Second Dose Administered"].astype("float").mean(axis = 0)
print("Average of Second Dose:", avg_seconddose)


# In[14]:


# Replacing Second Dose Administered
data["Second Dose Administered"].fillna(value = avg_seconddose, inplace = True)
data


# #### Number of persons state wise vaccinated for first dose in india

# In[15]:


first_dose = data.groupby('State')[['First Dose Administered']].sum()
first_dose


# ### Number of persons state wise vaccinated for second dose in india

# In[16]:


first_dose = data.groupby('State')[['Second Dose Administered']].sum()
first_dose


# ### Number of Males vaccinated

# In[17]:


male = data["Male(Individuals Vaccinated)"].sum()
print("The total number of male individuals vaccinated are", int(male))


# ### Number of females vaccinated

# In[18]:


female = data["Female(Individuals Vaccinated)"].sum()
print("The total number of female individuals vaccinated are", int(female))

