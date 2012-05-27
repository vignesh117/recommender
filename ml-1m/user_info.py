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

def info2(filename,bandits):
	points = []
	data = [x for x in open(filename).readlines()]
	data = map(lambda x:x.strip('\r\n').split('::'),data)
	ids  = list(set([x[0] for x in data]))
	sexes  = list(set([x[1] for x in data]))
	ages  = list(set([x[2] for x in data]))
	occs  = list(set([x[3] for x in data]))

	# Now form the user profile vector by collating bit vectors 
	for d in data:

		#Some initialization
		user_id = d[0]
		user_age = [0 for i in range(len(ages))]
		user_occ = [0 for i in range(len(occs))]
		
		#Update user_age
		age_index = ages.index(d[2])
		user_age[age_index] = 1

		#Update user_occ 
		occ_index = occs.index(d[3])
		user_occ[occ_index] = 1

		# Update sex
		sex = 0
		if d[1] == 'M':
			sex = 1

		# Create user profile by collating all vectors
		profile = [user_id] + [sex] + user_age + user_occ
		profile = map(lambda x:int(x), profile)

		#Create the point object and 
		point = Point(profile,bandits)
		point.set_affinity()
		points.append(point)
		points.append(point)
	return points


