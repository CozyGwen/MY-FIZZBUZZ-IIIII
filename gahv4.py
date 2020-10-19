x = 0
f = "Fizz"
b = "Buzz"
q = "FizzBuzz"

while x <= 99:
    x = x + 1
    if x % 3 == 0 and x % 15 != 0:
        print(f)
    if x % 5 == 0 and x % 15 != 0:
        print(b)
    if x % 15 == 0:
        print(q)
    else:
        '\n'
    if x % 3 == 0:
        continue
    if x % 5 == 0:
        continue
    if x % 15 == 0:
        continue
    print(x)
