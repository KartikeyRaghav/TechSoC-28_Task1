from math import pi


def logarithm():
    base = float(input("Enter base for log: "))
    num = float(input("Enter number for log: "))

    temp = base
    power = ""

    found = False

    i = 0

    if num == 1 and base != 1 and base > 0:
        print("Log of", num, "to base", base, "is 0\n")
    elif num > 1 and base != 1 and base > 0:
        while temp <= num:
            temp = base**i
            if temp == num:
                print("Log of", num, "to base", base, "is", i, "\n")
                found = True
                break
            elif temp > num:
                if base > 1:
                    temp = base ** (i - 1)
                    power += str(i - 1)
                elif base < 1:
                    temp = base ** (i + 1)
                    power += str(i + 1)
                break
            if base > 1:
                i += 1
            elif base < 1:
                i -= 1
        if power == "":
            power = "0"
        power += "."
        if found != True:
            for iter in range(16):
                for j in range(10):
                    temp = base ** float(power + str(j))
                    if temp == num:
                        power += str(j - 1)
                        break
                    elif temp < num:
                        if j == 9 and temp < num:
                            power += str(j)
                    else:
                        temp = base ** float(power + str(j - 1))
                        power += str(j - 1)
                        break
            print("Log of", num, "to base", base, "is", power, "\n")
    elif num < 1 and num < base and num > 0 and base > 0 and base != 1:
        while temp > num:
            temp = base**i
            if temp == num:
                print("Log of", num, "to base", base, "is", i, "\n")
                found = True
                break
            elif temp < num:
                if base < 1:
                    temp = base ** (i - 1)
                    power += str(i - 1)
                elif base > 1:
                    temp = base ** (i + 1)
                    if i + 1 == 0:
                        power = "-0"
                    else:
                        power += str(i + 1)
                break
            if base < 1:
                i += 1
            elif base > 1:
                i -= 1
        power += "."
        if found != True:
            for iter in range(16):
                for j in range(10):
                    temp = base ** float(power + str(j))
                    if temp == num:
                        power += str(j - 1)
                        break
                    elif temp > num:
                        if j == 9 and temp > num:
                            power += str(j)
                    else:
                        temp = base ** float(power + str(j - 1))
                        power += str(j - 1)
                        break
            print("Log of", num, "to base", base, "is", power, "\n")
    else:
        print("Invalid Operation")


def basic():
    try:
        result = eval(input("Enter the expression: "))
        print(result, "\n")
    except:
        print("Error\n")


def exponent():
    try:
        base = float(input("Enter base: "))
        power = float(input("Enter power: "))
        print(base**power, "\n")
    except:
        print("Error\n")


def factorial(fac):
    a = 1
    for i in range(2, fac + 1):
        a *= i
    return a


def sin(rad):
    temp = rad
    op = "+"
    for i in range(3, 20, 2):
        if op == "+":
            temp -= rad**i / factorial(i)
            op = "-"
        else:
            temp += rad**i / factorial(i)
            op = "+"
    return temp


def cos(deg):
    rad = (90 - deg) * pi / 180
    temp = rad
    op = "+"
    for i in range(3, 20, 2):
        if op == "+":
            temp -= rad**i / factorial(i)
            op = "-"
        else:
            temp += rad**i / factorial(i)
            op = "+"
    return temp


def trigno():
    print()
    while True:
        trigno_options = """Which function:
1. sin
2. cos
3. tan
4. cosec
5. sec
6. cot
7. Exit
: """
        choosen_option = input(trigno_options)
        print()
        if choosen_option == "7":
            break
        elif choosen_option not in "1234567":
            print("Invalid input\n")
            continue
        deg = float(input("Enter angle in degrees: "))
        sign = ""
        if deg >= 360:
            deg %= 360
        if (choosen_option == "1" or choosen_option == "4") and (deg > 180):
            sign = "-"
        elif (choosen_option == "2" or choosen_option == "5") and (
            deg > 90 and deg < 270
        ):
            sign = "-"
        elif (choosen_option == "3" or choosen_option == "6") and (
            (deg > 90 and deg < 180) or (deg > 270 and deg < 360)
        ):
            sign = "-"
        if deg != 90 and deg != 270:
            deg %= 90
        else:
            deg = 90
        rad = deg * pi / 180
        if choosen_option == "1":
            print(sign + str(sin(rad)) + "\n")
        elif choosen_option == "2":
            print(sign + str(cos(deg)) + "\n")
        elif choosen_option == "3":
            if deg != 90:
                print(sign + str(sin(rad) / cos(deg)) + "\n")
            else:
                print("Invalid input\n")
        elif choosen_option == "4":
            if deg != 0:
                print(sign + str(1 / sin(rad)) + "\n")
            else:
                print("Invalid input\n")
        elif choosen_option == "5":
            if deg != 90:
                print(sign + str(1 / cos(deg)) + "\n")
            else:
                print("Invalid input\n")
        elif choosen_option == "6":
            if deg != 0:
                print(sign + str(cos(deg) / sin(rad)) + "\n")
            else:
                print("Invalid input\n")


def quadratic():
    a = float(input("Enter coefficient of second degree term: "))
    b = float(input("Enter coefficient of first degree term: "))
    c = float(input("Enter constant term: "))
    d = b**2 - 4 * a * c
    if d < 0:
        print("No real solution possible\n")
    else:
        sol1 = (-b + d**0.5) / 2 * a
        sol2 = (-b - d**0.5) / 2 * a
        print("The two solutions are", sol1, "and", sol2, "\n")


print("Welcome User!!!\n")
while True:
    main_options = """What do you want to do(Enter number only)
1. Basic operations(+,-,*,/,//,%)
2. Exponent
3. Logarithm
4. Trigonometric
5. Quadratic Equation
6. Exit
: """
    choosen_option = input(main_options)
    if choosen_option == "1":
        basic()
    elif choosen_option == "2":
        exponent()
    elif choosen_option == "3":
        logarithm()
    elif choosen_option == "4":
        trigno()
    elif choosen_option == "5":
        quadratic()
    elif choosen_option == "6":
        break
    else:
        print("Invalid input\n")
