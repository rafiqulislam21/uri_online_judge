def calculate(percent):
    moneyEarned = round((salary * (percent/100)), 2)
    newSalary = round(salary + moneyEarned, 2)
    print("Novo salario: {}".format("{:.2f}".format(newSalary)))
    print("Reajuste ganho: {}".format("{:.2f}".format(moneyEarned)))
    print("Em percentual: {} %".format(percent))
    
    
salary = round(float(input()), 2)
if salary >=0 and salary <= 400:
    calculate(15)
elif salary > 400 and salary <= 800:
    calculate(12)
elif salary > 800 and salary <= 1200:
    calculate(10)
elif salary > 1200 and salary <= 2000:
    calculate(7)
elif salary > 200:
    calculate(4)