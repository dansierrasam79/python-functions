# return sorted string of words with hyphens
init_str = "green-red-yellow-black-white"
def retsrtstr(istr):
    ilst = []
    ilst = istr.split("-")
    ilst.sort()
    final_str = '-'.join(ilst)
    return final_str

print(retsrtstr(init_str))
