from __future__ import division
from collections import defaultdict
import random
class Point():

	def __init__(self, value =None ,bandits = None):

		self.value = value
		self.bandits = bandits
		self.affinity = {}
		#self.Q_values = None
		
		
		
	def set_affinity(self):
		n = len(self.bandits.keys())
		#print n
		norm = 1/n
		bandits = self.bandits
		for b in bandits.keys():
			self.affinity[b] = norm
	'''

	def set_Q(self):
		"""
		Returns a dictionary of Q values for each of the bandits
		"""
		n = self.n
		actions = self.actions
		Q_dict = {}
		for i in range(n):
			act_list = []
			act_prob = 1/len(actions)
			for j in range(len(actions)):
				act_list.append(act_prob)
			Q_dict[i] = act_list
		return Q_dict
	'''

	# Need to write code for modifying the affinity score.

	def update_affinity(self,avg_rew,bandit):
		# increase or decrease the probability of a given bandit
		beta = 0.05
		bandit_value = self.affinity[bandit]
		if bandit_value == []:
			bandit_value = 0
		bandit_value = bandit_value + beta * avg_rew

		# Update the new affinity value to the corresponding bandit
		self.affinity[bandit] = bandit_value
		all_values = self.affinity.values()
		#Normalize the values once again.
		'''
		total_values = sum(all_values)
		for b in self.affinity.keys():
			val = self.affinity[b]
			if total_values == 0:
				print 'It was Zero'
				self.affinity[b] = val
			else:
				new_val = val / total_values
				self.affinity[b] = new_val
		'''
		#print 'updated affinity'
		
		#print self.affinity



	def sample_bandit(self):
		"""Sample a bandit according to softmax

		Arguments:
		- `self`:
		"""
		aff = self.affinity.values()
		randomizer = lambda x:x+random.random()
		rand_aff = map(randomizer,aff)
		index =  aff.index(max(aff))
		max_value = max(aff)
		choices = [i for i in range(len(aff)) if aff[i] == max_value]
		index = random.choice(choices)
		return self.affinity.keys()[index] # Returns the name of the bandit rather than the index



