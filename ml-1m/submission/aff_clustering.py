from pylab import *
from flatten import *
import math,random,pickle
from collections import defaultdict
#from matplotlib import pyplot

# Finding the eucledean distance between two points
def getDistance(a, b):
	
	if len(a) != len(b):
		#print 'coordinates do not match'
		exit(0)

	ret = 0.0
	for i in range(len(a)): # Now considering only age and occupation
		ret = ret + pow((a[i] - b[i]),2)
	return math.sqrt(ret)
	

# I should build a dictionary with userid as the key and the cluster number as the value -- possible

#Given a set of points in the cluster, the centroid would be just the mean of all the points in the cluster.
def calculateCentroid(points):
	#print points
	#print 'I was called'
	centroids = []
	
	
	for i in range(len(points[0])):
		centroids.append(0.0)
		for p in points:
			centroids[i] = centroids[i] + p[i]
		centroids[i] = centroids[i]/len(points)
	return centroids
	
	'''
	# Just working with numeric attributes
	centroids = [[i[2]/len(points),i[3]/len(points)] for i in points]
	centroids = flatten(centroids)
	'''
	

	return centroids
#K-means Clustering
def kmeans(points,k, arm = None,old_cluster = None,m=50):
	#print 'Performing Clustering'	
	threshold = 0.03
# initally randomly selected k points will be centroids
	point_values = [x.value for x in points] # Given are point objects
	initial = random.sample(point_values,k)
	clusters = []
	
	#This is an alternative result; it returns a list of cluster numbers corresponding to the ordering of points in the points array.
	point_wise_clusters = []
	point_dict = {}
	
	#Now adding just the cluster centroids generated to the clusters
	for p in initial:
		clusters.append([p])
	#print clusters[0]	
	count = 0
		
	#Now, perform the clustering
	while count <=m :
		cluster_list = []
		for c in clusters:
			cluster_list.append([])
		for p in points:
			pv = p.value
			if old_cluster == None:
				oc = -1
			else:
				oc = old_cluster[pv[0]]
			dist = getDistance(pv,calculateCentroid(clusters[0]))
			#print dist
			index = 0
			for i in range(len(clusters[1:])):
				distance = getDistance(pv,calculateCentroid(clusters[i+1]))
				if distance < dist and validate_constraints(clusters[i+1],threshold,p,oc,arm) == True:
					dist = distance
					index = i+1
				else:
					continue
			cluster_list[index].append(pv)
			point_wise_clusters.append(index)
			
			# userid is the first feature in the cluster
			user_id = pv[0]
			point_dict[int(user_id)] = int(index)
		#print 'I came above'
		'''
		if count >= m:
			print 'I came here'
			break
		else:
			count+=1		
			print c
			for i in range(len(clusters)):
				clusters[i] = cluster_list[i]
		'''
		count+=1
		#print c
		for i in range(len(clusters)):
			clusters[i] = cluster_list[i]
	return point_dict

def validate_constraints(cluster, threshold,p,oc,arm):
	#print cluster
	#print arm
	c = cluster
	pv = p.value
	affinity = p.affinity
	if affinity == None:
		return True
	elif affinity == {} or oc == -1:
		return True
	else:
		aff_old = affinity[arm]
		if aff_old < threshold:
			#print 'Cluster values are changing'
			return False
		else:
			return True
