# find lst product
init_list = [8, 2, 3, -1, 7]

def fndproduct(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod

print(fndproduct(init_list))
