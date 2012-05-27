import pickle
from collections import defaultdict
def ratings_info(filename):
	user_dict = defaultdict(dict)
	movie_dict = defaultdict(dict)
	for line in open(filename):
		data = line.strip('\r\n').split('::')
		#print data
		user_id = int(data[0])
		movie_id = int(data[1])
		ratings = int(data[2])
		user_dict[user_id][movie_id] = ratings
		movie_dict[movie_id][user_id] = ratings
	return user_dict,movie_dict

user,movie = ratings_info('/home/such/Documents/Thesis/exp_new/Dataset/ml-1m/ml-1m/ratings.dat')
pickle.dump(user,open('user_rating_dict','wb'))
pickle.dump(movie,open('movie_rating_dict','wb'))

