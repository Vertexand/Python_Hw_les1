# 1. Напишите программу, которая принимает на вход цифру,
#    обозначающую день недели, и проверяет, является ли этот день выходным.

num = int(input())

if 5 < num < 8:
    print("Weekend")
elif 0 < num < 6:
    print("Workday")
else:
    print("It's not a day of the week!")




# day = int(input('введите цифру дня недели  '))# вар 2
# if day == 6 or day ==7:
#     print("yes")
# else:
#     print("no")