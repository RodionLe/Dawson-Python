mike = ["белая рубашка", "комбинезон цвета хаки", "пиджак"]
mr_dawson = mike
honey = mike
print(mike)
print(mr_dawson)
print(honey)
honey[2] = "красный свитер"
print(honey)
print(mike)
print(mr_dawson)

mike = ["белая рубашка", "комбинезон цвета хаки", "пиджак"]
honey = mike[:]
honey[2] = "красный свитер"
print(honey)
print(mike)
