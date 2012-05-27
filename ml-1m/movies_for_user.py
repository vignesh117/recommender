from __future__ import division
from flatten import *
from read_movie_info import get_genre,read_genre

genre_dict = read_genre()
fname = 'ratings.dat'
content = []
for line in open(fname):
	data = line.strip('\r\n').split('::')

	# Get the list of movies 
	content.append(data)
def movies_for_user(uid,mid):
	movie_info = [(x[1],x[2]) for x in content if x[0] == str(uid[0]) ]
	avg_user_rating = sum([int(x[1]) for x in movie_info])/len(movie_info)
	#print movie_info

	# movie_info gets the list of movies rated by the user.
	# Get the genre of the recommended movie

	# Get the genres corresponding to the recommended movie and get the list of all movies in that genre
	recommended_genre = get_genre(str(int(mid)))
	#print recommended_genre
	#recommended_genre = gen
	movie_genre = flatten([genre_dict[x] for x in recommended_genre])
	#print movie_genre
	#print movie_genre

	#Now get the ratings of all the movies rated by the user whose genre corresponds to the recommended movie
	reqd_movie = flatten([m[1] for m in movie_info if m[0] in movie_genre])
	reqd_movie = map(lambda x:int(x),reqd_movie)
	try:
		print (sum(reqd_movie)/len(reqd_movie),avg_user_rating) 
	except ZeroDivisionError:
		print 0,0
	# Now we need to 
#print movies_for_user([119,1,1],'2019')
def rated_genre(uid): # For this give the exact user id. This is used by the point class
	fname = 'ratings.dat'
	content = []
	for line in open(fname):
		data = line.strip('\r\n').split('::')

		# Get the list of movies 
		content.append(data)
	movie_info = [(x[1],x[2]) for x in content if x[0] == str(uid) ]
	genres =  flatten([get_genre(m[0]) for m in movie_info])
	genres = filter(lambda x:x!=0 ,genres)
	return list(set(genres))


