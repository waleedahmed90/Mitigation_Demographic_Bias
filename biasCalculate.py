from math import sqrt
import time

def averageBias(dict):
	biasList = dict.values()

	return round((sum(biasList)/len(biasList)), 3)


def newBiasGend(dic1, baseline):
	weight_male = 0.48
	weight_female = 0.52

	#(M)/(F)====0.96

	weight_ratio = weight_male / weight_female

	temp_dict = {}

	for t in dic1.keys():
		demo = dic1[t]

		bias_temp = ( weight_ratio - ( demo[0] / demo[1] ) )
		bias = sqrt(bias_temp**2)


		temp_dict[t] = round(bias, 3)

	return temp_dict



def newBiasRace(dic1, baseline):

	weight_white = 0.5
	weight_black = 0.3
	weight_asian = 0.2

	#(W)/(B+A)====1.0

	weight_ratio = weight_white / (weight_black + weight_asian)


	temp_dict = {}
	for t in dic1.keys():
		demo = dic1[t]
		
		bias_temp = ( weight_ratio - (demo[0] / ( demo[1] + demo[2] ) ) )
		bias = sqrt(bias_temp**2)
		

		temp_dict[t] = round(bias, 3)

	return temp_dict 


def newBiasAge(dic1, baseline):

	weight_ado = 0.40		#(less than 20 years of age) 		#(adolescent)
	weight_old = 0.07 		#(above 65 years of age) 	 		#(old)
	weight_yng = 0.25 		#(between 20 and 40 years of age)	#(young)
	weight_mid = 0.28 		#(between 40 and 65 years of age)	#(mid-aged)

	#(O+Y)/(A+M)====0.47(apprx)

	weight_ratio = (weight_old + weight_yng) / (weight_ado + weight_mid)


	temp_dict = {}
	for t in dic1.keys():
		demo = dic1[t]


		bias_temp = ( weight_ratio - ( (demo[1] + demo[2]) / ( demo[0] + demo[3] ) ) )
		bias = sqrt(bias_temp**2)
		
		temp_dict[t] = round(bias, 3)

	return temp_dict 




def eval_Print(origDictProm, origDictAdop, prom_bias_dict, adop_bias_dict):

	for c in prom_bias_dict.keys():

		print("Promoter Cluster Demographics::::::::::::: ",origDictProm[c], "-BIAS= ", prom_bias_dict[c])
		#print("Adopter Cluster Demographics:::: ",origDictAdop[c], " --------BIAS= ", adop_bias_dict[c])
		print("After Bias MitigationCluster Demographics: ",origDictAdop[c], "-BIAS= ", adop_bias_dict[c])
		print("\n")




start_time = time.time()

############BASELINE DEMOGRAPHICS########US POPULATION###########
#[Male, Female]
base_demographics_gen = [0.48, 0.52]

#[White, Black, Asian] 
base_demographics_rac = [0.5, 0.3, 0.2] 

#[Adolescent(<20), Old(65+), Young(20-40), Mid-Aged(40-65)] 
base_demographics_age = [0.4, 0.07, 0.25, 0.28] 


###############Promoters Demographics, coalitions clusters#############

Gender_promoters = { 1: [65.454, 34.546],
					 2: [7.302, 92.698],
					 3: [93.219, 6.781],
					 4: [40.681, 59.319]}
prom_gen_bias = newBiasGend(Gender_promoters, base_demographics_gen)


Race_promoters = {  1: [47.859, 39.546, 12.594],
					2: [94.027, 2.995, 2.978],
					3: [71.914, 11.818, 16.269],
					4: [13.254, 3.472, 83.274],
					5: [6.397, 90.761, 2.842]}
prom_rac_bias = newBiasRace(Race_promoters, base_demographics_rac)


Age_promoters = { 1: [9.701, 1.053, 54.251, 34.995],
				  2: [82.751, 0.107, 13.614, 3.528],
				  3: [21.521, 0.259, 66.299, 11.921],
				  4: [2.238, 0.137, 9.423, 88.202],
				  5: [3.217, 0.1, 92.44, 4.243]}
prom_age_bias = newBiasAge(Age_promoters, base_demographics_age)




###############with penalties, coalitions clusters#############					 

Gender_w_penal = {   1: [60.899, 39.111],
					 2: [30.945, 69.055],
					 3: [76.152, 23.848],
					 4: [47.711, 52.289]}
pen_gen_bias = newBiasGend(Gender_w_penal, base_demographics_gen)


Race_w_penal = {  1: [50.55, 33.538, 15.912],
				  2: [79.274, 9.657, 11.069],
				  3: [66.779, 17.079, 16.142],
				  4: [44.251, 7.836, 47.913] ,
				  5: [36.708, 56.137, 7.155]}
pen_rac_bias = newBiasRace(Race_w_penal, base_demographics_rac)


Age_w_penal = {  1: [12.841, 0.85, 53.256, 33.052],
				 2: [54.712, 0.176, 39.306, 5.806],
				 3: [29.377, 0.174, 59.744, 10.705],
				 4: [5.65, 0.564, 37.03, 56.755],
				 5: [13.517, 0.245, 70.384, 15.854]}
pen_age_bias = newBiasAge(Age_w_penal, base_demographics_age)



print("\n\nBIASES AFTER PENALTIES ONLY")
print("\n\n <GENDER> BASE_WEIGHTS: ", base_demographics_gen)
eval_Print(Gender_promoters, Gender_w_penal, prom_gen_bias, pen_gen_bias)

print("(GENDER)_AVERAGE_BIAS_ORIGINAL:::::: ", averageBias(prom_gen_bias))
print("(GENDER)_AVERAGE_BIAS_MITIGATED::::: ", averageBias(pen_gen_bias))


print("\n\n <RACE> BASE_WEIGHTS: ", base_demographics_rac)
eval_Print(Race_promoters, Race_w_penal, prom_rac_bias, pen_rac_bias)

print("(RACE)_AVERAGE_BIAS_ORIGINAL:::::: ", averageBias(prom_rac_bias))
print("(RACE)_AVERAGE_BIAS_MITIGATED::::: ", averageBias(pen_rac_bias))



print("\n\n <AGE> BASE_WEIGHTS: ", base_demographics_age)
eval_Print(Age_promoters, Age_w_penal, prom_age_bias, pen_age_bias)

print("(AGE)_AVERAGE_BIAS_ORIGINAL:::::: ", averageBias(prom_age_bias))
print("(AGE)_AVERAGE_BIAS_MITIGATED::::: ", averageBias(pen_age_bias))





##########################PENALTIES WITH COMPENSATION####################################

Gender_w_comp = {    1: [59.284, 40.716],
					 2: [27.911, 72.089],
					 3: [74.96, 25.04],
					 4: [45.426, 54.574]}
comp_gen_bias = newBiasGend(Gender_w_comp, base_demographics_gen)


Race_w_comp = {   1: [60.43, 26.719, 12.851],
				  2: [77.595, 10.817, 11.588],
				  3: [57.211, 8.403, 34.386],
				  4: [28.144, 5.448, 66.408],
				  5: [33.614, 56.195, 10.191]}
comp_rac_bias = newBiasRace(Race_w_comp, base_demographics_rac)


Age_w_comp = {   1: [12.379, 0.81, 50.798, 36.012],
				 2: [64.01, 0.268, 30.172, 5.55],
				 3: [34.701, 0.198, 55.217, 9.884],
				 4: [4.902, 0.475, 30.626, 63.996],
				 5: [14.552, 0.267, 69.268, 15.913]}
comp_age_bias = newBiasAge(Age_w_comp, base_demographics_age)



print("BIASES AFTER COMPENSATION")
print("\n\n <GENDER> BASE_WEIGHTS: ", base_demographics_gen)
eval_Print(Gender_promoters, Gender_w_comp, prom_gen_bias, comp_gen_bias)

print("(GENDER)_AVERAGE_BIAS_ORIGINAL:::::: ", averageBias(prom_gen_bias))
print("(GENDER)_AVERAGE_BIAS_MITIGATED::::: ", averageBias(comp_gen_bias))



print("\n\n <RACE> BASE_WEIGHTS: ", base_demographics_rac)
eval_Print(Race_promoters, Race_w_comp, prom_rac_bias, comp_rac_bias)

print("(RACE)_AVERAGE_BIAS_ORIGINAL:::::: ", averageBias(prom_rac_bias))
print("(RACE)_AVERAGE_BIAS_MITIGATED::::: ", averageBias(comp_rac_bias))



print("\n\n <AGE> BASE_WEIGHTS: ", base_demographics_age)
eval_Print(Age_promoters, Age_w_comp, prom_age_bias, comp_age_bias)

print("(AGE)_AVERAGE_BIAS_ORIGINAL:::::: ", averageBias(prom_age_bias))
print("(AGE)_AVERAGE_BIAS_MITIGATED::::: ", averageBias(comp_age_bias))






print("\n\nElapsed Time")
print("--- %s seconds ---" % (time.time() - start_time))