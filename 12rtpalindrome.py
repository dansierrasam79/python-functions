# return palindrome or not
init_str = "madam"
init_str2 = "daniel"

def ispalindrome(istr):
    reversdtr = istr[::-1]
    if istr == reversdtr:
        return True
    else:
        return False

print(ispalindrome(init_str))
print(ispalindrome(init_str2))
