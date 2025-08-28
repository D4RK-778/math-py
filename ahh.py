x = input("Enter a number: ")
y = input("Enter another number: ")

def check(c, b):
    if b:
        return str(c) + "/" + str(b) + " = " + str(c/b) + "\n" + str(c) + "*" + str(b) + " = " + str(c*b) + "\n" + str(c) + "+" + str(b) + " = " + str(c+b) + "\n" + str(c) + "-" + str(b) + " = " + str(c-b)
        
print(check(x, y))
