def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# # Проверяем для 6
fizz_buzz(6)

# # Проверяем для 5
fizz_buzz(5)

# # Проверяем для 4
fizz_buzz(4)
