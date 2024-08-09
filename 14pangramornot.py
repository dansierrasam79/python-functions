# pangram or not
alphabet_lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
init_str = "The quick brown fox jumps over the lazy dog"
init_str2 = "constantinople"

def ispangram(istr):
    no_dup_lst = []
    for letter in istr:
        print(letter)
        if letter in alphabet_lst and letter not in no_dup_lst:
            no_dup_lst.append(letter)
    if len(no_dup_lst) == 26:
        return True
    else:
        return False

print(ispangram(init_str))
print(ispangram(init_str2))
