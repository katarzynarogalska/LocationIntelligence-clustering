# Geospacial clustering 🌍

Geospacial clustering is used to detect areas that have similar features and group them together. In our project we are using [Location Data from Kaggle](https://www.kaggle.com/datasets/azharsaleem/location-intelligence-data-from-google-map).
This dataset provides information from Google Maps about business location,operations and customer interactions.
Given this features we will try to explore business trends and group similar objects together into clusters.

# Data overview 📄
In our dataframe we have columns like:
* business_id 
* phone_number
* name
* full_address
* **latitude**
* **longitude**
* review_count
* **rating**
* timezone
* website
* category
* claim_status
* plus_code
* geo_cluster
* country
* columns informing about working hours : Wednesday_morning 0-1 etc

# Milestones 🪨
## 1. EDA
The first part of our project is Exploratory Data Analysis. This part contains of:
* checking the size of our dataframe
* checking column types and the number of features
* detecting missing values
* data visualization : do we see a pattern?
* double checking the relevance of each feature : Is this feature important or is it just a noise?

## 2. Feature engineering
In the next step we try to fetch even more information from our data. Having  given features can we tell someting more about the business? 
In this part we will also check feature importance and drop irrelevant columns that can worsen future model's performance, as well as handle missing values and standardize numerical features or encode categorical ones. 

## 3. Modeling 
The last milestone is model selection. We will test out different models with different parameters and finally choose the best one for our project. Another important step in this part is to interpretate the model's output. What similarities are there between objects in every cluster? Why a certain business was classified to a certain cluster?

# Project summary ⏳
Comming soon...