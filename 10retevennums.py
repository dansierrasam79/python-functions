#return even nums in list
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []
def retevens(lst):
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
retevens(init_list)
print(even_list)
