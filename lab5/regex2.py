import re

def match_ab_range(text):
    pattern = r"ab{2,3}"
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

#exmpl
print(match_ab_range("abb"))     #True
print(match_ab_range("abbb"))    #True
print(match_ab_range("ab"))      #False
print(match_ab_range("abbbb"))   #False
print(match_ab_range("ac"))      #False