import re
def find_upper_lower_sequences(text):
    pattern = r"[A-Z][a-z]+"
    matches = re.findall(pattern, text)
    return matches

#xample
text1 = "HiWorld myVar AnotherExamp"
text2 = "lowercase UPPERCASE Test2004"
text3 = "Astring Bword"

print(find_upper_lower_sequences(text1))  # ['HiWorld', 'Var', 'Examp']
print(find_upper_lower_sequences(text2))  # ['Test']
print(find_upper_lower_sequences(text3))  # ['Astring', 'Bword']