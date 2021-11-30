salary = round(float(input()), 2)

if 0 <= salary <= 2000:
    print("Isento")
elif 2000 < salary <= 3000:
    t = (salary-2000)
    tax = t * (8/100)
    print("R$ {}".format("{:.2f}".format(tax,2)))
elif 3000 < salary <= 4500:
    t = (salary-2000)
    t1 = (t-1000)
    tax1 = (t-t1) * (8/100)
    tax2 = t1 * (18/100)
    tax = tax1+tax2
    print("R$ {}".format("{:.2f}".format(tax,2)))
elif salary > 4500:
    t = (salary-2000)
    t1 = (t-1000)
    t2 = (t1-1500)
    tax1 = (t-t1) * (8/100)
    tax2 = (t1-t2) * (18/100)
    tax3 = t2 * (28/100)
    tax = tax1+tax2+tax3
    print("R$ {}".format("{:.2f}".format(tax,2)))