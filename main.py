a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
d = (b**2)-(4*a*c)
if d < 0:
 print("Корней нет")
else:
 t = d**0.5
 x1 = (-b-t)/(2*a)
 x2 = (-b+t)/(2*a)
 print(x1)
 print(x2)