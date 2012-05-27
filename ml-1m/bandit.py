from __future__ import division
from collections import defaultdict
from rating_data import *
from find_missing_rating import *
from movies_for_user import *
import random

user_ratings = read_ratings('ratings.dat')
reward_dict = {}
reward_dict['5'] = 0.5 
reward_dict['4'] = 0.2
reward_dict['3'] = -0.3
reward_dict['2'] = -0.5
reward_dict['1'] = -0.6
reward_dict['0'] = -0.7
#reward_dict[None] = 0

class Bandit(object):

	def __init__(self,name =None, actions = None):

		self.name = name
		self.actions = actions
		self._reward = None
		self.count_actions = defaultdict() 
		self.Q_dict = defaultdict(list)
		
	def set_count(self):
		actions = self.actions
		for a in actions:
			self.count_actions[a] = 0
	
	
	def set_Q(self,p):
	
		actions = self.actions
		user = str(p.value[0])
		temp_Q = []
		Q_est = 1/len(actions)
		for i in range(len(actions)):
			self.Q_dict[user].append(Q_est)	
	def pull_arm(self,p):
		
		user = str(p.value[0])
		actions = self.actions
		epsilon = 0.4
		random_value = random.random()
		if random_value <= epsilon:
			return random.choice((actions))
		else:
			greedy_val = max(self.Q_dict[user])
			all_vals = self.Q_dict[user]
			choices = []
			action_index = 0
			for i in range(len(all_vals)):
				if greedy_val == all_vals[i]:
					choices.append(i)
		choice = random.choice(choices)
		return actions[choice]
	def update_Q(self,action,p):
		"""Updates the Q estimates based on the rewards
	
		Arguments:
		- `self`:
		"""
		user = str(p.value[0])
		reward = self.reward
		n = len(self.actions)
		count = self.count_actions[action]
		if self.Q_dict.get(user) == None:
			self.set_Q(p)
		previous_Q = self.Q_dict[user][self.actions.index((action))]
		
		#Doing an online mean update for the Q value for the given action
		new_Q = previous_Q + ((previous_Q + reward) / n)
		self.Q_dict[user][self.actions.index(action)] = new_Q


	def get_reward(self,p,action,clusters,bandit):
		#print bandit
		action = str(action)
		user = str(p.value[0])
		seen_genre = rated_genre(user)
		#print seen_genre
		rating = user_ratings.get(user).get(action)
		if rating == None:
			#self.reward = 0
			# Get the cluster id of the user
			cid = clusters[int(user)]
			rating = find_movie_rating(clusters,cid,action)
			rating = int(rating)
			reward = reward_dict[str(rating)]
			self.reward = reward

		# If the user has not seen that genre, penlize the bandit
		elif bandit not in seen_genre:
			#print 'I havn seen this'
			self.reward = -0.8

		else:
			actual_rating = user_ratings.get(user).get(action)
			reward = reward_dict[actual_rating]
			self.reward = reward



