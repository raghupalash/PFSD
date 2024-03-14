# C = (°F - 32) × 5/9;
# F = C * (9/5) + 32

while True:
    t = input("Choose what you want to convert from: F or C: ").upper()
    if t == "F":
        f = float(input("Give me temprature in Fahrenheit: "))
        c = (f - 32) * 5 / 9
        c = round(c, 2)
        print("Temprature in celcius: ", c)
        break
    elif t == "C":
        c = float(input("Give me temprature in Celcius: "))
        f = c * (9 / 5) + 32
        f = round(f, 2)
        print("Temprature in fahrenheit: ", f)
        break
    else:
        print("Wrong input! try again!")
