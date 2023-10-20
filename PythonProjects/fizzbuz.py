
# fizzbuzz.py
# This program prints the numbers from 1 to 100.
# But for multiples of three it prints "Fizz" instead of the number.
# For the multiples of five it prints "Buzz".
# For numbers which are multiples of both three and five it prints "FizzBuzz".

fizzbuzz = []
for i in range(1, 200):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz.append("FizzBuzz")
    elif i % 3 == 0:
        fizzbuzz.append("Fizz")
    elif i % 5 == 0:
        fizzbuzz.append("Buzz")
    else:
        fizzbuzz.append(i)
print(fizzbuzz)

