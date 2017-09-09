mike = ["белая рубашка", "комбинезон цвета хаки", "пиджак"]
mr_dawson = mike
honey = mike
print("mike(original): ", mike)
print("mr_dawson(copy mike): ", mr_dawson)
print("honey(copy mike): ", honey)
honey[2] = "красный свитер"
print("change honey")
print("honey(copy mike): ", honey)
print("honey(copy mike): ", mike)
print("honey(copy mike): ", mr_dawson)

mike = ["белая рубашка", "комбинезон цвета хаки", "пиджак"]
honey = mike[:]
honey[2] = "красный свитер"
print(honey)
print(mike)
