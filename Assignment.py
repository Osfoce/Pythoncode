print("choose operation")
operation =int(input("""Enter your operators in numbers,
    1 = +
    2 = -
    3 = *
    4 = /
    : """))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if operation == 1:
    res = x + y
    print("Result =", res)

elif operation == 2:
    res = x - y
    print("Result = ", res)

elif operation == 3:
    res = x * y
    print("Result = ", res)

elif operation == 4:
    res = x / y
    print("Result = ", res)
else:
    print("Wrong operator...!!")
