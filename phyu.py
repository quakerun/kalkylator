what = input("Що робимо? (+, -, *, /): " )

a = float( input("Введіть перше число: ") )
b = float( input("Введіть друге число :") )

if b == 0:
    print("бля... в школі був?")
else:
    if what == "+":
        c = a + b
    elif what == "-":
        c = a - b
    elif what  ==  "*":
        c = a * b
    elif what == "/":
        c = a / b
    else:
        print("Що ти вибрав?")


    if what in("+","-","*","/"):
        print("Результат: " + str(c))