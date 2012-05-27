from __future__ import division
from __future__ import division
from read_movie_info import *

def tester():
	ratings_file = open('ratings.dat')
	user = '5'
	user_rating = ['4','5']
	movies = []
	movie = '1964'
	for line in ratings_file.readlines():
	    temp = line.split('::')
	    info = (temp[0],temp[1],temp[2])
	    movies.append(info)

	for_user = [x[1] for x in movies if x[0] == user and x[2] in user_rating]
	print map(get_movie_name,for_user)
tester()
