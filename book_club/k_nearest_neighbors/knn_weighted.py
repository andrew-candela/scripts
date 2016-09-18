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
	#the condition is that w[i]/w[j] = distance[j]/distance[i]
	#or w[i]=w[min]*(d[min]*d[i])
	#impose the condition 1=w[min]*d[min]*sum(1/d[i])
	#this will let us solve for w[min]
	d_min=data_df.min()['distance']
	data_df['recip_distance']=np.reciprocal(data_df['distance'])
	weight_base=np.reciprocal(d_min * data_df.sum()['recip_distance'])
	#now I know the initial weight, let's calculate the full weight vector
	data_df['weight']=weight_base*d_min*np.reciprocal(data_df['distance'])	
	#estimate value
	data_df['weighted_scores']=data_df['val']*data_df['weight']
	return data_df.sum()['weighted_scores']


#run the script
estimate=knn_weighted(dataset,target_location)
print(estimate)