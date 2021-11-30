days = int(input())

year = int(days/365)
month = int((days%365)/30)
day = int(((days%365)%30)/1)

print("{} ano(s)".format(year))
print("{} mes(es)".format(month))
print("{} dia(s)".format(day))
