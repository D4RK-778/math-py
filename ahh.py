x = input("Enter a number: ")
y = input("Enter another number: ")

def check(c, b):
    z = int(c)
    if b:
        t = int(b)
        if z / t:
            cc = z / t
            i = z * t
            j = z + t  
            k = z - t
            l = z % t
            u = str(z)
            ccc = str(cc)
            o = str(t)
            return u + "/" + o + " = " + ccc + "\n" + u + "*" + o + " = " + str(i) + "\n" + u + "+" + o + " = " + str(j) + "\n" + u + "-" + o + " = " + str(k) + "\n" + u + "%" + o + " = " + str(l)

print(check(x, y))