# This file reads the user.dat file of the movie lens data set does some pre processing.
from point import Point
from read_movie_info import *
from movies_for_user import *

# The number of clusters is currently set to be the number of genres
k = 18

#Read user information and make points out of it

# Updated : Passing the bandit dictionary as another parameter
def user_info(filename,bandits):
	points = []

	for line in open(filename):
		data = line.strip('\r\n').split('::')
		sex = data[1]
		new_val = 0
		if sex == 'F':
			new_val = 1
		genres = rated_genre
		#p = [data[0],new_val,data[2],data[3]]
		p = [data[0], data[2],data[3]]
		to_int = lambda x:int(x)

		# Just converting everything to str; just in case
		p = map(to_int,p)

        # Make a point object from the point p
		point = Point(p,bandits)
		point.set_affinity() # Set affinity with k = 18 [ 18 Genres identified]
		points.append(point)
	return points



