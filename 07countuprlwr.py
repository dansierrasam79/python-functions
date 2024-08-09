# counts upper and lower case nums
init_str = 'The quick Brow Fox'
count_list = []
def countuprlwr(sentence):
    count_lwr, count_upr = 0,0
    for letter in sentence:
        if letter.islower():
            count_lwr += 1
        elif letter.isupper():
            count_upr += 1
    count_list.append(count_lwr)
    count_list.append(count_upr)
countuprlwr(init_str)
print(count_list)
