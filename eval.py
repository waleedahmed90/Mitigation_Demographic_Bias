#Evaluations on the trending topics


import gzip
import json
import glob
import itertools
import ntpath
import time
import os
import shutil
import operator
from math import sqrt
import time



def averageBiasScoreGend(dict, w_ratio):

	counter = 0
	biasSum = 0
	t_ratio = 0

	for t in dict.keys():
		[M, F] = dict[t]
		counter = counter + 1


		if F==0:
			t_ratio = M
		else:
			t_ratio = M/F

		bias = sqrt( ( w_ratio - t_ratio )**2 )
		biasSum = biasSum + bias


	ave_Bias = biasSum / counter

	return round(ave_Bias, 3)



def averageBiasScoreRace(dict, w_ratio):

	counter = 0
	biasSum = 0
	t_ratio = 0

	for t in dict.keys():
		[W, B, A] = dict[t]
		counter = counter + 1


		if (B+A)==0:
			t_ratio = W
		else:
			t_ratio = W/(B+A)

		bias = sqrt( ( w_ratio - t_ratio )**2 )
		biasSum = biasSum + bias


	ave_Bias = biasSum / counter

	return round(ave_Bias, 3)



def averageBiasScoreAge(dict, w_ratio):

	counter = 0
	biasSum = 0
	t_ratio = 0

	for t in dict.keys():
		[A, O, Y, M] = dict[t]
		counter = counter + 1

		if (A+M)==0:
			t_ratio = (O+Y)
		else:
			t_ratio = (O+Y)/(A+M)

		bias = sqrt( ( w_ratio - t_ratio )**2 )
		biasSum = biasSum + bias


	ave_Bias = biasSum / counter

	return round(ave_Bias, 3)


###################################################################################################
start_time = time.time()




# path_gender = "./Mitigation_Trending_UsageData/trending_gend_perc.gz"
# path_race = "./Mitigation_Trending_UsageData/trending_race_perc.gz"
# path_age = "./Mitigation_Trending_UsageData/trending_age_perc.gz"

path_gender = "./Mitigation_Trending_UsageData with compensation/trending_gend_perc.gz"
path_race = "./Mitigation_Trending_UsageData with compensation/trending_race_perc.gz"
path_age = "./Mitigation_Trending_UsageData with compensation/trending_age_perc.gz"

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


# path_gender_clus = './Clusters_Demographics/Gender_Clusters.gz'
# path_race_clus = './Clusters_Demographics/Race_Clusters.gz'
# path_age_clus = './Clusters_Demographics/Age_Clusters.gz'

path_gender_clus = './Clusters_Demographics wtih compensation/Gender_Clusters.gz'
path_race_clus = './Clusters_Demographics wtih compensation/Race_Clusters.gz'
path_age_clus = './Clusters_Demographics wtih compensation/Age_Clusters.gz'


#Loading dictionaries of Promoter percentage Gender
with gzip.open(path_gender_clus,'rt') as T1:
	demo_gender_temp = T1.read()
T1.close()

stats_gender_clus = json.loads(demo_gender_temp)

#Loading dictionaries of Promoter percentage Race
with gzip.open(path_race_clus,'rt') as T2:
	demo_race_temp = T2.read()
T2.close()

stats_race_clus = json.loads(demo_race_temp)

#Loading dictionaries of Promoter percentage Age
with gzip.open(path_age_clus,'rt') as T3:
	demo_age_temp = T3.read()
T3.close()

stats_age_clus = json.loads(demo_age_temp)


print("WITH PENALTIES AND COMPENSATION")
for c in stats_gender_clus.keys():

	clus_name = c

	clus_details = stats_gender_clus[clus_name]

	temp = {}

	for h in clus_details:

		temp[h] = stats_gender[h]

	print(c,":: Average Bias Score: ", averageBiasScoreGend(temp, (0.48/0.52)))


for c in stats_race_clus.keys():

	clus_name = c

	clus_details = stats_race_clus[clus_name]

	temp = {}

	for h in clus_details:

		temp[h] = stats_race[h]

	print(c,":: Average Bias Score: ", averageBiasScoreRace(temp, (0.5/(0.3+0.2))))


for c in stats_age_clus.keys():

	clus_name = c

	clus_details = stats_age_clus[clus_name]

	temp = {}

	for h in clus_details:

		temp[h] = stats_age[h]

	print(c,":: Average Bias Score: ", averageBiasScoreAge(temp, ((0.07+0.25)/(0.40+0.28))))










print("\n\nElapsed Time")
print("--- %s seconds ---" % (time.time() - start_time))