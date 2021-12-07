age = 0
age_sum = 0
age_counter = 0
while(True):
    age = int(input())
    if age < 0:
        break
    else:
        age_sum += age
        age_counter += 1
        
age_average = age_sum/age_counter

print("{:.2f}".format(age_average))
    