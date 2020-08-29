#/Users/WaleedAhmed/Documents/THESIS_DS_CODE/part2_Mitigation/Mitigation_Trending_UsageData

import time
start_time = time.time()

import gzip
import json
import numpy as np

from pandas import DataFrame
from sklearn.cluster import KMeans
import os
import shutil


def removingOldAge(dict_age):
	new_dict = {}

	for h in dict_age.keys():
		dict_age[h].remove((dict_age[h])[1])
		
	new_dict = dict_age
	return new_dict


#This function counts the top_h hashtags assigned to every cluster centroid
def topHashtagsPerCluster(top_h, Cluster_details, Sorted_Dictionary, T_Count):

	keys__1 = list(T_Count.keys())
	for cent in Cluster_details:
		hash_list = Cluster_details[cent]
		print("\nCLUSTER: ",cent, ": ", keys__1[cent])
		TEMP_DICT = {}

		for h in hash_list:
			TEMP_DICT[h] = Sorted_Dictionary[h]

		temp_sort_demo = sorted(TEMP_DICT.items(), key = lambda x: x[1], reverse=True)

		flag_1 = 0
		for i in temp_sort_demo:
			if not flag_1==top_h:
				print(i[0], " ::: ", i[1])
				flag_1 = flag_1+1


def nameClusterRoundOff(list_cent_r):
	x = list_cent_r
	y = [round(i, 3) for i in x]
	clus_name = str(y)
	return clus_name

def printClusterAssignmentDetails(clus_detail):
	for i in clus_detail:
		print(i,": ", clus_detail[i])



def clusterGrouping (hashtags, labels, centroids, n_clus):
	#has
	clusterDetails = {}

	for i in range(0, n_clus):
		clusterDetails[i]=[]
	

	for p in range(len(labels)):

		cluster_number = labels[p]
		hashtagName = hashtags[p]
	
		clusterDetails[cluster_number].append(hashtagName)	

	return clusterDetails



def clustering (dataset, n_clus):
	#dataset: dictionary of stats
	#n_clus: No of cluster

	df = DataFrame(dataset, columns=dataset.keys())
	df = df.T

	kmeans = KMeans(n_clusters=n_clus).fit(df)
	
	#cluster centers
	centroids = kmeans.cluster_centers_
	#assined clusters
	labels = kmeans.labels_
	#names of hashtags
	hashtag_names = df.index.values


	#function call
	clusterDetails = clusterGrouping(hashtag_names, labels, centroids, n_clus)

	return df, centroids, clusterDetails, labels, hashtag_names


path_gender = "./Mitigation_Trending_UsageData/trending_gend_perc.gz"
path_race = "./Mitigation_Trending_UsageData/trending_race_perc.gz"
path_age = "./Mitigation_Trending_UsageData/trending_age_perc.gz"


#Loading dictionaries of Promoter percentage Gender
with gzip.open(path_gender,'rt') as T1:
	demo_gender_temp = T1.read()
T1.close()

stats_gender = json.loads(demo_gender_temp)

#Loading dictionaries of Promoter percentage Race
with gzip.open(path_race,'rt') as T2:
	demo_race_temp = T2.read()
T2.close()

stats_race = json.loads(demo_race_temp)

#Loading dictionaries of Promoter percentage Age
with gzip.open(path_age,'rt') as T3:
	demo_age_temp = T3.read()
T3.close()

stats_age = json.loads(demo_age_temp)

dataset_g = stats_gender
n_clus_g = 4

dataset_r = stats_race
n_clus_r = 5

dataset_a = stats_age
n_clus_a = 5

# dataset_a = removingOldAge(stats_age)
# n_clus_a = 5


df_g, centroids_g, clusterDetails_g, labels_g, hashtag_names_g = clustering (dataset_g, n_clus_g)
df_r, centroids_r, clusterDetails_r, labels_r, hashtag_names_r = clustering (dataset_r, n_clus_r)
df_a, centroids_a, clusterDetails_a, labels_a, hashtag_names_a = clustering (dataset_a, n_clus_a)


######Trend_counts######
T_Count_Gender = {}
T_Count_Race = {}
T_Count_Age = {}

#Clusters:
Gender_Clusters = {}
Race_Clusters = {}
Age_Clusters = {}


list_cent_g = centroids_g.tolist()
list_cent_r = centroids_r.tolist()
list_cent_a = centroids_a.tolist()


for c in clusterDetails_g:
	temp_clus_name = nameClusterRoundOff(list_cent_g[c])
	T_Count_Gender[temp_clus_name] = len(clusterDetails_g[c])
	Gender_Clusters[temp_clus_name] = clusterDetails_g[c]

for c in clusterDetails_r:
	temp_clus_name = nameClusterRoundOff(list_cent_r[c])
	T_Count_Race[temp_clus_name] = len(clusterDetails_r[c])
	Race_Clusters[temp_clus_name] = clusterDetails_r[c]

for c in clusterDetails_a:
	temp_clus_name = nameClusterRoundOff(list_cent_a[c])
	T_Count_Age[temp_clus_name] = len(clusterDetails_a[c])
	Age_Clusters[temp_clus_name] = clusterDetails_a[c]



print("GENDER_CLUSTERS_HASHTAGS_COUNTS")
printClusterAssignmentDetails(T_Count_Gender)

print("\nRACE_CLUSTERS_HASHTAGS_COUNTS")
printClusterAssignmentDetails(T_Count_Race)

print("\nAGE_CLUSTERS_HASHTAGS_COUNTS")
printClusterAssignmentDetails(T_Count_Age)



with gzip.open('./SortedDict/Sorted_Dictionary.gz', 'rt') as T4:
	Sorted_Dictionary_temp = T4.read()
T4.close()

Sorted_dictionary = json.loads(Sorted_Dictionary_temp)

#########################################################

#Gender
top_h = 13
Cluster_details = clusterDetails_g
T_Count = T_Count_Gender
print("\n\n#########################################")
print("GENDER [MALE, FEMALE]")
topHashtagsPerCluster(top_h, Cluster_details, Sorted_dictionary, T_Count)

#Race
top_h=13
Cluster_details = clusterDetails_r
T_Count = T_Count_Race
print("\n\n#########################################")
print("RACE [WHITE, BLACK, ASIAN]")
topHashtagsPerCluster(top_h, Cluster_details, Sorted_dictionary, T_Count)

#Age
top_h = 13
Cluster_details = clusterDetails_a
T_Count = T_Count_Age
print("\n\n#########################################")
print("AGE ['-20', '65+', '20-40', '40-65']")
topHashtagsPerCluster(top_h, Cluster_details, Sorted_dictionary, T_Count)


try:
	os.mkdir('./Clusters_Demographics')
except:
	shutil.rmtree('./Clusters_Demographics', ignore_errors=True)
	os.mkdir('./Clusters_Demographics')


with gzip.open('./Clusters_Demographics/Gender_Clusters.gz', 'wb') as f1:
	f1.write(json.dumps(Gender_Clusters).encode('utf-8'))
f1.close()
print("<./Clusters_Demographics/Gender_Clusters.gz>:::::Written")
	
with gzip.open('./Clusters_Demographics/Race_Clusters.gz', 'wb') as f2:
	f2.write(json.dumps(Race_Clusters).encode('utf-8'))
f2.close()
print("<./Clusters_Demographics/Race_Clusters.gz>:::::Written")

with gzip.open('./Clusters_Demographics/Age_Clusters.gz', 'wb') as f3:
	f3.write(json.dumps(Age_Clusters).encode('utf-8'))
f3.close()
print("<./Clusters_Demographics/Age_Clusters.gz>:::::Written")



print("Elapsed Time")
print("--- %s seconds ---" % (time.time() - start_time))