# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record = np.array([[50,  9,  4,  1,  0,  0, 40,  0]])
print(new_record)

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

census = np.concatenate((data, new_record))


# --------------
#Code starts here
age = census[:,0]
print(age)

max_age = max(age)
print(max_age)

min_age = min(age)
print(min_age)

age_mean = np.mean(age)

age_std = np.std(age)


# --------------
#Code starts here
race = census[:,2]

race_0 = census[race == 0]
len_0 = len(race_0)
print(len_0)

race_1 = census[race == 1]
len_1 = len(race_1)
print(len_1)

race_2 = census[race == 2]
len_2 = len(race_2)
print(len_2)

race_3 = census[race == 3]
len_3 = len(race_3)
print(len_3)

race_4 = census[race == 4]
len_4 = len(race_4)
print(len_4)

minority_race = 3


# --------------
#Code starts here

senior_citizen = census[:,0].astype(np.int32) > 60
senior_citizens = census[census[:,0].astype(np.int32) > 60]    
work_hours = census[:,6]

work_ = work_hours[senior_citizen]
working_hours_sum = work_hours[senior_citizen].sum()

senior_citizens_len = len(work_)

avg_working_hours = working_hours_sum/ senior_citizens_len

print(avg_working_hours)




# --------------
#Code starts here
edu = census[:,1]

hi = edu > 10

high = census[hi]

lo = edu <= 10

low = census[lo]

income = census[:,7]

avg_pay_high = np.mean(income[hi])

avg_pay_low = np.mean(income[lo])




