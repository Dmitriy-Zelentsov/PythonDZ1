# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите значение x1 = '))
y1 = int(input('Введите значение y1 = '))
x2 = int(input('Введите значение x2 = '))
y2 = int(input('Введите значение y2 = '))

print(float(((x2-x1)**2+(y2-y1)**2)**0.5))