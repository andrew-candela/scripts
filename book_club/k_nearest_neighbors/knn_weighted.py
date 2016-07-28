from __future__ import division
import numpy as np
import pandas as pd


#this is looseley related to the K nearest neighbors method
#I'll have a target location - I want to guess the value of a target variable based on the values 
#of other data points, weighted by distance from the target location

#this takes a really long time to run. I'll bet there are all kinds of optimizations I can make

#let's restict ourselves to a unit square
x_pos=np.random.uniform(0,1,50)
y_pos=np.random.uniform(0,1,50)

#pick a random point
target_location=np.random.uniform(0,1,2)

#pick some random values
target_value=np.random.standard_normal(50)

#build the dataframe
dataset=pd.DataFrame(zip(x_pos,y_pos,target_value))
dataset.columns=['x','y','val']
dataset['distance']=np.sqrt(((dataset['x']-target_location[0])**2) + ((dataset['y']-target_location[1])**2))

#now I have the value and the distance from the target point right in the data frame.
#I need to do a little math to figure out the weights...

#the condition is that w[i]/w[j] = distance[j]/distance[i]
#or w[i]=w[min]*(d[min]*d[i])

#impose the condition 1=w[min]*d[min]*sum(1/d[i])
#this will let us solve for w[min]

d_min=dataset.min()['distance']

dataset['recip_distance']=np.reciprocal(dataset['distance'])
weight_base=np.reciprocal(d_min * dataset.sum()['recip_distance'])

#now I know the initial weight, let's calculate the full weight vector
dataset['weight']=weight_base*d_min*np.reciprocal(dataset['distance'])

#check if the wieghts sum to 1
#print(dataset.sum()['weight'])

#estimate value

dataset['weighted_scores']=dataset['val']*dataset['weight']
print(dataset.sum()['weighted_scores'])
