#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


# Load the dataset
airbnb_data = pd.read_csv('seattle_listings.csv')
# Check the shape and column names
print("Shape of the dataset:", airbnb_data.shape)
print("Column names:", airbnb_data.columns)


# In[12]:


# Data Cleaning
# Check for missing values
print("Missing values in each column:\n", airbnb_data.isnull().sum())


# In[15]:


# Check for duplicates
print("Number of duplicates:", airbnb_data.duplicated().sum())


# In[20]:


# Check for outliers
# Check the distribution of the price column using a box plot
#airbnb_data['price'] = airbnb_data['price'].astype(float) # show error to solve this convert 
airbnb_data['price'] = airbnb_data['price'].str.replace(',', '').str.replace('$', '').astype(float)
plt.boxplot(airbnb_data['price'])
plt.show()


# In[21]:


# Data Exploration
# Calculate descriptive statistics
print("Descriptive statistics for the price column:\n", airbnb_data['price'].describe())



# In[22]:


# Visualize the distribution of the price column using a histogram
plt.hist(airbnb_data['price'], bins=20)
plt.show()


# In[29]:


# Data Preparation
# Select the necessary columns for analysis
selected_columns = ['id', 'name', 'neighbourhood_group_cleansed', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'price']
airbnb_data_selected = airbnb_data[selected_columns]


# In[31]:


# Convert data types if required
airbnb_data_selected['price'] = airbnb_data_selected['price'].astype(str).str.replace('$', '').str.replace(',', '').astype(float)


# In[32]:


# Feature Engineering
# Calculate price per square foot
airbnb_data_selected['price_per_sqft'] = airbnb_data_selected['price'] / (airbnb_data_selected['bedrooms'] * airbnb_data_selected['accommodates'])


# In[33]:


# Data Analysis
# Calculate average price per night
avg_price = airbnb_data_selected['price'].mean()
print("Average price per night: ${:.2f}".format(avg_price))


# In[34]:


# Calculate the most expensive location
most_expensive_location = airbnb_data_selected.loc[airbnb_data_selected['price'] == airbnb_data_selected['price'].max(), 'neighbourhood_group_cleansed'].values[0]
print("Most expensive location:", most_expensive_location)


# In[36]:


# Calculate the busiest time of the year
airbnb_data_calendar = pd.read_csv('seattle_calendar.csv')
airbnb_data_calendar['date'] = pd.to_datetime(airbnb_data_calendar['date'])
airbnb_data_calendar['month'] = airbnb_data_calendar['date'].dt.month
airbnb_data_calendar_grouped = airbnb_data_calendar.groupby(['month'])['available'].count()
busiest_month = airbnb_data_calendar_grouped.idxmax()
print("Busiest month of the year:", busiest_month


# In[37]:


# Visualization
# Visualize the relationship between the price and the number of bedrooms using a scatter plot
plt.scatter(airbnb_data_selected['bedrooms'], airbnb_data_selected['price'])
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')
plt.show()


# In[38]:


# Visualize the relationship between the price and the property type using a bar chart
airbnb_data_selected_grouped = airbnb_data_selected.groupby(['property_type'])['price'].mean().sort_values(ascending=False)
plt.bar(airbnb_data_selected_grouped.index, airbnb_data_selected_grouped.values)
plt.xticks(rotation=90)
plt.xlabel('Property Type')
plt.ylabel('Average Price')
plt.show()


# In[53]:


#Conclusion
#Summarize the findings
print("Based on the analysis of Airbnb rental data for Seattle, we found that the average price per night is ${:.2f} and the most expensive location is {}.".format(avg_price, most_expensive_location))

