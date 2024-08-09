# display squares between 1 to 30
num_lst = []
def compsqrs(strt,end):
    nums = []
    for i in range(strt,end+1):
        nums.append(i*i)
    return nums
num_lst = compsqrs(1,30)
print(num_lst)
