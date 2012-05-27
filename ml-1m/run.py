from __future__ import division
import pickle
from collections import defaultdict
from aff_clustering import *
from user_info import *

#Load the user and movie ratings dictionaries using pickle

user_rating_dict = pickle.load(open('user_rating_dict'))
movie_rating_dict = pickle.load(open('movie_rating_dict'))

# Now define the number of clusters ; it will be equal to the number of movies
no_of_movies = len(movie_rating_dict.keys())
k = 18 # Currently set to the number of genres

#Now let us perform one round of clustering and display the results
print 'The number of clusters is:' + str(k) + '\n'
points = user_info('users.dat')
clusters = kmeans(points,k)
#print clusters

'''
Initializing the affinity values for each of the data points.
Affinity values are stochastic for each of the data points. So initializing equal affinity scores for all the points
Investigate: Could it be a fuzzy set?
'''

init_affin = 1/k
aff_dict = defaultdict(list)
aff_list = []
for i in range(k):
	aff_list.append(init_affin)

for p in points:
	user_id = p[0]
	aff_dict[user_id] = aff_list
print aff_dict
