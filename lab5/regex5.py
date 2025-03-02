import re
def match_a_anything_b(text):
    pattern = r"a.*b$"
    if re.search(pattern, text):
        return True
    else:
        return False

# xample
print(match_a_anything_b("axyzb"))    #True
print(match_a_anything_b("a123b"))    #True
print(match_a_anything_b("ab"))       #True
print(match_a_anything_b("afx"))      #False
print(match_a_anything_b("baxy"))     #False
print(match_a_anything_b("axybc"))    #True