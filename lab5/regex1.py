import re

def match_ab(text):
    pattern = r"ab*"
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

#exmp
print(match_ab("a"))      #True
print(match_ab("ab"))     #True
print(match_ab("abb"))    #True
print(match_ab("ac"))     #False
print(match_ab("ba"))     #False