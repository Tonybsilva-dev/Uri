a,b,c = map(float, input().split())
x,y,z = map(float, input().split())

Prod1 = b * c
Prod2 = y * z

Total = Prod1 + Prod2
print("VALOR A PAGAR: R$ %0.2f" %Total)
