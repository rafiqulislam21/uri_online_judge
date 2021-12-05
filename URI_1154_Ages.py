age = 0
age_sum = 0
age_counter = 0
while(age >= 0):
    age = int(input())
    age_sum += age
    age_counter += 1
    
age_average = age_sum/age_counter

print(round(age_average,3))
    