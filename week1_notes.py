"""
Operators
- Boolean Operators
    <, >, >=, <=, ==, !=
- Maths
    +, -, *, /, %, //
- Augmented assignment
    +-, -=, *=, /=
- Precedence of operator
    1. ()
    2. **
    3. +x, -x
    4. *, /, %, //
    5. +, -
    6. Comparison (<, > ...)
    7. not x
    8. and
    9. or

Selection
- if
    if xxx > 10:
        print("It is greater")`
    elif xxx > 5:
        print("It is > 5")
    else:
        print("All not true")
- while
    while (x > 0):
        x -= 1
        print("xxx")
- for
    for num in range(1, 5, 1):
        print(num)
    # range(start, end, step)
- break
- continue

"""

for i in range(1, 10):
    if i % 3 == 0:
        continue
    else:
        print(i)
        print()
