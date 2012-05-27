# Find the average ratings for a given movie from all the users in the given cluster

from __future__ import division
from rating_data import *
ratings_dict = read_ratings('ratings.dat')
def find_movie_rating(c,cid,mid):

	# Get the ratings dictionary

	# Get all the points in the cluster, cid
	points_in_cluster = []
	for p in c.keys():
		if c[p] == cid:
			points_in_cluster.append(p)

	# Get the ratings value for the points in the cluster
	total_ratings = []
	users_support = 0
	for p in points_in_cluster:

		#Always convert the user ratings to str
		p = str(p)
		rating_val = ratings_dict.get(p).get(mid)
		if rating_val != None:
			total_ratings.append(int(rating_val))
			users_support+=1
		else:
			continue
	if users_support == 0 :
		return 0
	else:
		return sum(total_ratings) / users_support
