num_sum = 0
valid_counter = 0
invalid_counter = 0

while (valid_counter < 2):
    num = float(input())
    if num >= 0 and num <= 10:
        valid_counter += 1
        num_sum += num
    else:
        invalid_counter += 1

for i in range(invalid_counter):
    print("nota invalida")

print("media = {}".format(round(num_sum / valid_counter, 3)))