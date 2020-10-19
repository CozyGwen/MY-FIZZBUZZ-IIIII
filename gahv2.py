x = 0
f = "Fizz"
b = "Buzz"
q = "FizzBuzz"

while x <= 99:
    x = x + 1
    if x % 3 == 0 and x != 0 and x % 15 != 0:
        '\r, flush=True'
        print(f)
    if x % 5 == 0 and x != 0 and x % 15 != 0:
        '\r, flush=True'
        print(b)
    if x % 15 == 0 and x != 0:
        '\r, flush=True'
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
