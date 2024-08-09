# perfect num or not
num = 6
num2 = 13
num3 = 28

def comperfnum(n):
    div_list = []
    for i in range(1,n):
        if n % i == 0:
            div_list.append(i)
    if sum(div_list) == n:
        return True
    else:
        return False

print(comperfnum(num))
print(comperfnum(num2))
print(comperfnum(num3))
