# return unique elems only
init_list = [1,2,3,3,3,3,4,5]
final_list = []

def retuniqlst(lst):
    for num in lst:
        if num not in final_list:
            final_list.append(num)

retuniqlst(init_list)
print(final_list)
