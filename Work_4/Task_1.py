# Задача 1. Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду).В этом классе реализуйте метод show_my_drink(),
# выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
# а иначе отобразится следующая фраза: «Обычная газировка».При решении задания можно дополнительно
# проверить тип передаваемого аргумента: принимается только строка.

class Soda:
    def __init__(self, additive=""):
        self.additive = additive

    def show_my_drink(self):
        if (type(self.additive) == str):
            if (self.additive):
                print(f"Газировка и {self.additive}")
            else:
                print("Обычная газировка")
        else:
            print("Если кто то зайдёт в это тело то он гей )")


cola = Soda("Сахар")
cola.show_my_drink()

pepsa = Soda()
pepsa.show_my_drink()

sprite = Soda(55)
sprite.show_my_drink()
