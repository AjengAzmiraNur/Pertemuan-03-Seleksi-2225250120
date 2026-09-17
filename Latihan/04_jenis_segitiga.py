a = float(input("sisi a: "))
b = float(input("sisi b: "))
c = float(input("sisi c:"))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("segitiga sama sisi")
    else: 
        if a == b or a == c or b == c:
            print("segitiga sama kaki")
        else: 
            print("segitiga sembarang")
else:
    print("ketiga sisi tidak membentuk segitiga")