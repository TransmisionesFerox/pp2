def is_palindrome(text):
    cleaned_text = "".join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]

#exampl
print(is_palindrome("madam"))         #True
print(is_palindrome("nurses run"))    #True
print(is_palindrome("python"))        #False
print(is_palindrome("A man a plan a canal Panama")) #True
print(is_palindrome("12321"))         #True