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

## 3. Clustering
In this projec we performed 2 step clustering. Firstly, we clustered our companies based on their location. 
We used custom KMeans with distance specified as haversine to take Earth's curve into consideration. Then we added geo-cluster labels to our dataframes, saved them and moved on to the second clustering.
In the second part (Model Building file) we used new data, preprocessed it and tried different models and metrics. Finally, we tried to interpret the output. What features are common in each cluster?

# Project summary 
The model we decided to choose was KMeans with 2 clusters. We achieved silhouette score around 0.87 as well as high minimal distance between different cluster, which means good cluster separation.
We confirmed our results with validation dataframe and moved on to interpretation. 
We noticed that the features most important for clustering are business opening hours. 
Companies that are mainly closed have been grouped as cluster 0 while open companies are cluster 1.
We plotted the results, as well as made a table showing which values of each feature appear in given cluster most often.
We came to the conclusion that to maximise the benefits of this clustering we can combine observations from both locaion and work-hours clustering, which led us to our final business goal...

# Business goal 💼
The main benefit of our project can be noticed by developers. By receiving a list of closed businesses in their area, they can create better spatial planning strategies and become interested in verifying whether the premises in which a particular business operated are indeed closed or for example undergoing renovation. This is because the reasons for closure can vary.