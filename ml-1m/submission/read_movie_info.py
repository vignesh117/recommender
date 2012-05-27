from collections import defaultdict
from flatten import*

# Read movie info


def read_items(filename):
    items = {} 
    for line in open(filename):
        #1::Toy Story (1995)::Animation|Children's|Comedy
        data =  line.strip('\r\n').split('::')
        item_id = (str(data[0])).strip()
        item_name = data[1].strip()
        genres = data[2].split('|')
	genres = map(lambda x:x.strip(),genres)
        '''
        item = Item(item_id)
        item.add_data({'name': item_name, 'genres': genres})
        items[item_id] = item
        '''

	#Modifying item to hold only genres
        item = [genres]
        items[item_id] = item
    return items


#Creating a dictionary of movies categorized by genres.

def read_genre():
	movies = read_items('movies.dat')
	genres = []
	for m in movies.keys():
		genres+=movies[m][0]
	#print genres
	genres = list(set(genres))
	#print genres	
	#create a genre dictionary
	genre_dict = defaultdict(list)
	for m in movies.keys():
		movie_genres = movies[m][0]
		for g in movie_genres:
			prev_movies = genre_dict[g]
			new_movies = prev_movies + [m]
			genre_dict[g].append(m)
	return genre_dict
	
def get_movie_name(movie_id):
	movies = read_items('movies.dat')
	try:
		genre = movies[movie_id]
		return genre
	except KeyError:
		return 0
			
def get_genre(movie_id):
	movies = read_items('movies.dat')
	try:
		genre = movies[movie_id]
		return flatten(genre)
	except KeyError:
		return 0
			

# Call it!
