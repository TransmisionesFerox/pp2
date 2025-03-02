import re
def find_lowercase_sequences(text):
    pattern = r"[a-z]+_[a-z]+"
    matches = re.findall(pattern, text)
    return matches

#exmp
text1 = "hi_world my_var another_examp"
text2 = "UPPER_CASE no_underscore lowercase_test"
text3 = "a_b c_d_e"

print(find_lowercase_sequences(text1))  # ['hi_world', 'my_var', 'another_examp']
print(find_lowercase_sequences(text2))  # ['lowercase_test']
print(find_lowercase_sequences(text3))  # ['a_b', 'c_d']