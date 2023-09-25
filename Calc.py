while True:
  s = input("Please enter a symbol (+, -, *, /): ")
  if s == '0':
     break
  if s in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print("%.2f" % (a + b))
        elif s == '-':
            print("%.2f" % (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("You can't divide by 0!")
  else:
        print("Invalid operation!")