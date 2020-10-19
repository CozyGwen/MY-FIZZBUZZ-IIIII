x = 0
f = "Fizz"
b = "Buzz"
q = "Fizz Buzz"


def unless():
    o = 1
    o = o + 1
    y = 15
    y = y + 15
    if o % 3 == 0:
        print(end='\r', flush=True)
    if o % 5 == 0:
        print(end='\r', flush=True)
    if o == y:
        print(end='\r', flush=True)
    else:
        '\n'


while x <= 99:
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
    x = x + 1
    if x % 3 == 0:
        continue
    if x % 5 == 0:
        continue
    if x % 15 == 0:
        continue
    print(x)
