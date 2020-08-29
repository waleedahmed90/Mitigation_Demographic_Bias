# MITIGATION OF BIAS IN THE DEMOGRAPHIC COALITION FOR HASHTAG SELECTION


### A proxy for trend selection

To determine the popularity/trendworthiness of a hashtag h at a point(timestamp) tn, during a particular day, is determined by the following equation:

- **Eq(1)**

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/1.png?raw=true)

#### Surge Ratio

The surge ratio of a hashtag h at a timestamp tn is defined as follows:

*"The ratio between the number of users mentioning h, at timestamp tn and the number of users who mentioned h at the previous timestamp tn-1"*

Mathematically, it is defined by parts as follows:

- **Eq(2)**

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/2.png?raw=true)

#### Impact

The impact of a hashtag h until a certain timestamp tn is defined as a decay function as follows:

*"The product of average tweets for h until the previous timestamp than tn, times the reciprocal of the decay factor"*

Mathematically, it is given as follows:

- **Eq(3)**

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/3.png?raw=true)


  - The first component in the quation above is the average tweets per time stamp until tn
  - The second component determines the decay. The factor of decay is lambda times E
  - n is the count for the time stamp which is under consideration and total timestamps per day are 96 with 15 minutes apart
  - E is mathematically defined as follows:
  
![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/4.png?raw=true)

  - The maximum bound of n for one day is calculated as follows
  
![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/5.png?raw=true)

- where,

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/6.png?raw=true)
 

## Mitigation Strategy

The Mitigation Strategy involves assigning a weight based penalty to the surge while picking the top 10 trends.
The weights are assigned to the demographic constituents for a particular demographic.

For assigning the weights, following is considered:
- The sum of all weights must be equal to 1

Following are the assigned weights to the demographic constituents for their corresponding categories:

- **[GENDER BASE WEIGHTS]**
-- **[0.48, 0.52] = [Male, Female]**

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/7.png?raw=true) 
 
- **[RACE BASE WEIGHTS]**
-- **[0.5, 0.3, 0.2] = [White, Black, Asian]**

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/8.png?raw=true)

- **[AGE_GROUP BASE WEIGHTS]**
-- **[0.40, 0.07, 0.25, 0.28] = [Adolescent, Old, Young, Mid-Aged] = ['-20', '65+', '20-40', '40-65']**

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/9.png?raw=true)


### Identification of Dominant and Subservient Groups

*"A dominant group is defined as a Gender, Racial or an Age group (or a combinationof these groups) which is dominant in numbers or amount and the subservient group is defined as a Gender, Racial or an Age group (or a combination of these groups) which is not dominant in numbers or amount."*

We identify these groups in our Gender, Race, and Age-Group Category while considering the United States of America's population baseline Demographics before performing any sorts of calculations. We do this to be able to know this later on when we perform the calculation of clusters, that if a particular groups becomes too much in majority compared to the other one. The details of that baseline is given as follows:



| **US Population**      | % Male | %Female | %White | %Black | %Asian | %Adol. | %Old | %Young | %Mid-Aged |
| ---------------------- |--------|---------| -------|--------|--------|--------|------|--------|-----------|
|    Percentages         |  49.2  |   50.8  |  72.4  |   12.6 |   4.8  |  13.6  | 13.5 |  26.7  |    33.2   |


### Mitigation Approach
The approach is to add penalties while surge score is calculated. If the demographic is biased towards a particular Demographic group or a group of groups, its surge will be reduced. 

### Contemporary Dominant and Subservient Groups

It is very important to understand the contemporary dominant and subservient groups because that is important to understand the method behind the penalties and compensations.
If a demographic coalition behind a hashtag involves a group, being larger in numbers compared to the other groups, that group becomes a contemporary dominant group. The other(s) naturally will be considered as subservient groups.


### Penalties
The concept behind adding penalties is to finally obtain the trending topics whose demographic coalitions have a balanced representation between the pre-conceived and contemporary dominant and subservient group(s).

- The idea is to find out the contributions in the 'surge', which is being calculated in **Eq(1)**, by all the groups in the demographic coalition.
- The new surge will be then reduced. That reduction is determined by the base weight and the contribution from the group which has lesser majority in the contemporary demographic representation. Consider the following example, 

If a demographic coalition has two groups [A, B] with the base weights [0.5, 0.5], with surge = 100 and contemporary coalition [0.7, 0.3]. Contribution of A to the surge is 70 and that of B is 30. Here A is a contemporary dominant group and we calculate the newSurge under base weights while considering the contribution of the contemporay subservient group to be 30.

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/10.png?raw=true)

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/11.png?raw=true)

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/12.png?raw=true)

The group A had an edge of 40 in demographic coalition which will reduce the over all surge from 100 to 60.

Having more number of tweets per minute for a hashtag is good to increase the surge score but having a biased coalition behind it is actually going to be reduce the surge score is going to reduce as the percentage of a representation of a particular group increases.

### Compensation

We continue under the assumption that the pre-conceived dominant groups will not receive any compensation if they are under contemporary subservient status.

For calculating the compensation for subservient groups, we need to add some amount to the surge score if they are contemporarily dominant. For that we make use of the following scheme: 

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/13.png?raw=true)

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/14.png?raw=true)

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/15.png?raw=true)

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/16.png?raw=true)



*"The goal in the end is to have trending topics which have a more balanced demographic coalition behind them rather than being too biased towards a particular demographic group"*


### Bias Function

The bias function determines the distance between the weightRatio in base weights and the weightRatio in demographic coalition: The average bias is given by the following formula,

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/17.png?raw=true)

where,
- S is the set of selected trends/hashtags

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/18.png?raw=true)

![alt text](https://github.com/waleedahmed90/Mitigation_Demographic_Bias/blob/master/Eqs_Images/19.png?raw=true)

## Results
The results are given in RESULTS.txt file.

- The average Bias score is calculated after penalties without compensation and after penalties with compensation.
- The average bias reduces more if the compensation is added with penalties as compared to after applying only the penalties.

## Dataset

The dataset used is a property of the Max Planck Institute for Software Systems, Saarbrücken, Germany
