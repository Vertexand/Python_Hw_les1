# 5. Напишите программу, которая принимает на вход координаты
#    двух точек и находит расстояние между ними в 2D пространстве.
   # https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

x_1 = int(input('x1 = '))
y_1 = int(input('y1 = '))
x_2 = int(input('x2 = '))
y_2 = int(input('y2 = '))

print('расстояние между точками 'f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5}")
