# check for prime
num = 8
num2 = 3

def chckprime(n):
    count_prm = 0
    for i in range(1,n+1):
        if n % i == 0:
            count_prm += 1
    if count_prm == 2:
        return True
    else:
        return False

print(chckprime(num))
print(chckprime(num2))
