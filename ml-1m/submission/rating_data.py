from collections import defaultdict
'''
from recsys.datamodel.data import Data

filename = '/home/such/Documents/Thesis/exp_new/Dataset/ml-1m/ml-1m/ratings.dat'

data = Data()
format = {'col':0, 'row':1, 'value':2, 'ids': 'int'}
    # About format parameter:
    #   'row': 1 -> Rows in matrix come from column 1 in ratings.dat file
    #   'col': 0 -> Cols in matrix come from column 0 in ratings.dat file
    #   'value': 2 -> Values (Mij) in matrix come from column 2 in ratings.dat file
    #   'ids': int -> Ids (row and col ids) are integers (not strings)
data.load(filename, sep='::', format=format)
train, test = data.split_train_test(percent=80) # 80% train, 20% test
print test.get()
'''
def read_ratings(filename):
	user_ratings = defaultdict(defaultdict) 
	for line in open(filename):
		data = line.strip('\r\n').split('::')

		#Always convert the userid to str
		user_id = str(data[0])
		movie_id = data[1]
		rating = data[2]
		timestamp = data[3]

		# User ratings is a double dict with the movie id as the second key
		user_ratings[user_id][movie_id] = rating
	
	return user_ratings


#print read_ratings('/home/such/Documents/Thesis/exp_new/Dataset/ml-1m/ml-1m/ratings.dat')
