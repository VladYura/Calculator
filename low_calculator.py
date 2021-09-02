import math


Input = lambda x: float(input(f"Введите {x} число: "))
sum = lambda x, y: x + y
diff = lambda x, y: x - y
op = lambda x, y: x * y
quo = lambda x, y: x / y
deg = lambda x, y: x**y
fabs = lambda x: abs(x)
dagr = lambda x, y: x / y * 100


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


def View():
    print("-----Калькулятор-----")

    for i, j in options.items():
        print(f"{i}: {j}")

    choice = input("\nВыберите действие: ")

    if choice == '1':
        print(f"\nОтвет: {sum(Input('первое'), Input('второе'))}")
    elif choice == '2':
        print(f"\nОтвет: {diff(Input('первое'), Input('второе'))}")
    elif choice == '3':
        print(f"\nОтвет: {op(Input('первое'), Input('второе'))}")
    elif choice == '4':
        try:
            print(f"\nОтвет: {quo(Input('первое'), Input('второе'))}")
        except ZeroDivisionError:
            print("\nДелить на ноль нельзя!")
    elif choice == '5':
        a = int(input("Введите число: "))
        if a == abs(a):
            print(f"\nОтвет: {fact(a)}")
        else:
            print("\nФакториал принимает только натуральные числа!")
    elif choice == '6':
        print(f"\nОтвет: {deg(float(input('Введите число: ')), float(input('Введите степень: ')))}")
    elif choice == '7':
        print(f"\nОтвет: {fabs(float(input('Введите число: ')))}")
    elif choice == '8':
        a = float(input("Введите число: "))
        b = float(input("Введите основание: "))
        if (a != 1 and a > 0) and b > 0:
            print(f"\nОтвет: {math.log(a, b)}")
        else:
            print("\nВы не знаете свойства логарифма!")
    elif choice == '9':
        try:
            print(f"\nОтвет: {dagr(Input('первое'), Input('второе'))}")
        except ZeroDivisionError:
            print("\nДелить на ноль нельзя!")
    else:
        print("\nТакого действия нет!")


options = {'1': "+",
           '2': "-",
           '3': "*",
           '4': "/",
           '5': "Факториал",
           '6': "Возвести в степень",
           '7': "Модуль",
           '8': "Логарифм",
           '9': "Процентное соотношение"}

word = ['первое', 'второе']

while True:
    View()
    if input("\nВведите n для выхода...") == 'n':
        break
