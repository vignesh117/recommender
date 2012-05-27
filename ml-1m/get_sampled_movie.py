def get_sampled_movie():
	ratings_file = open('ratings.dat')
	movies = [x.split('::')[1] for x in ratings_file.readlines()]
	movie_file = open('movies.dat')
	movie_info = [y for y in movie_file.readlines() if y.split('::')[0] in movies]
	sampled_movie = open('sampled_movie','wb')
	for m in movie_info:
		sampled_movie.write(m)
	sampled_movie.close()
get_sampled_movie()
