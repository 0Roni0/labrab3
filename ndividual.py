import math
print('ведите координаты точки А')
xA=float(input('xA:'))
yA=float(input('yA'))
print('Введите координаты точки В:')
xB=float(input('xB:'))
yB=float(input('yB'))
print('Введите координаты точки C:')
xC=float(input('xC:'))
yC=float(input('yC'))
AB=math.sqrt((xB-xA)**2+(yB-yA)**2)
BC=math.sqrt((xC-xB)**2+(yC-yB)**2)
AC=math.sqrt((xC-xA)**2+(yC-yA)**2)
P=AB+BC+AC
S=math.sqrt(P*(P-AB)*(P-BC)*(P-AC))
print ('Периметр равен',"%.2f"%P, 'Площадь равна',"%.2f"%S)