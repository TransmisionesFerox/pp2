#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
#3
def solve(numheads, numlegs):
    #check if the problem has valid solution
    if numlegs % 2 != 0 or numheads > numlegs // 2:
        return "No solution"

    #calculate the number of rabbits and chickens
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits

    #check if the calculated numbers are valid
    if rabbits < 0 or chickens < 0:
        return "No solution"

    return f"Rabbits: {rabbits}, Chickens: {chickens}"
#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]




