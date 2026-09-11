id = int(input("Введите количество строк"))
for i in range(1, id+1):
    name = str(input("Введите имя"))
    town = str(input("Введите название своего города"))
    age = int(input("Введите свой возраст"))
    height = int(input("Введите свой рост"))
    weight = int(input("Введите свой вес"))
    print(i, name, town, age, height, weight)