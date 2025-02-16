def square_numbers(n):
    for i in range(n + 1):
        yield i * i

N = int(input("Enter a number: "))
squares = square_numbers(N)
print(", ".join(map(str, squares)))