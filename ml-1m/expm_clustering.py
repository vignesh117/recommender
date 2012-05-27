from __future__ import division
from user_info import *
from aff_clustering import *
from read_movie_info import *
from bandit import *
from point import *
from rating_data import *
from find_missing_rating import *
from movies_for_user import *
from collections import OrderedDict as od
from collections import Counter

#Now create bandits 
#total_bandits = range(0,k)
movie_dict = read_genre() # This gives us the actions for each of the bandits. Here the actions are movies specific to a genre
b_keys = movie_dict.keys()
bandit_dict = od() # using ordered dictionary to retain the order in which the bandits are added.

bandits = [] # list of bandit objects 
for b in b_keys:
	acts = movie_dict[b]
	bandit = Bandit(b,acts)
	bandit.set_count()
	bandit_dict[b] = bandit

# Getting the point class information 
#25-05 modifying the user info function to info2. Refer to V3 changes for the changes
points = info2('users.dat',bandit_dict)
#print points[0]

#print points

point_values = [x.value for x in points]

#Set the Q values for each of the points
for b in bandit_dict.values():
	for p in points:
		b.set_Q(p)

# Initialize some values


# sample some users for testing and recommendation
sample_users = [random.choice(points) for i in range(1,2)]


# Sample a 
def play(p,round):
	#print 'Playing round: '+str(round)
	sample_p = p

	# Maintain an affinity update counter
	aff_thresh = 5
	aff_count = 0

	#Maintain rewards for each of the bandits for affinity update
	band_rew_dict = defaultdict(list)

	# Maintain the arm pulled, for validating clusters

	for i in range(30):

		sampled_b =  sample_p.sample_bandit() #This just returns the string, Sci-fi,Horror etc
		band = bandit_dict[sampled_b] # This gives us the actual bandit

		
		arm = band.pull_arm(sample_p)

		# Change here is that we need update q values for all the bandits that the arm belonged to.

		genres = get_genre(arm)

		for g in genres:
			band = bandit_dict[g]
			band.get_reward(sample_p,arm,clusters,sampled_b)

		# Rewards are acculmuated for calculating the affinity
			rew = band.reward
		#rewards.append(rew)
			band_rew_dict[band.name].append(rew)

		#print 'Reward obtainted: '+ str(rew)
			band.update_Q(arm,sample_p)

		# You should be passing the name of the bandit
		
		if aff_count == aff_thresh:
			print 'updating affinity'
			for b in band_rew_dict.keys():
				rewards = band_rew_dict[b]
				avg_rew = sum(rewards) / len(rewards)
				sample_p.update_affinity(avg_rew,band.name)
				aff_count = 0
			band_rew_dict = defaultdict(list)
		else:
			aff_count+=1
	return sampled_b

def recommend(p,clusters):
	""" This recommends a movie to a user based on the cluster it belongs to """
	#print 'New affinity: ' + str(sample_p.affinity)
	#print band.Q_dict[sample_p.value[0]]
	cno = clusters[p.value[0]] # This is the cluster dict which gives the final clustering of the point
	new_band = bandit_dict[bandit_dict.keys()[cno]] # Bandit is chosen based on the cluster no
	print new_band.name
	'''
	new_band_sam = p.sample_bandit()
	new_band = bandit_dict[new_band_sam]
	'''
	new_arm = new_band.pull_arm(sample_p)
	#print str(p.value)+' : ' + str(new_arm)
	#print '\n'
	new_band.get_reward(p,new_arm,clusters,new_band.name)
	#print new_band.reward
	return new_arm

'''
# Testing the missing value problem
movie_ratings = read_ratings('ratings.dat') # Read movie ratings
p = random.choice(points)

#Always convert userid to str
p_value = str(p.value[0])
m = ""
flag = 0
while flag == 0:
	sampled_b = p.sample_bandit()
	band = bandit_dict[sampled_b]
	arm = band.pull_arm(p)
	if movie_ratings.get(p_value).get(arm) == None:
		flag = 1
		m = arm

print "old Rating = "+ str(movie_ratings.get(p_value).get(arm))

# Find the cluster corresponing to p
cid = clusters[p_value] 
print cid

# Find the rating
rating = find_movie_rating(clusters,cid,m)
print "New rating = " +str(rating)
'''


k = 18 # Some dummy value; actually this should be the number of movies
clusters = kmeans(points,k,None)
#print clusters
round = 0
for s in sample_users:

	#Sample a point and play the game
	sample_p = s 

	#play and learn the values
	band = play(sample_p,round)
	round+=1
	
	
	# Perform clustering 
	clusters = kmeans(points,k,band,clusters)
	#print clusters

	#Play another round
	band = play(sample_p, round)
	round+=1
	

	# Another round of clustering
	clusters = kmeans(points,k,band,clusters)
	#print clusters

	#Another round of play and recommend
	band = play(sample_p,round)
	
	
'''
# Now to generalize for unknown points
sample_points = [random.choice(points) for i in range(100)]
for s in sample_points:
	recommend(s)
'''

for s in sample_users:
	sample_p = s
#Recommendation for the known points
	r = []
	for i in range(1,10):
		r.append(recommend(sample_p,clusters))
		c = Counter(r)
	recommended = [x for x in c.keys() if c[x] == max(c.values())][0]
	print str(sample_p.value)+':'+str(recommended)
    
#print 'Point is: ' + str(sample_p.value[0])
#print 'Old affinity: ' + str(sample_p.affinity)

