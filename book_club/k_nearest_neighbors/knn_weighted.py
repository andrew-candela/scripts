from __future__ import division
import numpy as np
import pandas as pd


#this is looseley related to the K nearest neighbors method
#I'll have a target location - I want to guess the value of a target variable based on the values 
#of other data points, weighted by distance from the target location

#let's restict ourselves to a unit square - pick some random points
x_pos=np.random.uniform(0,1,50)
y_pos=np.random.uniform(0,1,50)
#pick a random point as the target location 
target_location=np.random.uniform(0,1,2)
#pick some random values
target_value=np.random.standard_normal(50)
#build the dataframe
dataset=pd.DataFrame(zip(x_pos,y_pos,target_value))


#define a function that takes the dataset and a target point, and returns the estimate
def knn_weighted(data_df,point_to_estimate):
	"""data will be a data frame with 3 columns - ['x','y','val']. Point to estimate is an array of length 2"""
	data_df.columns=['x','y','val']
	#build distances into data_df
	data_df['distance']=np.sqrt(((data_df['x']-point_to_estimate[0])**2) + ((data_df['y']-point_to_estimate[1])**2))
	#the condition is that w[i]=distance[i]/total_distance
	total_distance=data_df.sum()['distance']
	data_df['weight']=np.reciprocal(total_distance)*data_df['distance']
	#estimate value
	data_df['weighted_scores']=data_df['val']*data_df['weight']
	estimate=data_df.sum()['weighted_scores']
	dataset.drop(['weighted_scores','distance','weight'],axis=1,inplace=True)
	return estimate


#run the script
estimate=knn_weighted(dataset,target_location)
print(estimate)
