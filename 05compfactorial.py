# compute factorial
num = 3
def compfact(fact_num):
    fact = 1
    for i in range(1,fact_num+1):
        fact *= i
    return fact
print(compfact(num))
