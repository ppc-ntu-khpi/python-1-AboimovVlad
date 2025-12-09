# def sqrPlus1(x):
#   return x*x+1

# numbers=[]
# n = 1
# while True:
#   if n <= 10:
#     x = int(input(str(n)+" - введіть число від 0 до 10:"))

#     # вам треба дописати/змінити цей блок коду
#     if 0 <= x <= 10:
#     # кінець вашого коду
    
#       numbers.append(sqrPlus1(x))
#     else:
#       print("Потрібне число від 0 до 10!")
#   else:
#     break
#   n = n + 1
# print(numbers)


# 2 завдання: лямбда-функції

# add = lambda a, b: a + b
# sub = lambda a, b: a - b
# mul = lambda a, b: a * b
# div = lambda a, b: a / b if b != 0 else 0

# a = int(input("Введіть перше число:"))
# b = int(input("Введіть друге число:"))
# c = 0

# menu = {}
# menu['1']="Додати числа" 
# menu['2']="Відняти числа"
# menu['3']="Перемножити числа"
# menu['4']="Поділити числа"
# menu['5']="завершити роботу"
# options=menu.keys()
# for entry in options: 
#     print(entry, menu[entry])
# while True:   
#   selection=input("Оберіть операцію:") 
#   if selection =='1': 
#     print("Додавання:", add(a, b))
#   elif selection == '2': 
#     print("Віднімання:", sub(a, b))
#   elif selection == '3':
#     print("Множення:",mul(a, b))
#   elif selection == '4': 
#     print("Ділення",div(a, b))
#   elif selection == '5': 
#     break
#   else: 
#     print ("Невідома операція!")


# функція з аргументами за замовченням

def controlEngine(id, name, operation="стоп", priority="високий"):

  print('Агрегат:',name, '#',id, "\n\tОбрана операція:", operation ,"\n\tПриорітет:", priority)

controlEngine(1,"реактор")
controlEngine(1,"реактор","запуск")
controlEngine(1,"реактор", priority="звичайний")
controlEngine(operation = "запуск", id = 1,name = "реактор", priority = "звичайний")