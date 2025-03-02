import math

def multiply_list(numbers):
    if not numbers:
        return 1 
    return math.prod(numbers)

#xmpl
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7]
numbers3 = []

print(multiply_list(numbers1))  # 24
print(multiply_list(numbers2))  # 210
print(multiply_list(numbers3))  # 1